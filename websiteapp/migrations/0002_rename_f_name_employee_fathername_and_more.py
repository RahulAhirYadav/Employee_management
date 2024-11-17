# Generated by Django 5.0.3 on 2024-03-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='f_name',
            new_name='fathername',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='m_name',
            new_name='mothername',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empattendence',
            name='date',
            field=models.DateField(),
        ),
    ]