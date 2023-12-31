# Generated by Django 4.2.1 on 2023-07-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_id_alter_measurement_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
