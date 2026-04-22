# tests.py
from organism import Organism
from population import Population
from ecosystem import Ecosystem

def test_organism_alive():
    o = Organism("Тест", 10)
    assert o.is_alive() is True
    o.eat(-20)
    assert o.is_alive() is False
    print("✅ test_organism_alive пройден")

def test_population_energy():
    p = Population("Тест_pop")
    p.add_member(Organism("A", 10))
    p.add_member(Organism("B", 20))
    assert p.total_energy() == 30
    print("✅ test_population_energy пройден")

def test_ecosystem_simulation():
    eco = Ecosystem("Тест_эко")
    pop = Population("Рыбы")
    pop.add_member(Organism("Немо", 5))
    eco.add_population(pop)
    eco.simulate_day(food_per_alive=3)
    assert pop.members[0].energy == 8
    print("✅ test_ecosystem_simulation пройден")

if __name__ == "__main__":
    test_organism_alive()
    test_population_energy()
    test_ecosystem_simulation()
    print("\n🎉 Все тесты пройдены!")
