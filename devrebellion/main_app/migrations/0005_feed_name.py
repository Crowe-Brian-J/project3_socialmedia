# Generated by Django 4.2.2 on 2023-06-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_comment_user_alter_feed_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
