# Generated by Django 5.0.2 on 2024-03-06 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='url',
            new_name='url_content',
        ),
    ]
