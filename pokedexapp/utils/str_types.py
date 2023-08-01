def get_str_types(pokemon_types):
    type_mapping = {
        '1': 'normal',
        '2': 'fighting',
        '3': 'flying',
        '4': 'poison',
        '5': 'ground',
        '6': 'rock',
        '7': 'bug',
        '8': 'ghost',
        '9': 'steel',
        '10': 'fire',
        '11': 'water',
        '12': 'grass',
        '13': 'electric',
        '14': 'psychic',
        '15': 'ice',
        '16': 'dragon',
        '17': 'dark',
        '18': 'fairy',
    }

    type_names = [type_mapping.get(t_id, None) for t_id in pokemon_types]
    return [t_name for t_name in type_names if t_name is not None]
