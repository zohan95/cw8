# Generated by Django 2.2 on 2019-11-16 06:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Название')),
                ('category', models.CharField(choices=[('fruits', 'Фрукты'), ('wear', 'Одежда'), ('other', 'Другое')],
                                              default='other', max_length=63, verbose_name='Категории')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('image',
                 models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Картинка товара')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(max_length=511, verbose_name='Текст отзыва')),
                ('mark', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5),
                                                                            django.core.validators.MinValueValidator(
                                                                                1)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='review_user',
                                             to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product',
                                   to='webapp.Product', verbose_name='Товар')),
            ],
        ),
    ]
