from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    password = forms.CharField(max_length=100, required=True, label='Password',
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password confirm',
                                       widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='Email' )
    first_name = forms.CharField(max_length=100, label='First name', required=False)
    second_name = forms.CharField(max_length=100, label='Second Name', required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already taken.', code='username_taken')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered.', code='email_registered')
        except User.DoesNotExist:
            return email

    def clean_second_name(self):
        f_name = self.cleaned_data.get('first_name')
        s_name = self.cleaned_data.get('second_name')
        print(f_name, s_name)
        if not (f_name or s_name):
            raise ValidationError('Enter First or Second name')

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='passwords_do_not_match')
        return self.cleaned_data



class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)
    birth_date = forms.DateField(label='День рождения', input_formats=['%Y-%m-%d', '%d.%m.%Y'], required=False)
    about = forms.CharField(label='О себе', required=False)
    git_hub = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'http://github.com/<username>/'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'birth_date', 'about', 'git_hub']
        profile_fields = ['avatar', 'birth_date', 'about', 'git_hub']

        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}

    def clean_git_hub(self):
        git_hub = self.cleaned_data.get('git_hub')
        print(git_hub)
        if git_hub[:17]!='http://github.com' and git_hub[:18]!='https://github.com':
            raise ValidationError('Please enter: http://github.com/<username>')
        else:
            return git_hub

    def save(self, commit=True):

        user = super().save(commit)

        self.save_profile(commit)

        return user

    def save_profile(self, commit=True):

        profile = self.instance.profile

        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()

    def get_initial_for_field(self, field, field_name):

        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)

        return super().get_initial_for_field(field, field_name)


class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, required=True, label='New Password',
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='New Password confirm',
                                       widget=forms.PasswordInput)
    old_password = forms.CharField(max_length=100, required=True, label='Old Password',
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password.', code='invalid_password')
        return old_password

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='passwords_do_not_match')
        return self.cleaned_data

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']