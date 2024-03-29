# Generated by Django 5.0.2 on 2024-03-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='btn_id',
            field=models.CharField(max_length=100, null=True, verbose_name='Button ID'),
        ),
        migrations.AlterField(
            model_name='target',
            name='form_id',
            field=models.CharField(max_length=100, null=True, verbose_name='Form ID'),
        ),
        migrations.AlterField(
            model_name='target',
            name='password_id_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Password Filed ID Or Name'),
        ),
        migrations.AlterField(
            model_name='target',
            name='redirect_url',
            field=models.CharField(max_length=1000, null=True, verbose_name='Redirect Url'),
        ),
        migrations.AlterField(
            model_name='target',
            name='username_id_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Username Field ID Or Name'),
        ),
    ]
