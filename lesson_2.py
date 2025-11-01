class Dwarf:
    def __init__(self, name, hp, drink, work_id):
        self.name = name
        self.HP = hp
        self.drink = drink
        self.work_id = work_id

    def assign_work(self, work_id):
        self.work_id = work_id

    def get_drink(self, drink):
        self.drink = drink

    def get_status(self):
        if self.drink > 50:
            return f"{self.name} is drunk"
        elif self.work_id:
            return f"{self.work_id}"
        else:
            return f"{self.name} is not busy"


class Weapon:
    def __init__(self, name, kind, damage, range):
        self.name = name
        self.kind = kind
        self.damage = damage
        self.range = range

    def upgrade(self, damage, range):
        self.damage = damage
        self.range = range

    def calc_damage(self, distance):
        if distance > self.range:
            return 0
        elif distance > self.range / 2:
            return self.damage / 2
        return self.damage

    def get_characteristics(self):
        return f"Damage: {self.damage}\nRange: {self.range}"


class Animal:
    def __init__(self, name, kind, mass, speed):
        self.name = name
        self.kind = kind
        self.mass = mass
        self.speed = speed

    def run(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def sleep(self):
        self.stop()
        self.mass += 0.1

    def eat(self, mass):
        self.mass += mass

    def get_status(self):
        return f"Name {self.name}\nKind {self.kind}\nSpeed {self.speed}\nMass {self.mass}"



gimli = Dwarf(name="Gimli", hp=150, drink=10, work_id=0)

print("--- Dwarf Status ---")
print(f"Initial Status: {gimli.get_status()}")

gimli.assign_work(work_id=1)
print(f"Status after work assignment (1): {gimli.get_status()}")

gimli.get_drink(drink=60)
print(f"Status after drinking (60): {gimli.get_status()}")


donkey = Animal(name="Donkey", kind="Beast of Burden", mass=200, speed=5)

print("\n--- Animal Status ---")
print("Initial Status:")
print(donkey.get_status())

donkey.run(speed=15)
donkey.eat(mass=5.5)
donkey.sleep()

print("\nFinal Status:")
print(donkey.get_status())


axe = Weapon(name="Axe", kind="Melee", damage=100, range=3)

print("\n--- Weapon Characteristics ---")
print("Initial:")
print(axe.get_characteristics())

axe.upgrade(damage=150, range=4)
print("\nAfter Upgrade:")
print(axe.get_characteristics())

print(f"\nDamage at distance 1 (close): {axe.calc_damage(1)}")
print(f"Damage at distance 3 (medium): {axe.calc_damage(3)}")
print(f"Damage at distance 5 (far): {axe.calc_damage(5)}")