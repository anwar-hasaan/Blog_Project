# Generated by Django 3.1.1 on 2021-09-04 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0003_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_comment',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog_App.blog_comment'),
        ),
    ]
