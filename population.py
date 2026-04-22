# population.py
from organism import Organism
from typing import List

class Population:
    """Управляет группой однотипных организмов."""

    def __init__(self, species_name: str):
        self.species_name = species_name
        self.members: List[Organism] = []

    def add_member(self, organism: Organism):
        self.members.append(organism)

    def total_energy(self) -> float:
        """Суммарная энергия популяции."""
        return sum(m.energy for m in self.members)

    def alive_count(self) -> int:
        """Количество живых организмов."""
        return sum(1 for m in self.members if m.is_alive())
