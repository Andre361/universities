# Generated by Django 4.0.4 on 2022-05-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_university_state_province'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name_plural': 'Universities'},
        ),
        migrations.AlterField(
            model_name='university',
            name='state_province',
            field=models.TextField(null=True),
        ),
    ]