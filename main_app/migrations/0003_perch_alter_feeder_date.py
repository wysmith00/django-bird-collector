# Generated by Django 5.0.1 on 2024-02-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='feeder',
            name='date',
            field=models.DateField(verbose_name='Seen eating at the Feeder'),
        ),
    ]