# Generated by Django 3.2.7 on 2021-11-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean', models.CharField(max_length=60, verbose_name='Korean')),
                ('uzbek', models.CharField(max_length=60, verbose_name="O'zbekcha")),
            ],
        ),
    ]
