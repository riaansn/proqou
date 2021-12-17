from abc import ABCMeta, abstractstaticmethod


class IFruit(metaclass=ABCMeta):
    """Abstract Fruit class - Fruit interface."""

    def __init__(self):
        super().__init__()

    @abstractstaticmethod
    def fruit_information(self):
        """Interface method to get fruit."""

    @abstractstaticmethod
    def calculate_flavour_strength(self):
        """Interface method to get fruit."""

    @abstractstaticmethod
    def calculate_vitamin_c(self):
        """Interface method to get fruit."""
