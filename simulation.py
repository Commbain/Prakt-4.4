# simulation.py
from organism import Organism
from population import Population
from ecosystem import Ecosystem

def run_simulation(days: int = 3):
    """Запускает пошаговую симуляцию экосистемы."""
    print("=== СИМУЛЯЦИЯ ЭКОСИСТЕМЫ ===\n")

    rabbit1 = Organism("Заяц_1", 20)
    rabbit2 = Organism("Заяц_2", 15)
    fox = Organism("Лиса", 30)

    rabbits_pop = Population("Зайцы")
    rabbits_pop.add_member(rabbit1)
    rabbits_pop.add_member(rabbit2)

    foxes_pop = Population("Лисы")
    foxes_pop.add_member(fox)

    forest = Ecosystem("Лес")
    forest.add_population(rabbits_pop)
    forest.add_population(foxes_pop)

    for day in range(1, days + 1):
        print(f"\nДень {day}")
        forest.simulate_day(food_per_alive=10)

    print("\n=== ИТОГИ ===")
    for pop in forest.populations:
        print(f"{pop.species_name}: живых {pop.alive_count()}, "
              f"общая энергия {pop.total_energy():.1f}")

if __name__ == "__main__":
    run_simulation()
