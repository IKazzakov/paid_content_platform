# Generated by Django 4.2.9 on 2024-04-22 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('published_on', models.BooleanField(default=False, verbose_name='Published on')),
                ('views', models.IntegerField(blank=True, default=0, null=True, verbose_name='Views')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is paid')),
                ('comment', models.ManyToManyField(blank=True, null=True, to='blog.comment', verbose_name='Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]