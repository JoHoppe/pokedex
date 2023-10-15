# Generated by Django 4.2.1 on 2023-10-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedexapp', '0001_initial'),
        ('trainercard', '0006_alter_trainercard_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokeTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='My first Team', max_length=15, unique=True)),
                ('pok_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_1', to='pokedexapp.pokemon')),
                ('pok_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_2', to='pokedexapp.pokemon')),
                ('pok_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_3', to='pokedexapp.pokemon')),
                ('pok_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_4', to='pokedexapp.pokemon')),
                ('pok_5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_5', to='pokedexapp.pokemon')),
                ('pok_6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pok_6', to='pokedexapp.pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='trainercard',
            name='poke_teams',
            field=models.ManyToManyField(to='trainercard.poketeam'),
        ),
    ]
