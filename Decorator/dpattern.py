from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

# Decorator
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Decorator: Milk
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0

# Concrete Decorator: Sugar
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

# Usage
simple_coffee = SimpleCoffee()
print("Cost of simple coffee:", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print("Cost of milk coffee:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of sugar and milk coffee:", sugar_milk_coffee.cost())
