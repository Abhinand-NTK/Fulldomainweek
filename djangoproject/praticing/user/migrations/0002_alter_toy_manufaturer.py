# Generated by Django 4.2.7 on 2023-12-02 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='Manufaturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.manufaturer'),
        ),
    ]
