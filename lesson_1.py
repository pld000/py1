#--------------------------------------------------1.1--------------------------------------------------
# YandexGo
# ------------------------
# Car
#   Свойства:
#     - марка машины
#     - гос номер
#     - цвет
#     - класс комфорта
# ------------------------
# Driver
#   Свойства:
#     - имя
#     - машина: Car
#     - рейтинг
#   Методы:
#     - оставить отзыв о пассажире
#     - принять заказ
#     - отклонить заказ
#     - завершить заказ
# ------------------------
# Passenger
#   Свойства:
#     - имя
#     - способ оплаты
#     - рейтинг
#   Методы:
#     - ввести адрес
#     - разместить заказ
#     - отменить заказ
#     - оставить отзыв о водителе
# ------------------------
# Route
#   Свойства:
#     - начальный пункт
#     - конечный пункт
#     - время пути
#     - стоимость поездки
#   Методы:
#     - построить маршрут
#     - расчитать стоимость маршрута
#     - перестроить маршрут
# ------------------------
# Payment
#   Свойства:
#     - метод оплаты
#     - номер заказа
#   Методы:
#     - совершить оплату



# Wildberies
# ------------------------
# Customer
#   Свойства:
#     - имя
#     - лист ожиданий
#     - выполненные заказы
# ------------------------
# Shop
#   Свойства:
#     - список товаров
#     - юридическая информация
#     - рейтинг
#   Методы:
#     - добавить товар
#     - убрать товар
#     - обновить статус заказа
# ------------------------
# Order
#   Свойства:
#     - список товаров
#     - магазины: Shop[]
#     - адрес доставки
#     - статус заказа
#   Методы:
#     - получить информацию о заказе
# ------------------------
# Payment
#   Свойства:
#     - метод оплаты
#     - номер заказа
#   Методы:
#     - совершить оплату

#--------------------------------------------------1.2--------------------------------------------------
class Dwarf:
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.skills = []
        self.age = 0
        self.gender = ""
        self.mood = ""
        self.equipped_weapon = None

    def __str__(self):
        weapon_info = "без оружия" if not self.equipped_weapon else f"с {self.equipped_weapon.name}"
        return f"Дварф {self.name} ({self.profession}), {self.age} лет, {weapon_info}"

class Weapon:
    def __init__(self):
        self.name = ""
        self.material = ""
        self.type = ""
        self.damage = ""
        self.quality = ""
        self.weight = 0.0
        self.is_artifact = False

    def __str__(self):
        artifact_status = " (АРТЕФАКТ)" if self.is_artifact else ""
        return f"{self.name} [{self.material} {self.type}], урон: {self.damage}{artifact_status}"

class Animal:
    def __init__(self):
        self.species = ""
        self.is_tame = False
        self.is_domestic = False
        self.size = ""
        self.diet = ""
        self.habitat = ""
        self.is_dangerous = False

    def __str__(self):
        tame_status = "прирученное" if self.is_tame else "дикое"
        danger_status = "опасное" if self.is_dangerous else "безопасное"
        return f"{self.species} ({tame_status}, {danger_status}, {self.diet})"


print("=== ДВАРФЫ ===")

dwarf1 = Dwarf()
dwarf1.name = "Урист Маккрейт"
dwarf1.profession = "шахтер"
dwarf1.skills = ["горное дело", "ношение тяжестей", "упрямство"]
dwarf1.age = 45
dwarf1.gender = "мужской"
dwarf1.mood = "задумчивый"

dwarf2 = Dwarf()
dwarf2.name = "Анита ЖелезнаяКузня"
dwarf2.profession = "воин"
dwarf2.skills = ["метание", "рукопашный бой", "стратегия"]
dwarf2.age = 32
dwarf2.gender = "женский"
dwarf2.mood = "воинственное"

print(dwarf1)
print(dwarf2)

print("\n=== ОРУЖИЕ ===")

weapon1 = Weapon()
weapon1.name = "Стальной топор Убийца"
weapon1.material = "сталь"
weapon1.type = "топор"
weapon1.damage = "рубящий"
weapon1.quality = "мастерское"
weapon1.weight = 3.5
weapon1.is_artifact = False

weapon2 = Weapon()
weapon2.name = "Пламенный Коготь"
weapon2.material = "обсидиан"
weapon2.type = "меч"
weapon2.damage = "колющий/режущий"
weapon2.quality = "легендарное"
weapon2.weight = 2.1
weapon2.is_artifact = True

print(weapon1)
print(weapon2)

print("\n=== ЖИВОТНЫЕ ===")

animal1 = Animal()
animal1.species = "гигантский ёж"
animal1.is_tame = True
animal1.is_domestic = True
animal1.size = "средний"
animal1.diet = "насекомоядное"
animal1.habitat = "подземелья"
animal1.is_dangerous = False

animal2 = Animal()
animal2.species = "пещерный крокодил"
animal2.is_tame = False
animal2.is_domestic = False
animal2.size = "большой"
animal2.diet = "плотоядное"
animal2.habitat = "подземные озера"
animal2.is_dangerous = True

print(animal1)
print(animal2)

print("\n=== СВЯЗИ МЕЖДУ ОБЪЕКТАМИ ===")
dwarf2.equipped_weapon = weapon2
print(f"{dwarf2.name} теперь вооружен: {dwarf2.equipped_weapon}")

dwarf3 = Dwarf()
dwarf3.name = "Борис Камнедел"
dwarf3.profession = "оружейник"
dwarf3.age = 67
dwarf3.equipped_weapon = weapon1
print(dwarf3)

#--------------------------------------------------1.3--------------------------------------------------
def change_mood(dwarf, mood):
    dwarf.mood = mood

print(f"НАСТРОЕНИЕ ДВАРФА 1 ДО БРАТА: {dwarf1.mood}")
dwarf1_brother = dwarf1
change_mood(dwarf1_brother, 'весельчак')

print(f"НАСТРОЕНИЕ БРАТА ДВАРФА 1: {dwarf1.mood}")
print(f"НАСТРОЕНИЕ ДВАРФА 1 ПОСЛЕ БРАТА: {dwarf1.mood}")
