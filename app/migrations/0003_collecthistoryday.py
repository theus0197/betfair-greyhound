# Generated by Django 4.2.3 on 2023-08-29 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_races_race_greyhound'),
    ]

    operations = [
        migrations.CreateModel(
            name='collectHistoryDay',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('last_refresh', models.DateField()),
                ('len_history', models.IntegerField()),
                ('greyhound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.greyhound')),
            ],
            options={
                'verbose_name': 'collectHistoryDay',
                'verbose_name_plural': 'collectHistoryDay',
            },
        ),
    ]
