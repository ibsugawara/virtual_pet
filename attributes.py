class Attributes:
    def __init__(self, health, hunger, fun, sleepiness, coins, pet):
        self.health = health
        self.hunger = hunger
        self.sleepiness = sleepiness
        self.fun = fun
        self.coins = coins
        self.pet = pet

    def show_status(self):
        print(f"Name: {self.pet.name}\nSpecies: {self.pet.species}\nFavorite Food: {self.pet.favorite_food}\n")
        status_list = []
        if self.health < 50:
            status_list.append("sick")
        if self.hunger < 50:
            status_list.append("hungry")
        if self.fun < 50:
            status_list.append("bored")
        if self.sleepiness < 50:
            status_list.append("tired")

        if not status_list:
            status = "feeling good"
        elif len(status_list) == 1:
            status = status_list[0]
        elif len(status_list) == 2:
            status = status_list[0] + " and " + status_list[1]
        elif len(status_list) == 3:
            status = status_list[0] + ", " + status_list[1] + " and " + status_list[2]
        elif len(status_list) == 4:
            status = status_list[0] + ", " + status_list[1] + " and " + status_list[2] + " and " + status_list[3]

        print(f"{self.pet.name} is {status}")
        print(f"""Health: {self.health}
Hunger: {self.hunger}
Fun: {self.fun}
Sleep: {self.sleepiness}
Coins: {self.coins}""")
        
    def check_game_over(self):
        if self.health <= 0:
            print("Your pet got too sick...\nGAME OVER")
            exit()
        if self.hunger <= 0:
            print("Your pet starved...\nGAME OVER")
            exit()
        if self.sleepiness <= 0:
            print("Your pet got too tired...\nGAME OVER")
            exit()