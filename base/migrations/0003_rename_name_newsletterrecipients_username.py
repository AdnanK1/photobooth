# Generated by Django 4.0.5 on 2022-06-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_newsletterrecipients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletterrecipients',
            old_name='name',
            new_name='username',
        ),
    ]
