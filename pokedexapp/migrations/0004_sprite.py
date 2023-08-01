# Generated by Django 4.2.1 on 2023-07-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedexapp', '0003_remove_pokemon_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField()),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pokedexapp.pokemon')),
            ],
        ),
    ]
