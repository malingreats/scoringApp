# Generated by Django 3.0.8 on 2021-02-13 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='head',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='users.Manager'),
        ),
        migrations.AddField(
            model_name='loanofficer',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Manager', verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='loanofficer',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='users.AccountUser', verbose_name='Officer Account'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='users.AccountUser', verbose_name='Manager Account'),
        ),
    ]
