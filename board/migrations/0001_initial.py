# Generated by Django 5.0.7 on 2024-07-11 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
                ('name', models.CharField(blank=True, default='Anonymous', max_length=255)),
                ('image_url', models.CharField(blank=True, default='', max_length=1024)),
                ('post_text', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.post')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
            ],
            bases=('board.post',),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.post')),
                ('corresponding_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='board.thread')),
            ],
            bases=('board.post',),
        ),
    ]