# Generated by Django 3.0.2 on 2022-09-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Senior One', 'Senior One'), ('Seinor 2', 'Senior 2'), ('Upper Primary', 'Upper Primary')], max_length=200, null=True),
        ),
    ]
