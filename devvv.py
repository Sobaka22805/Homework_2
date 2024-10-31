print("hello!")

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 15:
            self.hunger -= 15
            self.happiness += 10
            print(f"{self.name} поел! Уровень голода: {self.hunger}, уровень счастья: {self.happiness}")
        else:
            print(f"{self.name} не голоден сейчас.")

    def play(self):
        if self.energy > 10:
            self.happiness += 10
            self.energy -= 15
            print(f"{self.name} поиграл! Уровень счастья: {self.happiness}, уровень энергии: {self.energy}")
        else:
            print(f"{self.name} слишком устал, чтобы играть. Нужно отдохнуть!")

    def rest(self):
        if self.energy < 90:
            self.energy += 20
            self.hunger += 10
            print(f"{self.name} отдохнул! Уровень энергии: {self.energy}, уровень голода: {self.hunger}")
        else:
            print(f"{self.name} не хочет отдыхать, у него много энергии.")

    def status(self):
        print(f"Статус {self.name} ({self.species}):")
        print(f"Голод: {self.hunger}/100")
        print(f"Энергия: {self.energy}/100")
        print(f"Счастье: {self.happiness}/100")
        print()


my_pet = Pet("Мурзик", "кот")
my_pet.status()
my_pet.feed()
my_pet.play()
my_pet.rest()
my_pet.status()
