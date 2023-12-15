# Generated by Django 4.2.6 on 2023-12-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
