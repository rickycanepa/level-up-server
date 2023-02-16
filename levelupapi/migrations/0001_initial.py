# Generated by Django 4.1.7 on 2023-02-16 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_event', models.DateField()),
                ('start_time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('min_player', models.IntegerField()),
                ('max_player', models.IntegerField()),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='levelupapi.gametype')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='EventGamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='levelupapi.event')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attendee', to='levelupapi.gamer')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(through='levelupapi.EventGamer', to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='game_events', to='levelupapi.game'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_host', to='levelupapi.gamer'),
        ),
    ]