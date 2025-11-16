from typing import List


class Dwarf:
    def __init__(self, name, hp, drink, work_id):
        self.__name = name
        self.__HP = hp
        self.__drink = drink
        self.__work_id = work_id
        self.__equipped_weapon = None

    def assign_work(self, work_id):
        self.__work_id = work_id

    def get_drink(self, drink):
        self.__drink = drink

    def equip_weapon(self, weapon):
        self.__equipped_weapon = weapon

    def apply_weapon(self, distance):
        return self.__equipped_weapon.calc_damage(distance)

    def get_status(self):
        if self.__drink > 50:
            return f"{self.__name} is drunk"
        elif self.__work_id:
            return f"{self.__work_id}"
        else:
            return f"{self.__name} is not busy"
            

class Weapon:
    def __init__(self, name, kind, damage, range):
        self.__name = name
        self.__kind = kind
        self.__damage = damage
        self.__range = range

    def upgrade(self, damage, range):
        self.__damage = damage
        self.__range = range

    def calc_damage(self, distance):
        if distance > self.__range:
            return 0
        elif distance > self.__range / 2:
            return self.__damage / 2
        return self.__damage

    def get_characteristics(self):
        return f"Damage: {self.__damage}\nRange: {self.__range}"


class Sword(Weapon):
    def __init__(self, name, damage, range, blade_length):
        super().__init__(name, "melee", damage, range)
        self.__blade_length = blade_length

    def sharpen(self):
        print(f"The {self.__blade_length} cm blade has been sharpened — damage increased!")
        self.upgrade(damage=self.calc_damage(0) + 10, range=self._Weapon__range)

    def swing(self):
        print("You make a powerful sword swing!")


class Bow(Weapon):
    def __init__(self, name, damage, range, arrow_count):
        super().__init__(name, "ranged", damage, range)
        self.__arrow_count = arrow_count

    def shoot(self, distance):
        if self.__arrow_count <= 0:
            print("No arrows left!")
            return 0
        self.__arrow_count -= 1
        dmg = self.calc_damage(distance)
        print(f"Shot at {distance} m: dealt {dmg} damage.")
        return dmg

    def refill_arrows(self, count):
        self.__arrow_count += count
        print(f"Quiver refilled. Arrows available: {self.__arrow_count}")


class Animal:
    def __init__(self, name, kind, mass, speed):
        self.__name = name
        self.__kind = kind
        self.__mass = mass
        self.__speed = speed

    def run(self, speed):
        self.__speed = speed

    def stop(self):
        self.__speed = 0

    def sleep(self):
        self.stop()
        self.__mass += 0.1

    def eat(self, mass):
        self.__mass += mass

    def get_status(self):
        return f"Name: {self.__name}\nKind: {self.__kind}\nSpeed: {self.__speed}\nMass: {self.__mass}"


class Dog(Animal):
    def __init__(self, name, mass, speed, breed):
        super().__init__(name, "dog", mass, speed)
        self.__breed = breed

    def bark(self):
        print(f"The {self.__breed} barks loudly!")

    def fetch(self, item):
        print(f"The dog fetched the {item}!")


class Bird(Animal):
    def __init__(self, name, mass, speed, wingspan):
        super().__init__(name, "bird", mass, speed)
        self.__wingspan = wingspan

    def fly(self, altitude):
        print(f"The bird flies up to {altitude} meters!")

    def sing(self):
        print("The bird sings a beautiful melody.")


#------------------------------ Task 4.1 ------------------------------
d = Dwarf('Villi', 100, 0, 2)
s = Sword('Flamberg', 30, 200, 10)

d.equip_weapon(s)
res = d.apply_weapon(60)
print(res)

#------------------------------ Task 4.2 ------------------------------
# Параметрический полиморфизм - поведение функции будет одинаковым для разных подтипов
# Подтиповой полиморфизм - поведение вызываемого метода зависит от его реализации в конктетном типе
#------------------------------ Task 4.3 ------------------------------

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def do_something_with_animal(animal: Animal):
    animal.foo()
    
def fill_animals(animals: List[Animal]):
    animals = []
    for i in range(500):
        if i % 2 == 0:
            animals.append(Bird())
        else:
            animals.append(Cat())
    return animals


animals_list = fill_animals([])

for animal in animals_list:
    animal.foo()

# Такой вывод получился в результате полиморфизма подтипов