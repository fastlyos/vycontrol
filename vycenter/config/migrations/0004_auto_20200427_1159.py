# Generated by Django 2.0.3 on 2020-04-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20200426_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instance',
            name='id',
        ),
        migrations.AlterField(
            model_name='instance',
            name='hostname',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]