# Generated by Django 4.0.3 on 2022-06-27 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options_reviews_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-total_vote', 'title']},
        ),
    ]
