# Generated by Django 4.1.7 on 2023-04-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('heading', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('fees', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
