import games

class Actions:
    def __init__(self, attributes, pet, pet_asleep):
        self.attributes = attributes
        self.pet = pet
        self.pet_asleep = pet_asleep
        self.owned_medicine = []

    def eat(self):
        fridge = [self.pet.favorite_food]
        while True:
            food_menu = int(input("""
    ==============================
        🍽️ FOOD MENU 🍽️       
    ==============================
        1 - Eat Food              
        2 - Buy Food             
        0 - Back                 
    ==============================
    """))
            if food_menu == 1:
                if not self.pet.asleep:
                    food_points = 0
                    if self.attributes.hunger == 100:
                        print(f"{self.pet.name} is too full to eat!")
                        break
                    print(f"\nFridge: {', '.join(fridge)}")
                    food_choice = input(f"Which food will {self.pet.name} eat? \n >> ").title()
                    if food_choice in fridge:
                        if food_choice == self.pet.favorite_food:
                            food_points = 15
                            fridge.remove(food_choice)
                        else: 
                            food_points = 5
                            fridge.remove(food_choice)
                        self.attributes.hunger += food_points
                        print(f"{self.pet.name} ate a {food_choice} and gained {food_points} hunger!")
                    else:
                        print(f"{self.pet.name} doesn't have that in the fridge!")
                else:
                    print(f"{self.pet.name} is sleeping!")
                    break
            elif food_menu == 2:
                fridge_menu = int(input("""
==============================
           BUY FOOD         
==============================
    1 - Apple (3 coins)       
    2 - Banana (3 coins)
    3 - Cheese Bread (3 coins)
    4 - Hot Dog (3 coins)
    0 - Back                  
==============================
"""))
                if fridge_menu == 1:
                    if "Apple" not in fridge:
                        if self.attributes.coins >= 3:
                            self.attributes.coins -= 3
                            fridge.append("Apple")
                        else:
                            print("Not enough coins!")
                    continue

                elif fridge_menu == 2:
                    if "Banana" not in fridge:
                        if self.attributes.coins >= 3:
                            self.attributes.coins -= 3
                            fridge.append("Banana")
                        else:
                            print("Not enough coins!")
                    continue

                elif fridge_menu == 3:
                    if "Cheese Bread" not in fridge:
                        if self.attributes.coins >= 3:
                            self.attributes.coins -= 3
                            fridge.append("Cheese Bread")
                        else:
                            print("Not enough coins!")
                    continue

                elif fridge_menu == 4:
                    if "Hot Dog" not in fridge:
                        if self.attributes.coins >= 3:
                            self.attributes.coins -= 3
                            fridge.append("Hot Dog")
                        else:
                            print("Not enough coins!")
                    continue

                elif fridge_menu == 0:
                    break
                else:
                    print("Invalid option!")
                    continue
            elif food_menu == 0:
                break        
    def sleep(self):
        while True:
            sleep_choice = int(input("""
==============================
         SLEEP MENU           
==============================
1 - Sleep                    
2 - Wake up                 
0 - Exit                    
==============================
"""))
            if sleep_choice == 1:
                if self.pet.asleep:
                    print(f"{self.pet.name} is already sleeping!")
                elif self.attributes.sleepiness == 100:
                    print(f"{self.pet.name} is not feeling tired.")
                else:
                    print(f"{self.pet.name} is now sleeping!")
                    self.attributes.sleepiness += 10
                    self.pet.asleep = True
                break
            elif sleep_choice == 2:
                if not self.pet.asleep:
                    print(f"{self.pet.name} is already awake!")
                else:
                    print(f"{self.pet.name} has woken up!")
                    self.pet.asleep = False
                break
            elif sleep_choice == 0:
                break
            else:
                print("Invalid option! Please choose between 0 and 2.")
                continue
            
    def play(self):
        if self.pet.asleep:
            print(f"{self.pet.name} is sleeping!")
            return
        else:
            confirmation = input("Do you want to play a Word Game? (Y/N)").upper()
            if confirmation == "Y":
                result = games.word_game()
                if result == "won":
                    self.attributes.coins += 10
            else:
                return

    def health(self):
        while True:
            health_menu = int(input("""
==============================
         HEALTH MENU          
==============================
1 - Buy medicine             
2 - Use medicine           
0 - Exit                    
==============================
"""))
            if health_menu == 1:
                medicine_menu = int(input("""
==============================
        BUY MEDICINE          
==============================
1 - Small Potion (5 coins)   
2 - Big Potion (10 coins)    
0 - Back                     
==============================
"""))
                if medicine_menu == 1:
                    if self.attributes.coins >= 5:
                        print("You bought a Small potion!")
                        self.attributes.coins -= 5
                        self.owned_medicine.append("Small potion")
                    else:
                        print("Not enough coins!")
                    break
                elif medicine_menu == 2:
                    if self.attributes.coins >= 10:
                        print("You bought a Big potion!")
                        self.attributes.coins -= 10
                        self.owned_medicine.append("Big potion")
                    else:
                        print("Not enough coins!")
                    break
            if health_menu == 2:
                if not self.pet.asleep:
                    print(f"\nOwned medicine: {', '.join(self.owned_medicine)}")
                    medicine_choice = input(f"Which medicine will {self.pet.name} have?\n>> ").capitalize()

                    potion_effects = {
                                    "Small potion": 5,
                                    "Big potion": 10
                                    }
                    
                    if medicine_choice in self.owned_medicine:
                            if self.attributes.health == 100:
                                print(f"{self.pet.name} is healthy!")
                            else:
                                effect = potion_effects[medicine_choice]
                                self.attributes.health += effect
                                print(f"{self.pet.name}'s health was increased by {effect}!")
                                self.owned_medicine.remove(medicine_choice)
                            break
                    else:
                        print("Invalid medicine choice or you don't have that medicine in stock!")
                else:
                    print(f"{self.pet.name} is sleeping!")
                    break

            if health_menu == 0:
                break

            else:
                print("Invalid option! Please choose between 0 and 2")
                continue