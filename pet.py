class VirtualPet:
    def __init__(self, name, species, favorite_food):
        self.name = name
        self.species = species
        self.favorite_food = favorite_food
        self.asleep = False

    def play(self):
        print(f"{self.name} is playing!")

    def status(self):

        if self.hunger < 50:
            pet_status = "Hungry"
            print(f"{self.name} wants a {self.favorite_food.lower()}")
        elif self.health < 50:
            pet_status = "Sick"
            print(f"{self.name} needs medicine.")
        elif self.sleepiness < 50:
            pet_status = "Tired"
            print(f"{self.name} needs to sleep.")
        elif self.fun < 50:
            pet_status = "Fun"
            print(f"{self.name} wants to play.")
        print(f"Pet status: {pet_status}")
        