# Generated by Django 2.1.2 on 2018-11-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrcPassBreaker', '0004_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
