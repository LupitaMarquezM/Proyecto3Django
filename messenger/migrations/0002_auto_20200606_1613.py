# Generated by Django 3.0.6 on 2020-06-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='contente',
            new_name='content',
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
