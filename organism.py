# organism.py

class Organism:
    """Базовый класс для любого организма в экосистеме."""

    def __init__(self, name: str, energy: float):
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float):
        """Увеличивает энергию организма при поедании пищи."""
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Возвращает True, если организм жив."""
        return self.energy > 0
