# Question 1
''' num = int(input("Provide a number: "))
num2 = int(input("Provide another number: "))

if num%2 and num2%2:
    print(num - num2)
    print(num2 - num)
    print("Your number is odd")
elif num%2 and not num2%2 or num2%2 and not num%2:
    print(num*num2)
    print("1 number is even and the other number is odd")
else:
    print(num + num2)
    print("Your number is even")
'''
# Question 2
''' num = int(input("Provide a 3 digit number to check if all digits are even: "))
remainder = 0
if num%2==0:
    remainder = num%10
    num = num - remainder
    num = num/10
    if num%2==0:
        remainder = num%10
        num = num - remainder
        num = num/10
        if num%2==0:
            print("All digits are even")
'''
#More Code Efficient Version of Question 2
''' num = int(input("Provide a 3 digit number to check if all digits are even: "))
remainder = 0

while num%2==0:
    remainder = num%10
    num = num - remainder
    num = num/10
        print("All digits are even")
'''
# Question 3 Answer Using A For Loop
''' x = range(0, 500520, 2)
for n in x:
    print(n)
'''
# Question 3 Answer Using A While Loop
''' sum = 0
i = 0
while i<500520 and sum<500520:
    i = i + 2
    print(i-2)
'''

# Question 4 (rock, paper, scissors question)
import random

playagain = True
while(playagain):


    Computer_opponent = random.choice(["rock", "paper", "scissors"]) #randomly picks 1 from the list

    Player_choice = str(input("Are you choosing rock, paper, or scissors?: "))

    #checks if you tied
    if Player_choice==Computer_opponent:
        print("You tied")

    #checks if you won
    elif (Player_choice=="rock" and Computer_opponent=="scissors") or (Player_choice=="paper" and Computer_opponent=="rock") or (Player_choice=="scissors" and Computer_opponent=="paper"):
        print("You win")
    #checks if you lost
    else:
        print("You lost")

    user_choice = str(input("Do you want to play again? Yes or No?: "))
    if user_choice=="No":
        playagain = False
