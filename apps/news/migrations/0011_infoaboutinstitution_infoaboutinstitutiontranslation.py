# Generated by Django 5.1.1 on 2024-09-21 05:19

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_subcategory_options_and_more'),
        ('news', '0010_alter_comment_options_alter_contactinfo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAboutInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='category_info', to='menu.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': '4. Другая информация об институте',
                'verbose_name_plural': '4. Другая информация об институте',
                'ordering': ['id'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InfoAboutInstitutionTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='news.infoaboutinstitution')),
            ],
            options={
                'verbose_name': '4. Другая информация об институте Translation',
                'db_table': 'news_infoaboutinstitution_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
