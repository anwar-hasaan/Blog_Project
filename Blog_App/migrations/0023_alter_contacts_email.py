# Generated by Django 3.2.7 on 2021-09-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0022_alter_blog_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
