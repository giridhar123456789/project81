# Generated by Django 4.2.2 on 2023-06-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=10)),
                ('sclass', models.IntegerField(max_length=10)),
                ('sjd', models.DateField()),
                ('scd', models.DateField()),
            ],
        ),
    ]