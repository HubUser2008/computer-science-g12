from ast import literal_eval

dollabills ={"money":10,"influence":0,"Debt":0}

money_makers=   {
                "LemonsRus":{"num_stores":1, "cost":50, "level":1, "income":10},
                "Cafe":{"num_stores":0, "cost":500, "level":1, "income":80},
                "DeezSeedz":{"num_stores":0, "cost":5000, "level":1, "income":640},
                }

def save_game():
    with open("save.txt","w") as my_file:
        my_file.write("dollabills = "+str(dollabills)+ "\n")
        my_file.write("money_makers = "+str(money_makers)+"\n")


def load_game():
    global dollabills, money_makers # this line of code allows for external definitions to exist in this function, so that the 
                                    # variables can be used outside of this function as well
    with open("save.txt", "r") as my_file:
        for line in my_file:
            key, value = line.strip().split('=',1)
            if key == "dollabills":
                dollabills = literal_eval(value)
            elif key == "money_makers":
                money_makers = literal_eval(value)
if __name__ == "__main__":
    save_game()
    # load_game()

    print(dollabills)
    print(money_makers)