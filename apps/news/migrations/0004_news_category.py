# Generated by Django 5.1.1 on 2024-09-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_subcategory_options_and_more'),
        ('news', '0003_comment_is_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='category_news', to='menu.category', verbose_name='Категория'),
        ),
    ]
