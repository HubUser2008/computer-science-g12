import random, string, json, os # this imports modules for random numbers, JSON handling, and file operations; all of which will be
# used below
import time # Imports the time module so that I can input delays in between s_prints and prints

def roll(min_val, max_val):
    return random.randint(min_val, max_val) # Depending on what the minimum value and maximum value are, this returns a random integer
# value in between those min and max values, including the min and max values themselves

def s_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

class roguelite_main_character:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.strength = 5
        self.dexterity = 5 # Dexterity refers to one's skill in performing tasks, especially tasks that are completed with hands
        self.intelligence = 10
        self.level = 1
        self.experience = 0
        self.glory_points = 0
        self.health_potions = 2
        self.deaths = 0

        if self.health <= 0:
            print("You have died. Your journey ends here, weak warrior...") # If the player's health is less than or equal to 0, meaning
            # that the player has died in battle, then this print message will pop up

    def display_stats(self):
        print(f"\n{self.name} - Henry Bartholomew") # The \n is used to move the player's name and the rest of the player's stats
        # down 1. All these print messages defined in this function, display_stats, are used to print whatever the player's current
        # stats are
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Glory Points: {self.glory_points}")
        print(f"Stats: STR={self.strength}, DEX={self.dexterity}, INT={self.intelligence}")
        print(f"Health Potions: {self.health_potions}")
    
    def level_up(self):
        self.level += 1
        self.health = 100 + (10 * self.level) # The player's health is dependent on whatever the player's current level is. The
        # player's health will be 10 times whatever their current level is, added onto the constant 100, meaning that the least amount
        # of health that a player can have (excluding the very beginning) is 100.
        self.strength += 10 # For every level that the player gains, the player's strength will increase by 10 from what it was originally
        self.dexterity += 10 # For every level that the player gains, the player's dexterity will increase by 10 from what it was originally
        self.intelligence += 10 # For every level that the player gains, the player's intelligence will increase by 10 from what it was originally
        print(f"\n{self.name} has leveled up to Level {self.level}!") # Whenever the player's level increases, which only happens
        # after a player has won a battle, a statement of the player's name along with the level that they leveled up to, will show up
    
    def combat_win(self, enemy):
        self.glory_points += enemy.glory_points # This adds the number of glory points that the enemy had, to the number of glory points
        # that the player currently has (obviously only when the player has successfully beaten the enemy in a battle)
        self.experience += enemy.experience # This adds experience that the enemy had, to the experience that the player currently has
        # (obviously only when the player has successfully beaten the enemy in a battle)
        print(f"\nYou defeated {enemy.name}!") # The name of the enemy that the player (you) defeated in a battle
        print(f"Glory points taken from your opponent: {enemy.glory_points}") # The amount of glory points that the player (you) took
        # from your opponent
        if self.experience >= self.level * 10: # If the player's experience is greater than or equal to the player's level multiplied by
            # 10, then the player will level up
            self.level_up()

class medieval_enemy:
    def __init__(self, name, health, attack, difficulty, glory_points, experience): # Function used to store the enemy's name,
        # health, numerical value of attack, it's difficulty (which will be stored as a string), number of glory points (used in the
        # shop), and the experience that the player will gain when the player defeats the enemy
        self.name = name
        self.health = health
        self.attack = attack
        self.difficulty = difficulty
        self.glory_points = glory_points
        self.experience = experience

class Shop:
    shop_inventory = { # This is the dictionary of the items that will be displayed in the shop (afterlife merchant), along with 
        # their base prices
        "Small Health Potion": 50,
        "Medium Health Potion": 150,
        "Large Health Potion": 300,
        "Legendary Sword": 1000
    }

    @staticmethod # This makes a function that doesn't receive self (which is an instance) or cls (class) as the first parameter
    # Furthermore, "@staticmethod" binds the function, which is defined as a staticmethod, to the class rather than to instances of 
    # the class. And whatever is defined as a static method can be called on the class itself, without having to call it as an instance
    # And furthermore, @staticmethod makes it so that when the function that was defined as a static method 
    def display_shop(): # @staticmethod is used here because the function, display_shop, is a function that is just used to show 
        # the shop's inventory, as it doesn't need any parameters itself since it's not an object.
        print("\n=== WELCOME TO THE SHOP ===")
        for item, price in Shop.shop_inventory.items():
            print(f"{item} - {price} Glory Points")

    @staticmethod
    def buy_item(player):
        choice = input("Enter the item name you want to buy: ").strip().lower() # This makes the player's input case insensitive, so that 
        # if the player wants to buy a "Small Health Potion" for example, if they type "small health potion", it'll still work since the 
        # player's input is now case insensitive
        price = Shop.shop_inventory.get(choice)

        if price is None:
            print("That item does not exist!")
            return

        if player.glory_points >= price:
            player.glory_points -= price

            if "Potion" in choice:
                player.health_potions += 1
            elif choice == "Legendary Sword":
                player.strength += 10

            print(f"You purchased {choice}!")
        else:
            print("Not enough glory points!")

# .items() dictionary method displays the shop. .get() dictionary method  ensures that the 
# .pop() dictionary method removes the sword from the shop once the player, Henry Bartholomew the 3rd (III) has bought it from the shop

class combat:
    @staticmethod
    def battle(player, enemy):
        print(f"\nA wild {enemy.name} appears! Prepare for battle!")
        fight = True # Sets the variable called "fight" to true, and when fight is true, the player is now engaged in a battle with
        # an enemy
        while fight: # A continuous loop that will happen until the player has won the battle or lost the battle
            if enemy.health <= 0:
                print(f"\n{enemy.name} has been defeated!")
                player.combat_win(enemy)
                player.display_stats() # Displays the player's stats whenever they win a battle against an enemy
                return True
            elif player.health <= 0:
                print("\nYou have been defeated... You're weak and unworthy! Depart!")
                player.display_stats()
                return False
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
                    return False
                else:
                    print("Invalid choice!")

                if enemy.health > 0:
                    enemy_damage = roll(enemy.attack - 1, enemy.attack + 1)
                    player.health -= max(0, enemy_damage)
                    print(f"{enemy.name} dealt {enemy_damage} damage to you!")

class Storyline:
    def __init__(self, player):
        self.player = player
        self.next_battle = 1  # Tracks the  battle number that comes next (intended to be in chronological order, which it will be)

    def display_stats(self):
        print("\n=== CURRENT PLAYER STATS ===")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Glory Points: {self.glory_points}")
        print(f"Health Potions: {self.health_potions}")
        print(f"Deaths: {self.deaths}")
        print("============================\n")

    def save_game(self):
        data = { # Dictionary created and represented as the variable, "data", which tracks all of the player's stats
        "name": self.player.name,
        "health": self.player.health,
        "strength": self.player.strength,
        "dexterity": self.player.dexterity,
        "intelligence": self.player.intelligence,
        "glory points": self.player.glory_points,
        "health potions": self.player.health_potions,
        "level": self.player.level,
        "experience": self.player.experience,
        "deaths": self.player.deaths,
    }
        with open("save_file.json", "w") as file: # When the game is saved, the player's 'data' (which are all of the player's stats)
            # will be saved to a file that will be created called "save_file.json", hence why "json" was imported earlier.
            # the 'w' parameter means that the file will be created and the player's 'data' (player's stats) will be written in the
            # file
            json.dump(data, file) # This actually writes the player's 'data' to the JSON file, meaning that the 'save_file.json' file, 
            # will include all of the player's stats
        
        print("Game Progress Saved")
    
    def load_game(self):
        if not os.path.exists("save_file.json"): # This checks to see if the save file called "save_file.json" exists. If it doesn't
            # exist, 'False' is returned.
            return False

        with open("save_file.json", "r") as file: # This  opens the save file so that it can be read by the player
            data = json.load(file) # Since 'data' is the variable name that stores the player's stats, the save file will then include
            # and be loaded in the save file, meaning that "save_file.json" now includes the player's stats

        self.player.name = data.get("name", self.player.name)
        self.player.health = data.get("health", self.player.health)
        self.player.strength = data.get("strength", self.player.strength)
        self.player.dexterity = data.get("dexterity", self.player.dexterity)
        self.player.intelligence = data.get("intelligence", self.player.intelligence)
        self.player.glory_points = data.get("glory_points", 0)
        self.player.health_potions = data.get("health_potions", 0)
        self.player.level = data.get("level", 1)
        self.player.experience = data.get("experience", 0)
        self.player.deaths = data.get("deaths", 0)

        print("Save file loaded successfully.")
        return True

    def reset_player(self):
        self.player.health = 100 # This is a reset player function, which is called to action in the programming below, when the
        # player loses a battle, meaning that the player has died. When the player loses a battle (meaning that the player has died), the 
        # reset_player(self) function will be called to action, causing the player's health to be reset back to 100
    
    def display_achievement1(self):
        henry_achievement1 = {
            "GOBLIN GRUNT SLAYER"
            }
        
        if self.player.deaths == 0:
            s_print("\n===YOU'VE RECEIVED AN ACHIEVEMENT!===\n"
                "\n=== ACHIEVEMENTS ===\n")
            s_print(f"Achievement 1: {henry_achievement1}")

        if self.player.deaths >0:
            s_print("\nYou can no longer receive this achievement, as this is a prestige related achievement, meaning that once you've achieved this achievement, you have the achievement forever.\n")
            return False
    
    def display_achievement2(self):
        henry_achievement2 = {
                "BANDIT RAIDER DEVOURER"
            }
        s_print("\n=== YOU'VE RECEIVED AN ACHIEVEMENT===\n")
        s_print(f"Achievement 2: {henry_achievement2}")

    def check_achievements(self):
        choice1 = input("\nDo you want to display your achievements, so that you can see your current achievements? (Type 'yes' or 'no'): ").strip().lower()
        
        if choice1 == "yes":
            self.display_achievement1()
            self.display_achievement2()
        else:
            return False
    
    def shop(self, current_battle_num):
        s_print("\n=== THE AFTERLIFE MERCHANT APPEARS ===\n")

        shop_inventory = {
        "Small Health Potion": 50 + (self.player.deaths * 20),
        "Medium Health Potion": 150 + (self.player.deaths * 40),
        "Large Health Potion": 300 + (self.player.deaths * 60),
        "Legendary Sword": 1000 + (self.player.deaths * 200)
    }
        
        while True:  # Keep showing shop until player exits or buys something
            # Display shop inventory
            for item, price in shop_inventory.items():
                print(f"{item} - {price} Glory Points")

            choice = input("\nWhat would you like to buy? (or type 'exit' to leave the shop): ")

            if choice.lower() == "exit":
                print("You leave the shop...")
                return current_battle_num  # Return to the same battle number

            # Check if item exists in inventory
            price = shop_inventory.get(choice)
            if price is None:
                print("That item does not exist. Please try again.")
                continue  # Show shop again

            # Check if player has enough glory points
            if self.player.glory_points >= price:
                self.player.glory_points -= price

                if "Potion" in choice:
                    self.player.health_potions += 1
                    print(f"You purchased {choice}!")
                elif choice == "Legendary Sword":
                    self.player.strength += 10
                    print(f"You purchased {choice}!")
                
                # After successful purchase, ask if they want to continue shopping or exit
                continue_shopping = input("Purchase complete! Continue shopping? (yes/no): ").lower()
                if continue_shopping != "yes":
                    return current_battle_num  # Exit shop and continue to next battle
                # If they say yes, the while loop continues
            else:
                print("Not enough glory points. Re-enter a different option or exit the shop.")
                # The loop continues, showing the shop again

    def introduction(self):
        ''' s_print("Henry Bartholomew the 3rd (III)! WAKE UP!")
        s_print("Huh? Where am I?")
        s_print("You are at THE MEDIEVAL BATTLE ARENA! For you were kidnapped by the Beyond Warlord, and you are now a gladiator, who is forced to fight evil entities wrecking havoc in the Beyond World to hopefully defeat them, to then be able to fight the ULTIMATE BEYOND WARLORD, and once and for all, restore the peace and tranquility that was once present in the Beyond World prior to the presence of the ULTIMATE BEYOND WARLORD and his evil entities who are beneath him!")
        s_print("No, no no. This can't be happening...")
        s_print("Mr. Bartholomew the 3rd (III), what do you mean 'This can't be happening...'?")
        s_print("You don't understand! Firstly, I don't even know who you are, and secondly, I'm not even a gladiator! A gladiator must be strong but I'm beyond weak. I'm so weak to the point where I got kidnapped, and I don't even remember getting kidnapped! THAT'S HOW PATHETIC AND WEAK I AM!")
        s_print("Stop blabbering at ONCE Mr. Bartholomew the 3rd! No more of this nonsense and certainly no more talking! You are now a gladiator, and you will eventually become strong enough to beat the Beyond Warlord and finally restore peace to the Beyond World, for he has been terrorizing the Beyond World for centuries upon centuries!")
        s_print("WHY ME THOUGH!? YOU KEEP SAYING THAT I'VE BEEN 'CHOSEN' BUT WHY ME!? YOU DIDN'T EVEN CHOOSE SOMEONE FROM THIS SO CALLED 'BEYOND WORLD' TO RESTORE ITS ONCE PEACEFUL AND TRANQUILITY VIBE! YOU CHOSE SOMEONE FROM EARTH, AND OUT OF EVERYONE ON PLANET EARTH, ON GOD'S GREEN EARTH, WHY DID IT HAVE TO BE ME OF ALL PEOPLE!? LIKE I SAID BEFORE, I DON'T EVEN LIVE IN THE BEYOND WORLD AND I'M NOT EVEN FROM HERE TO BEGIN WITH! I AM FROM EARTH, AND ALSO, I DON'T EVEN KNOW HOW TO THROW A PUNCH, LET ALONE EVEN FIGHT TO BEGIN WITH! I LITERALLY GET MADE FUN OF ON EARTH FOR BEING THE WEAKEST PERSON IN MY SCHOOL! WHAT DON'T YOU GET!? I'M NOT CUT OUT FOR THIS!")
        s_print("SILENCE MR. BARTHOLOMEW THE 3RD! I won't tell you this again, for next time, I will kill you with my bare hands! Now pay attention-eth, for the most dangerous fights and battles of your life are about to begin!")
        s_print("FOR WELCOME GLADIATOR BARTHOLOMEW TO YOUR JOURNEY OF RESTORING PEACE & TRANQUILITY TO THE BEYOND WORLD! You are to defeat all of the powerful and most dangerous enemies leading up to the ULTIMATE, OH SO TERRIBLE, BEYOND WARLORD, OF THE BEYOND WORLD! Do you have what it takes, or are you just some puny, unworthy wimp that was kidnapped?")
        s_print("That last part! I am! I very much am!")
        s_print("Also, Mr. Bartholomew the 3rd (III), you will be granted a shop that you can access only if you decide to run away from a fight or if you lose a fight, since you must be helped in some way, as you're a very weak and fragile gladiator right now")
        s_print("Gee... thanks... I guess...")
        time.sleep(1)
        s_print("Oh my gosh... why is this happening to me...?")
        time.sleep(2)
        s_print("AHHHH! WHAT IS THAT!?")
        s_print("That is the first evil enemy that you will have to slay Mr. Bartholomew the 3rd (III)") '''
        s_print("Please. Just call me Bat...")
        self.next_battle = 1  # Set next battle to 1
        self.first_battle()
    
    def first_battle(self):
        s_print("You are now in your 1st battle confrontation!")
        s_print("The enemy is a weak, goblin grunt!")
        s_print("What will you do!?!?!?")
        
        time.sleep(1)
        
        enemy = medieval_enemy("Goblin Grunt", 20, 5, "easy", 100, 10)
        result1 = combat.battle(self.player, enemy)

        if result1 is True:
            if self.player.deaths >0:
                s_print("You can no longer receive this achievement, as this is a prestige related achievement, meaning that once you've achieved this achievement, you have the achievement forever.")
            elif self.player.deaths == 0:
                self.display_achievement1()
            self.next_battle = 2  # Set next battle to 2
            s_print("Wow! Even though the goblin grunt is very weak, I'm surprised that you actually managed to defeat it! You're getting stronger, and you are now 1 step closer to finally defeating the BEYOND WARLORD!")
            s_print("WATCH OUT THOUGH, for the next enemy is much stronger than the puny, weak goblin grunt. And look! Your next enemy has appeared right before you!")
            self.second_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(1)  # Pass current battle number to shop
            self.save_game()
            self.reset_player()
            self.first_battle()

    def second_battle(self):
        enemy = medieval_enemy("Bandit Raider", 120, 8, "easy-medium", 120, 50)
        result2 = combat.battle(self.player, enemy)
            
        if result2 is True:
            self.display_achievement2()
            self.next_battle = 3  # Set next battle to 3
            s_print("You have successfully survived your second battle. The road ahead is still quite long, but don't give up, for the end...\n")
            s_print("WILL BE WORTH IT!")
            s_print("WATCH OUT THOUGH, for the next enemy is much stronger than the Bandit Raider. And it could pop out against you at any moment...")
            s_print("LOOK NOW! IT'S SUDDENLY APPEARED RIGHT BEFORE YOU! THE ARMORED FOOTMAN! WATCH OUT, FOR HE'S DANGEROUS!")
            self.third_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(2)  # Pass current battle number to shop
            self.save_game()
            self.reset_player()
            self.first_battle()

    def third_battle(self):
        enemy = medieval_enemy("Armored Footman", 250, 12, "medium", 200, 100)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 4  # Set next battle to 4
            s_print("Oh my gosh... I genuinely don't believe it. You have actually managed to not only survive but triumph through 3 successful battles against the enemies of the Beyond World! This is absolutely incredible and you're doing amazing, Henry Bartholomew the 3rd")
            s_print("Yes, yes, I know. You were chosen and all, but despite you being the chosen one, I still had my doubts about you. Very heavy, suffocating doubts about you since you're just a scrawny, little, weak supposed 'gladiator'")
            s_print("Wow, thank you for being very uplifting after I just defeated the Bandit Raider, my toughest opponent yet. You were almost just as uplifting as my parents were when I told them that I wanted to drop out of school to be a stand up, medieval comedian for the vikings and knights at the local bar!")
            s_print("Yikes. How were you chosen to restore peace and tranquility to the Beyond World again?")
            s_print("You're not helping dude...")
            s_print("Anyway... time to get back on topic. Look! Your next enemy has appeared right before you! The Rogue Assassin! He's more dangerous and powerful than any enemy that you've faced up to this point, so be extra careful and cautious!")
            self.fourth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(3)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def fourth_battle(self):
        enemy = medieval_enemy("Rogue Assassin", 350, 15, "medium-difficult", 250, 150)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 5  # Set next battle to 5
            s_print("You just keep surprising me again and again. Amazing job so far, Henry Bartholomew the 3rd, or should I call you, the CHOSEN ONE!?")
            s_print("...")
            s_print("Tough crowd huh?")
            s_print("Anyway, continue pushing forward, as every push that you make is 1 step forward into finally defeating the ULTIMATE BEYOND WARLORD, and restoring peace to the Beyond World!")
            s_print("Okay. I wi- WOAH! WHO IS THIS!?")
            s_print("The bloodthirsty, dangerous, and powerful War Hound... He is so much stronger than the Rogue Assassin. Defeating it almost guarantees your victory towards your destiny! So go, and make sure that the doggy sits!")
            self.fifth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(4)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def fifth_battle(self):
        enemy = medieval_enemy("War Hound", 500, 20, "difficult", 300, 300)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 6  # Set next battle to 6
            s_print("Spectacular! You actually managed to defeat the War Hound! I'm honestly in shock right now, and you just continue to impress me more and more, and put me more and more in shock!")
            s_print("Heh. I thought I was a gladiator, not an electrician.")
            s_print("Again... why were you chosen to begin with?")
            s_print("I'll just go and fight the next enemy of the Beyond World, whoever it'll be. It won't matter anyway though. I've transformed from a weak and puny gladiator, into a strong and terrifying one. I could defeat the Beyond Warlord right now if I were to encounter him. Piece of cake, pshhh!")
            s_print("Calm down 'Bat.' The Beyond Warlord is at least ten thousand (10,000) stronger than you and all the enemies that you've fought against combined. You're getting a lot stronger, but you're still a rookie.")
            s_print("YOUR REIGN OF TERROR ENDS HERE, GLADIATOR!")
            s_print("WOAH. This one talks! The enemies who are able to talk, within the Beyond World, are typically must stronger than the enemies who can't. You've got your work cut out for you here Mr. Bartholomew the 3rd!")
            self.sixth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(5)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def sixth_battle(self):
        enemy = medieval_enemy("Dark Mage", 600, 60, "EXTREMELY DIFFICULT", 400, 400)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 7  # Set next battle to 7
            s_print("I know that I'm sounding like a broken record here, but this is just absurd! You've come so far! I'm truly proud of you! But your work here is not finished.")
            s_print("You still have a long way to go. Watch out for your next enemy. It could pop out at any moment, and obviously, it'll be much stronger than the enemy that you just faced, despite the talking enemy that you just previously faced.")
            time.sleep(2)
            s_print("LOOK OUT! IT'S THE SHIELD CAPTAIN!")
            self.seventh_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(6)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()
    
    def seventh_battle(self):
        enemy = medieval_enemy("Shield Captain", 700, 50, "BEYOND IMPOSSIBLE", 450, 450)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 8  # Set next battle to 8
            s_print("You actually managed to defeat the Shield Captain! The Shield Captain is strong enough to contend with me. Obviously I'd still win, but nonetheless, the Shield Captain is not a pushover in the slightest, and yet you were able to take it down...!")
            s_print("EXCELLENT! Continue on this glorious, victorious road, Mr. Bartholomew the 3rd (III)!")
            time.sleep(2)
            s_print("I'LL KILL YOU, GLADIATOR! YOU'RE NOT EVEN WORTHY ENOUGH TO BE CALLED OR EVEN BE RECOGNIZED AS A GLADIATOR! I'LL TEAR YOU TO SHREDS!")
            s_print("Oooh, shiver me timbers. I'm quaking in my shining armor. I've defeated all the other enemies up to this point. The outcome of our battle won't be any different, 'Berseker Warrior.' What a lame name.")
            self.eigth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(7)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()
    
    def eigth_battle(self):
        enemy = medieval_enemy("Berseker Warrior", 800, 75, "CRAZY IMPOSSIBLE", 500, 500)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 9  # Set next battle to 9
            s_print("Okay... you might be stronger than me now, and that's scaring me a little bit since you were just some weak, unknown gladiator prior to all these battles.")
            s_print("I'm definitely stronger than you now. I'm a whole new different person than I was back when I was first got kidnapped. I could even say that I'm too strong now. Where is that Beyond Warlord. I'll end him quickly and finally be able to go back to Earth to brag and show my family and friends how strong I've become!")
            time.sleep(1)
            s_print("You don't listen do you? I told you, you've become so much stronger, but the Beyond Warlord is out of this world, both figuratively and literally. He's on a whole different level. I like the confidence but you still need to be careful, cautious, and you still need to fight more enemies to strengthen yourself even more!")
            s_print("yeah, yeah whatever. Where's this next enemy at though? I want to fight him already!")
            time.sleep(2)
            s_print("Sorry to keep your death waiting, supposed 'gladiator.' I see that you have defeated the Berseker Warrior. Impressive. But you must now go against me. It doesn't matter how strong you've become. I'll end you. For again, sorry for stalling your death for this long.")
            s_print("Big talk for someone who's about to get stomped, heh")
            self.ninth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(8)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def ninth_battle(self):
        enemy = medieval_enemy("Demonic WarKnight", 1000, 100, "BEYOND CRAZY IMPOSSIBLE", 1000, 1000)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 10  # Set next battle to 10
            s_print("Damn it. I hate to admit it, but you're definitely stronger than me now. I wouldn't have been able to defeat the Demonic Warknight. That being is too strong and fast for me, and yet, you were able to fend it off with relative ease.")
            time.sleep(1)
            s_print("That fight definitely wasn't relatively easy, as it was the most difficult one yet, but I wouldn't say that it was hard either. I'm really built different now. I'm the strongest, and I'll truly prove to you that I'm the strongest when I defeat the Beyond Warlord!")
            s_print("That won't be happening anytime soon, warrior gladiator. I see that you defeated the Demonic Warknight. Not impressive at all in the slightest. I could have killed that guy with my eyes closed whenever I wanted to, just like I could kill you whenever I want to. And I want to right now. Your journey ends here, for I'll make sure that you won't be able to fight my father, the ULTIMATE, OH SO TERRIBLE, OH SO POWERFUL, BEYOND WARLORD! For you're not even worthy of being in his presence, let alone fighting him!")
            time.sleep(1)
            s_print("Again, again, and again. So much talk and hype for something that I'm about to stomp on and crush like a little, insignificant bug. You're an insect to me. I'll make sure that you're not breathing soon.")
            time.sleep(1)
            s_print("I'd like to see you try, gladiator...")
            self.tenth_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(9)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def tenth_battle(self):
        enemy = medieval_enemy("The Fallen WARLORD", 2000, 200, "ULTIMATELY BEYOND CRAZY IMPOSSIBLE", 2000, 2000)
        result = combat.battle(self.player, enemy)
        if result is True:
            self.check_achievements()
            self.next_battle = 11  # Set next battle to 11
            s_print("AHHHHHH! YOU DEFEATED THE BEYOND WARLORD'S SON! OH MY GOSH, OMG OMG OMG! THAT'S SO INCREDIBLY IMPRESSIVE, YOU DON'T EVEN UNDERSTAND")
            time.sleep(1)
            s_print("Although this is great news, the BEYOND WARLORD is going to be so pissed, and he'll surely pop out at any moment.")
            time.sleep(1)
            s_print("Let him reveal himself. He'll suffer the consequences for doing so!")
            time.sleep(2)
            s_print("WHO SHALL SUFFER CONSEQUENCES, PUNY GLADIATOR!?")
            time.sleep(1)
            s_print("YOU DEFEATED MY SON! BIG WHOOP. I HAVE THOUSANDS OF OTHER VERSIONS OF HIM LAYING AROUND ELSEWHERE ON OTHER PLANETS!")
            time.sleep(1)
            s_print("THOUGH, YOU DEFEATING MY SON IS VERY DISRESPECTFUL TO ME. I'LL GIVE YOU A PERMANENT REASON AS TO WHY YOU SHOULD HAVE NEVER COME HERE IN THE FIRST PLACE, 'THE CHOSEN ONE!'")
            time.sleep(1)
            s_print("I defeated one of your many sons, and I'll defeat you too. You don't scare me anymore. You're nothing but another enemy that I'll stomp once again. In fact, you are NOTHING.")
            time.sleep(1)
            s_print("INSOLENT, PRIDEFUL, ARROGANT, AND IGNORANT HUMAN! I WILL SILENCE YOU AT ONCE!")
            time.sleep(1)
            s_print("Even though I'm basically your tour guide through this whole entire thing and I'm pretty strong myself, I'm so scared that I could pee my pants through my silver armour. Oh my gosh...")
            time.sleep(1)
            s_print("Please, keep that to yourself next time... Way too much unnecessary information...")
            s_print("WHAT THE WEAK GLADIATOR SAID! NOW COME, SO THAT YOU CAN ENTER YOUR COFFIN ALREADY!")
            self.eleventh_battle()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(10)  # Pass current battle number to shop
            self.check_achievements()
            self.save_game()
            self.reset_player()
            self.first_battle()

    def eleventh_battle(self):
        enemy = medieval_enemy("THE ULTIMATE, OH SO TERRIBLE, OH SO POWERFUL, BEYOND WARLORD", 5000, 1000, "Give up.", 99999999999999999999999, 99999999999999999999999999)
        result = combat.battle(self.player, enemy)
        if result is True:
            s_print("AHHHHHHHHHHH! OH MY GOSH! WOW! YOU ACTUALLY DID IT")
            s_print("WOW! I CAN'T BELIEVE YOU ACTUALLY ACCOMPLISHED YOUR DESTINY AND WHAT YOU WERE CHOSEN FOR, MR. BARTHOLOMEW THE 3RD. MR CHOSEN ONE! You've gone through countless of battles, countless of strong enemies, and countless of hardships, and they all boiled down to this one moment. This one true moment...")
            time.sleep(2)
            s_print("THIS ONE TRUE MOMENT OF TAKING ON THE BEYOND WARLORD HEAD ON. 1 ON 1. AND YOU ACTUALLY MANAGED TO DEFEAT HIM! THE MOST POWERFUL BEING IN ALL OF EXISTENCE! AND YOU DEFEATED HIM ALL BY YOURSELF THROUGH HARD WORK, DETERMINATION, GRIT, RESILIENCE, AND OBVIOUSLY, THROUGH TRUE STRENGTH! YOU ARE THE STRONGEST BEING TO EVER LIVE.")
            time.sleep(2)
            s_print("But let's not forget, you have finally restored peace to the Beyond World, for the Beyond Warlord has been terrorizing the Beyond World for centuries upon centuries, and now, thanks to you, the Beyond World can finally live in peace! You are a true hero, and you will be remembered as one for all of eternity!")
            time.sleep(2)
            s_print("Now, you can finally return back to your true home world, for your mission here has been completed. And don't worry, you'll still be the strongest being in all of existence back at your home world as well, for you have truly earned this.")
            time.sleep(2)
            s_print("Heh, now I can finally call you a true Gladiator. In fact, not only are you a true Gladiator, you're a god gladiator. You are the godiator!")
            time.sleep(2)
            s_print("NOW! DO AS YOU PLEASE!")
            time.sleep(1)
            s_print("Gladly. Thank you.")
            self.check_achievements()
        else:
            self.player.deaths += 1
            battle_to_return_to = self.shop(11)  # Pass current battle number to shop
            self.check_achievements()
            self.reset_player()
            self.first_battle()

if __name__ == "__main__":
    gladiator_name = "Henry Bartholomew the 3rd (III)"
    player = roguelite_main_character(gladiator_name)
    storyline = Storyline(player)

    loaded = storyline.load_game()

    if not loaded:
        storyline.introduction()
    else:
        print("Resuming your journey...")
        storyline.first_battle()