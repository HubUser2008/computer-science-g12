from random import randint, choice
import time

# Utility functions
def roll(min_val, max_val):
    return randint(min_val, max_val)

def sleep(timer):
    if timer == "s":
        time.sleep(1)
    elif timer == "m":
        time.sleep(2)
    elif timer == "b":
        time.sleep(4)
    else:
        time.sleep(8)

def s_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

class main_character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 5
        self.dexterity = 5 #Dexterity refers to one's skill in performing tasks, especially tasks that are completed with hands
        self.intelligence = 10
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.health_potions = 2
        self.player = player

    def display_stats(self):
        print(f"\n{self.name} - Gareth Knight")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Gold: {self.gold}")
        print(f"Stats: STR={self.strength}, DEX={self.dexterity}, INT={self.intelligence}")
        print(f"Health Potions: {self.health_potions}")

    def level_up(self):
        self.level += 1
        self.health = 100 + (10 * self.level)
        self.strength += 5
        self.dexterity += 5
        self.intelligence += 10
        print(f"\n{self.name} has leveled up to Level {self.level}!")

    def combat_win(self, enemy):
        self.gold += enemy.gold
        self.experience += enemy.experience
        print(f"\nYou defeated {enemy.name}!")
        print(f"Gold taken from your opponent: {enemy.gold}")
        if self.experience >= self.level * 10:
            self.level_up()
# Enemy class
class enemy:
    def __init__(self, name, health, attack, difficulty, gold, experience):
        enemy.name = name
        enemy.health = health
        enemy.attack = attack
        enemy.difficulty = difficulty
        enemy.gold = gold
        enemy.experience = experience

# Combat System
class combat:
    @staticmethod
    def battle(self, enemy):
        print(f"\nA wild {enemy.name} appears! Prepare for battle!")
        fight = True
        while fight:
            if enemy.health <= 0:
                print(f"\n{enemy.name} has been defeated!")
                player.combat_win(enemy)
                fight = False
            elif player.health <= 0:
                print("\nYou have been defeated...")
                fight = False
            else:
                choice = input("(a)ttack, (d)efend, (h)eal, or (r)un: ").lower()
                if choice == "a":
                    damage = roll(player.strength - 2, player.strength + 2)
                    enemy.health -= max(0, damage)
                    print(f"You dealt {damage} damage to {enemy.name}!")
                elif choice == "d":
                    defense = roll(player.dexterity - 1, player.dexterity + 1)
                    player.health += defense
                    print(f"You defended, regaining {defense} health!")
                elif choice == "h":
                    if player.health_potions > 0:
                        player.health = min(player.health + 20, 100)
                        player.health_potions -= 1
                        print("You used a health potion!")
                    else:
                        print("No health potions left!")
                elif choice == "r":
                    print("You fled the battle!")
                    fight = False
                else:
                    print("Invalid choice!")

                if enemy.health > 0:
                    enemy_damage = roll(enemy.attack - 1, enemy.attack + 1)
                    player.health -= max(0, enemy_damage)
                    print(f"{enemy.name} dealt {enemy_damage} damage to you!")

# Example storyline
class Storyline:
    def __init__(self, player):
        self.player = player

    def start(self):
        s_print(f"Welcome, brave knight: {self.player}, to your journey for TRUE STRENGTH!\n")
        s_print("Your mission is to defeat the dangerous tribes, empires, and soldiers causing trouble in your city to RESTORE PEACE & to TRULY PROVE YOURSELF!")
        s_print("You will truly prove yourself by defeating the GREATEST VILLAIN of them all!")

        self.first_battle()

    def first_battle(self):
        enemy1 = enemy("Tribal Warrior", 30, 5, "easy", 10, 5)
        combat.battle(self.player, enemy)
        s_print("You have survived your first battle. The road ahead is long. Prepare yourself...")

        self.second_battle()

    def second_battle(self):
        enemy2 = enemy("Empire Soldier", 40, 8, "easy-medium", enemy.gold == 15, enemy.experience == 20)
        combat.battle(self.player, enemy)
        s_print("You have survive your second battle. The road ahead is still quite long, but don't give up, for the end...\n")
        s_print("WILL BE WORTH IT!")

        self.third_battle()

    def third_battle(self):
        enemy3 = enemy("Elite Guard", 55, 12, "medium", 20, 30)
        combat.battle(self.player, enemy)
        s_print("You have survive your third battle. Continue on the victorious road, knight...")

        self.fourth_battle()

    def fourth_battle(self):
        enemy4 = enemy("Crazy Empire Soldier", 70, 15, "medium-difficult", 25, 40)
        combat.battle(self.player, enemy)
        s_print("You have surprisingly survived your fourth battle. I thought you'd be dead by now. Congratulations for proving me wrong. Continue... for victory AWAITS you!")

        self.fifth_battle()

    def fifth_battle(self):
        enemy5 = enemy("Insane Warlord Junior", 85, 20, "difficult", 35, 70)
        combat.battle(self.player, enemy)
        s_print("")

        self.sixth_battle()

    def sixth_battle(self):
        enemy6 = ("The WARLORD", 100, 30, "EXTREMELY DIFFICULT", enemy.gold == 100, enemy.experience == 100)
        combat.battle(self.player, enemy)
        s_print("Wow. You did it. You really did it...\n")
        sleep("b")
        s_print("You transformed yourself from a weak, nobody warrior, to a god... for only gods could defeat the warlord...\n")
        sleep("b")
        s_print("You've truly proved yourself! You can finally call yourself, the STRONGEST!")

        if player.health <= 0:
            print("You have died. Your journey ends here, weak warrior...")

if __name__ == "__main__":
    knight_name = input("Enter the name of your weak knight: ")
    player = (knight_name)
    storyline = Storyline(player)
    storyline.start()
