class Pets:

    def __init__(self, name, feed, voice, weight):
        self.name = name
        self.feed = feed
        self.voice = voice
        self.weight = weight


    def describe_pets(self):
        greeting = "Привет! Меня зовут" + " " + self.name + "." + " Моя еда это " + self.feed + " и я говорю " + self.voice + ", " + "а вешу " + str(self.weight) + " кг."
        return greeting


class Cow(Pets):
    milk = 0

    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

    def milking(self, milk):
        self.milk += milk
        return "Я даю " + str(milk) + " литров молока."


pet_cow = Cow("Манька", "сено и трава", "Муууу", 450)
print(pet_cow.describe_pets())
print(pet_cow.milking(10))


class Geese(Pets):
    eggs = 0

    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

    def picking_eggs(self, eggs):
        self.eggs += eggs
        return "Я даю " + str(eggs) + " яиц."

pet_goose = Geese("Серый", "зелень", "Кря-Кря", 3)
pet_another_goose = Geese("Белый", "зелень", "Кря-Кря", 2)
# print(pet_goose.describe_pets())
# print(pet_another_goose.describe_pets())


class Sheeps(Pets):
    wool= 0

    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

    def picking_wool(self, wool):
        self.wool += wool
        return "Я даю " + str(wool) + " кг шерсти."

pet_sheep = Sheeps("Барашек", "сено и трава", "Беее", 80)
pet_another_sheep = Sheeps("Кудрявый", "сено и трава", "Беее", 120)
# print(pet_sheep.describe_pets())
# print(pet_another_sheep.describe_pets())


class Goats(Cow):

    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

pet_goat = Goats("Рога", "сено и трава", "Меее", 20)
pet_another_goat = Goats("Копыта", "сено и трава", "Меее", 80)
# print(pet_goat.describe_pets())
# print(pet_another_goat.describe_pets())
# print(pet_goat.milking(2))


class Chickens(Geese):


    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

pet_chicken = Chickens("Ко-ко", "зерно", "Коо-Ко-Ко-Ко", 3)
pet_another_chicken = Chickens("Кукареку", "зерно", "Кукаре-Ку", 4)
# print(pet_chicken.describe_pets())
# print(pet_another_chicken.describe_pets())

class Duck(Geese):


    def __init__(self, name, feed, voice, weight):
        super().__init__(name, feed, voice, weight)

pet_duck = Duck("Кряква", "зерно", "Кря-Кря", 1)
# print(pet_duck.describe_pets())


def sum_weight_name():

    t = {
        pet_cow.name: pet_cow.weight,
        pet_duck.name: pet_duck.weight,
        pet_chicken.name: pet_chicken.weight,
        pet_another_chicken.name: pet_another_chicken.weight,
        pet_another_goat.name: pet_another_goat.weight,
        pet_goat.name: pet_goat.weight,
        pet_sheep.name: pet_sheep.weight,
        pet_another_sheep.name: pet_another_sheep.weight,
        pet_goose.name: pet_goose.weight,
        pet_another_goose.name: pet_another_goose.weight
    }
    v = list(t.values())
    k = list(t.keys())

    return sum(v), k[v.index(max(v))]

print(sum_weight_name())