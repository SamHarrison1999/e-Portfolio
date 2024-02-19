def print_nested_dictionary_keys_and_values(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print_nested_dictionary_keys_and_values(value)
        else:
            print(f'{key} : {value}')


def nested_dictionary_values(dictionary):
    for values in dictionary.values():
        if isinstance(values, dict):
            yield from nested_dictionary_values(values)
        else:
            yield values


def get_keys(dictionary, keys=None):
    keys = keys or []
    if isinstance(dictionary, dict):
        keys += dictionary.keys()
        [get_keys(x, keys) for x in dictionary.values()]
    elif isinstance(dictionary, list):
        [get_keys(x, keys) for x in dictionary]
    return list(set(keys))


vehicles = {
    "car1": {
        "make": "Telsa",
        "model": "Model 3",
        "year": 2024,
        "engine": {
            "transmission": "Automatic",
            "horse power": 250
        }
    },
    "car2": {
        "make": "Ford",
        "model": "GT",
        "year": 2024,
        "engine": {
            "transmission": "Manual",
            "horse power": 400
        }
    },
    "car3": {
        "make": "Toyota",
        "model": "Yaris",
        "year": 2024,
        "engine": {
            "transmission": "Hybrid",
            "horse power": 150
        }
    }
}

if __name__ == '__main__':
    print_nested_dictionary_keys_and_values(vehicles)
    print(list(nested_dictionary_values(vehicles)))
    print(get_keys(vehicles))
