import random

#Fighter Type:
#Beginner, Intermediate, Advanced
class Fighter_Type:

    #Fighter Option
    def __init__(self, fighter_option):
        self.__fighter_option = fighter_option

    #Set Health to 100
    def __init__(self):
        self._health = 100

    #Sets fighter health min & max 0-100
    def fighter_health(self, updated_health):
        self._health = min(100, max(0, updated_health))
        return self._health
    #Sets fighter strength based on type of fighter
    def fighter_pick(self, fighter_pick=None):
        if self.__fighter_option == 1:
            fighter_pick == "Beginner"
            fighter_strength = random.randint(1, 30)
            return fighter_pick
        elif self.__fighter_option == 2:
            fighter_pick == "Intermediate"
            fighter_strength = random.randint(31, 60)
            return fighter_pick
        elif self.__fighter_option == 3:
            fighter_pick == "Advanced"
            fighter_strength = random.randint(61, 100)
            return fighter_pick
        else:
            print("Please make a correct selection for your fighter option!")

computerUser_health = 100
fighter_pick = True
active_fight = True

while fighter_pick == True:
    print("\nFighter Option\n1. Beginner\n2. Intermediate\n3. Advanced")
    fighter_selection = int(input("\nSelect a fighter: "))
    if fighter_selection == 1:
        print("You are a beignner")
    elif fighter_selection == 2:
         print("You are intermediate")
    elif fighter_selection == 3:
         print("You are advanced")
    else:
         print("Wrong option selected!")
    break;

while active_fight == True:
    print("\nAttack Options\n1. Punch\n2. Kick\n3. Slap\n4. Block")
    attack_choice = int(input("\nPick an attack: "))














