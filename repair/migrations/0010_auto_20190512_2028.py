# Generated by Django 2.1.7 on 2019-05-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0009_auto_20190512_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phoneproblem',
            old_name='problem_type',
            new_name='problem',
        ),
    ]
