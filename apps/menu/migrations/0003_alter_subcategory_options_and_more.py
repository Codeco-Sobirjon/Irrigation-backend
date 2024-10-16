# Generated by Django 5.1.1 on 2024-09-14 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_subcategory_tertiarycategory_toplevelcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегория'},
        ),
        migrations.AlterModelOptions(
            name='tertiarycategory',
            options={'verbose_name': 'Третичная категория', 'verbose_name_plural': 'Третичная категория'},
        ),
        migrations.AlterModelOptions(
            name='toplevelcategory',
            options={'verbose_name': 'Основная категория', 'verbose_name_plural': 'Основная категория'},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='menu.category', verbose_name='Родитель категории'),
        ),
    ]
