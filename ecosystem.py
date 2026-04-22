# ecosystem.py
from population import Population
from typing import List

class Ecosystem:
    """Экосистема, объединяющая разные популяции."""

    def __init__(self, name: str):
        self.name = name
        self.populations: List[Population] = []

    def add_population(self, population: Population):
        self.populations.append(population)

    def simulate_day(self, food_per_alive: float = 5):
        """Один день симуляции: каждый живой организм ест."""
        for pop in self.populations:
            print(f"\n--- {pop.species_name} ---")
            for org in pop.members:
                if org.is_alive():
                    org.eat(food_per_alive)
                else:
                    print(f"{org.name} мёртв.")
