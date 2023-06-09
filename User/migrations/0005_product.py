# Generated by Django 4.1.7 on 2023-03-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
