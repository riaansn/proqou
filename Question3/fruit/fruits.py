from .base_fruit import IFruit


class Banana(IFruit):
    def __init__(self, grams):
        """Banana nutition values per 100g

        Args:
            grams int: Banana weight.
        """
        self.name = "banana"
        self.flavour_strength = 40
        self.citrus = False
        self.vitamin_c = 85
        self.grams = grams

    def fruit_information(self):
        """Banana nutritional information."""
        return {
            "name": self.name,
            "flavour_strength": self.calculate_flavour_strength(),
            "citrus": self.citrus,
            "vitamin_c": self.calculate_vitamin_c(),
            "weight": self.grams,
        }

    def calculate_flavour_strength(self):
        return self.flavour_strength * (self.grams / 100)

    def calculate_vitamin_c(self):
        return self.vitamin_c * (self.grams / 100)


class Orange(IFruit):
    def __init__(self, grams):
        """Orange nutition values per 100g

        Args:
            grams int: Orange weight.
        """
        self.name = "orange"
        self.flavour_strength = 70
        self.citrus = True
        self.vitamin_c = 150
        self.grams = grams

    def fruit_information(self):
        """Orange nutritional information."""
        return {
            "name": self.name,
            "flavour_strength": self.calculate_flavour_strength(),
            "citrus": self.citrus,
            "vitamin_c": self.calculate_vitamin_c(),
            "weight": self.grams,
        }

    def calculate_flavour_strength(self):
        return self.flavour_strength * (self.grams / 100)

    def calculate_vitamin_c(self):
        return self.vitamin_c * (self.grams / 100)


class Apple(IFruit):
    def __init__(self, grams):
        """Apple nutition values per 100g

        Args:
            grams int: Apple weight.
        """
        self.name = "apple"
        self.flavour_strength = 50
        self.citrus = False
        self.vitamin_c = 75
        self.grams = grams

    def fruit_information(self):
        """Apple nutritional information."""
        return {
            "name": self.name,
            "flavour_strength": self.calculate_flavour_strength(),
            "citrus": self.citrus,
            "vitamin_c": self.calculate_vitamin_c(),
            "weight": self.grams,
        }

    def calculate_flavour_strength(self):
        return self.flavour_strength * (self.grams / 100)

    def calculate_vitamin_c(self):
        return self.vitamin_c * (self.grams / 100)


class Strawberry(IFruit):
    def __init__(self, grams):
        """Strawberry nutition values per 100g

        Args:
            grams int: Strawberry weight.
        """
        self.name = "strawberry"
        self.flavour_strength = 50
        self.citrus = False
        self.vitamin_c = 90
        self.grams = grams

    def fruit_information(self):
        """Strawberry nutritional information."""
        return {
            "name": self.name,
            "flavour_strength": self.calculate_flavour_strength(),
            "citrus": self.citrus,
            "vitamin_c": self.calculate_vitamin_c(),
            "weight": self.grams,
        }

    def calculate_flavour_strength(self):
        return self.flavour_strength * (self.grams / 100)

    def calculate_vitamin_c(self):
        return self.vitamin_c * (self.grams / 100)


class Lemon(IFruit):
    def __init__(self, grams):
        """Lemon nutition values per 100g

        Args:
            grams int: Lemon weight.
        """
        self.name = "lemon"
        self.flavour_strength = 90
        self.citrus = True
        self.vitamin_c = 130
        self.grams = grams

    def fruit_information(self):
        """Lemon nutritional information."""
        return {
            "name": self.name,
            "flavour_strength": self.calculate_flavour_strength(),
            "citrus": self.citrus,
            "vitamin_c": self.calculate_vitamin_c(),
            "weight": self.grams,
        }

    def calculate_flavour_strength(self):
        return self.flavour_strength * (self.grams / 100)

    def calculate_vitamin_c(self):
        return self.vitamin_c * (self.grams / 100)
