# Generated by Django 5.0.4 on 2024-04-19 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('column', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('priority', models.IntegerField()),
                ('column_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='column.column')),
            ],
            options={
                'db_table': 'Task',
            },
        ),
    ]