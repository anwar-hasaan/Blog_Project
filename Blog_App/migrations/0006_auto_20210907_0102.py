# Generated by Django 3.2.7 on 2021-09-07 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog_App', '0005_auto_20210905_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_comment',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog_App.blog_comment'),
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('sn_no', models.AutoField(primary_key=True, serialize=False)),
                ('auth_token', models.CharField(max_length=150)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
