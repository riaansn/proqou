#! /usr/bin/python3
# -*- coding: utf-8 -*-


import argparse
from fruit.fruit_factory import FruitFactory


def get_parser():
    parser = argparse.ArgumentParser(
        description="Calculating nutrition for smoothy recipies..."
    )
    parser.add_argument(
        "-n", "--name", type=str, metavar="", required=True, help="Recipe name"
    )
    parser.add_argument(
        "-f",
        "--fruit",
        type=str,
        action="append",
        metavar="",
        required=True,
        help="Fruit type and weight.",
        nargs=2,
    )
    return parser.parse_args()


# Separating printing responsibility...
def print_result(fruits, vitamin_c, weight, pecentage, flavour):
    print(f"List of Fruits: {fruits}")
    print(f"Total vitamin C: {vitamin_c}")
    print(f"Total weight: {weight}g")
    print(f"Total citrus: {pecentage}%")
    print(f"Strongest flavours in your smoothy: {flavour}")


# This function has way to many responsibilities... Creating a class or two would be a better way to control responsibilities...
def recipe(ingredients):

    # Control variables...
    fruits = []
    top_flavours = ["", ""]
    flavour_1 = 0
    flavour_2 = 0
    total_vitamin_c = 0
    total_weight = 0
    total_citrus = 0

    # Helper functions since this is not a class...
    def calculate_citrus_percentage(total, length):
        return float("{0:.1f}".format((total / length) * 100))

    def get_fruit(item):
        fruit_factory = FruitFactory()
        fruit = fruit_factory.fruit_factory(item[0], int(item[1]))
        return fruit.fruit_information()

    try:

        for item in ingredients:
            fruit = get_fruit(item)

            if fruit["citrus"]:
                total_citrus += 1

            total_weight += fruit["weight"]
            total_vitamin_c += fruit["vitamin_c"]
            fruits.append(fruit["name"])
            flavour = fruit["flavour_strength"]

            # This whole section should be a separate function...
            if flavour_1 < flavour:
                top_flavours[0] = fruit["name"]
                flavour_1 = flavour
            elif flavour_2 < flavour:
                top_flavours[1] = fruit["name"]
                flavour_2 = flavour
            else:
                flavour = 0

        print_result(
            fruits,
            total_vitamin_c,
            total_weight,
            calculate_citrus_percentage(total_citrus, len(ingredients)),
            top_flavours,
        )
    except Exception as e:
        print(e)


def main(recipe_name, ingredients):
    print(f"{recipe_name} smoothy nutritional information is as follows:")
    recipe(ingredients)


if __name__ == "__main__":
    args = get_parser()
    main(args.name, args.fruit)
