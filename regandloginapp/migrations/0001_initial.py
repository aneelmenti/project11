# Generated by Django 4.2.1 on 2023-05-04 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('mobno', models.IntegerField()),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]
