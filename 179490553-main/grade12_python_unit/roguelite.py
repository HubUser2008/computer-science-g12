import math, os

game = True

dollabills ={"money":100,"influence":0,"Debt":0}
money_makers=   {
                "LemonsRus":{"num_stores":0, "cost":50, "level":1, "income":10},
                "Cafe":{"num_stores":0, "cost":500, "level":1, "income":80},
                "DeezSeedz":{"num_stores":0, "cost":5000, "level":1, "income":640},
                }


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
    os.system("cls")
    print("Ha Ha business go up")


    player_options = ["Pass a round","Buy a business","Throw it all away"]
    
    print("____________________________________________________________________________________")
    print(f"Current stats \n \t money available = {dollabills['money']} \n" )
    print("____________________________________________________________________________________")
    for i in zip(range(1,4),player_options):
        print(str(i[0])+" "+i[1])
    player_choice = input("Select an option:  ")
    while player_choice not in ("1","2","3"):
        player_choice = input("Select an option:  ")


    if player_choice == "1":
        earnings(money_makers)
    
    elif player_choice == "2":
        for business in money_makers.keys():
            print(f"(You have {money_makers[business]["num_stores"]})")
        pass