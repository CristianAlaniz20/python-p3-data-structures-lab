spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_name_list = [food["name"] for food in spicy_foods if food.get("name")]
    return food_name_list

def get_spiciest_foods(spicy_foods):
    list_of_spicy_foods_dicts = [food for food in spicy_foods if food.get("heat_level") > 5]
    return list_of_spicy_foods_dicts

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    dict_by_cuisine = [food for food in spicy_foods if food.get("cuisine") == cuisine]
    if dict_by_cuisine:
        return dict_by_cuisine[0]
    else:
        return None

def print_spiciest_foods(spicy_foods):
    food_list_with_spice_over_five = get_spiciest_foods(spicy_foods)
    print_spicy_foods(food_list_with_spice_over_five)
    

def get_average_heat_level(spicy_foods):
    heat_level_total = 0
    number_of_elements = 0
    for food in spicy_foods:
        heat_level_total += food.get("heat_level")
        number_of_elements += 1
    average_heat_level = heat_level_total / number_of_elements
    return average_heat_level
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
