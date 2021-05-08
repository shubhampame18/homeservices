# Generated by Django 3.2 on 2021-05-06 07:51

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
            name='CustomerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('image', models.FileField(upload_to='')),
                ('usertype', models.CharField(max_length=15)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]