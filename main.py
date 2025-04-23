from pet import VirtualPet
from attributes import Attributes
from actions import Actions

def create_pet():
    species = ["Bat", "Giraffe", "Monkey", "Parrot", "Cat", "Dog"]
    foods = ["Banana", "Apple", "Cheese Bread", "Hot Dog"]

    name = input("What is your pet's name?\n>> ")

    while True:
        species_input = input(f"What is their species?\n{', '.join(species)}\n>> ").capitalize()
        if species_input in species:
            break
        else:
            print("Invalid species. Please choose from the list.")

    while True:
        favorite_food = input(f"What is their favorite food?\n{', '.join(foods)}\n>> ").title()
        if favorite_food in foods:
            break
        else:
            print("Invalid food. Please choose from the list.")


    pet_bat = VirtualPet(name, species_input, favorite_food)
    stats = Attributes(70, 70, 70, 70, 0, pet_bat)
    actions = Actions(stats, pet_bat, False)
    return stats, actions

stats, actions = create_pet()

def reduce_attributes(health=0, hunger=0, sleepiness=0, fun=0):
    stats.health -= health
    stats.hunger -= hunger
    stats.sleepiness -= sleepiness
    stats.fun -= fun

def menu():
    while True:
        try:
            choice = int(input("""
          VIRTUAL PET MENU               
======================================
1 - Eat                      
2 - Play                     
3 - Sleep                    
4 - Status       
5 - Health                                       
0 - Exit       
======================================                               
>> """))
        except ValueError:
            print("Invalid input! Please enter a number.")
        
        if choice == 1:
            actions.eat()
            reduce_attributes(5, 0, 10, 5)
            stats.check_game_over()
        elif choice == 2:
            actions.play()
            reduce_attributes(5, 5, 10, 0)    
            stats.check_game_over()
        elif choice == 3:
            actions.sleep()
            reduce_attributes(5, 5, 0, 10)
            stats.check_game_over()
        elif choice == 4:
            stats.show_status()
        elif choice == 5:
            actions.health()
        elif choice == 0:
            confirmation = input("Are you sure you want to leave? Your progress will be lost! (Type 'Y' if you're sure.) ").upper()
            if confirmation == "Y":
                print("Turning off...")
                exit()
            else:
                print("You chose not to leave!")
                continue
        else:
            print("Invalid option. Please choose between 0 and 4.")
menu()