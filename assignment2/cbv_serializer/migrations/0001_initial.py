# Generated by Django 5.1.3 on 2024-12-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]