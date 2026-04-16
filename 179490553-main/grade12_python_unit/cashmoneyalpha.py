import math, os

game = True
#us as a player and keys for stats
dollabills ={"money":100,"influence":0,"Debt":0}
#availabe businesses and their stats (both owned and unowned)
money_makers=   {
                "LemonsRus":{"num_stores":1, "cost":50, "level":1, "income":10},
                "Cafe":{"num_stores":0, "cost":500, "level":1, "income":80},
                "DeezSeedz":{"num_stores":0, "cost":5000, "level":1, "income":640},
                }

#calculates amount of money earned in a single round
def earnings(money_dict):
    for business in money_dict.keys():
        dollabills["money"]+= money_dict[business]["num_stores"]*(money_dict[business]["income"] +0.3* money_dict[business]["level"])


def add_influence(money_dict):
    n=1
    tot_income = 0
    for business in money_dict.keys():
        tot_income+= money_dict[business]["num_stores"]*(money_dict[business]["income"] +0.3* money_dict[business]["level"])
    while 2**n<tot_income:
        n+=1

    dollabills["influence"]+=n
    


#Lawyered

#milestones

while game:
    os.system('clear')
    print("Ha Ha business go up")


    player_options = ["Pass a round","Buy a business","Throw it all away","Spend Influence"]
    
    print("____________________________________________________________________________________")
    print(f"Current stats \n \t money available = {dollabills['money']} \n" )
    print("____________________________________________________________________________________")
    for i in zip(range(1,5),player_options):
        print(str(i[0])+" "+i[1])
    player_choice = input("Select an option:  ")
    while player_choice not in ("1","2","3","4"):
        player_choice = input("Select an option:  ")


    if player_choice == "1":
        earnings(money_makers)
    
    elif player_choice == "2":
        for business in money_makers.keys():
            print(f"You have {money_makers[business]["num_stores"]} {business}")
            print(f"Cost to buy another is {money_makers[business]["cost"]}\n")
        buy_this = input("Which one would you like to buy?")
        if buy_this in money_makers.keys():
            if dollabills["money"]>=money_makers[buy_this]["cost"]:
                money_makers[buy_this]["num_stores"]+=1
                dollabills["money"]-=money_makers[buy_this]["cost"]
                custom_wait = input("Hit Enter to Continue")
            else:
                earnings(money_makers)
                print("I've held your hand here, you couldn't affort the business \n here is your regular income instead")
        else:
            print("type better next time")
    
    elif player_choice=="3":
        print("Time to cash it in")
        add_influence(money_makers)
        print(f"You now have {dollabills['influence']} influence")
        custom_wait = input("Hit Enter to Continue")
        dollabills ={"money":100,"influence":0,"Debt":0}


    elif player_choice=="4":
        print("Which buisness would you like to upgrade?")
        while dollabills["influence"]>0:
            up_choice=input("Type the name of the business you would like to upgrade or type NA to exit")
            if up_choice in money_makers.keys():
                num_ups = int(input("How many upgrades would you like to spend"))
                if num_ups>dollabills["influence"]:
                    print("You have not enough influence")

                else:
                    money_makers[up_choice]["level"]+= num_ups
                    dollabills["influence"]-= num_ups
            elif up_choice == "NA":
                break

            else:
                print("Typing is hard")


# still left unfinshed / disfunctional
'''
- reset values
- read and write to a save file
- debt and debt collector mini game?
- '''