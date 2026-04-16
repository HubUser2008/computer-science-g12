import random as rd
character = ["name", "health", "strength", "int"]
m_c = ["Space Man", 100, 12, 7]

print("You land on a strange planet and encounter a jelly like rock")
j_r = ["jelly like rock", 20, 5, 1]
choice1 = input("Would you like to pet, kick, or hug the rock?: ")
if choice1 == "pet":
    print("The jellyrock joins your party")
    m_c.append(["jellyrock"])
elif choice1 == "hug":
    print("The depressed jelly rock appreciates your sign of affection and blesses you with +10 health: ")
    m_c[1] = m_c[1] + 10
else:
    print("'You have chosen hate over love... time to die!' says the jelly rock")
    combat1 = input("punch, run, use potion")
    if combat1 == "punch":
        damage = rd.randint(0, m_c[2])
        j_r[1]-=damage
