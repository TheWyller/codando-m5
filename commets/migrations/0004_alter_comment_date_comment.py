# Generated by Django 4.0.5 on 2022-11-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commets', '0003_alter_comment_post_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
