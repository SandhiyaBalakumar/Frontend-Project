# Generated by Django 5.0.4 on 2024-05-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_delete_signin'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]
