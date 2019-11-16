from django import forms

from webapp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['product', 'author']