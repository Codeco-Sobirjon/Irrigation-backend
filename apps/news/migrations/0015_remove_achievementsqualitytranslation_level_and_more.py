# Generated by Django 5.1.1 on 2024-09-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_achievementscategory_achievementsquality_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievementsqualitytranslation',
            name='level',
        ),
        migrations.AddField(
            model_name='achievementsquality',
            name='level',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Уровень достижений'),
        ),
    ]
