from .fruits import Banana, Apple, Strawberry, Orange, Lemon


class FruitFactory:
    """Fruit Factory class

    Raises:
        AssertionError: Ingredient not available.

    Returns:
        IFruit: as fruit subclass.
    """

    @staticmethod
    def fruit_factory(fruit_name, grams):
        try:
            if fruit_name.lower() == "banana":
                return Banana(grams)
            elif fruit_name.lower() == "orange":
                return Orange(grams)
            elif fruit_name.lower() == "apple":
                return Apple(grams)
            elif fruit_name.lower() == "strawberry":
                return Strawberry(grams)
            elif fruit_name.lower() == "lemon":
                return Lemon(grams)
            else:
                raise AssertionError(
                    f"Ingredient: {fruit_name} is not available for your smoothy."
                )
        except AssertionError as e:
            print(e)
