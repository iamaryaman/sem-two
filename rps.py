import random as r
  
def comp_choose():
    return r.randint(1, 3)

player1 = input("Player's choice - Type 1 for Rock, 2 for Paper, 3 for Scissors: ")

choicedict = {1:"Rock",2:"Paper",3:"Scissors"}

if player1.isdigit():
    player1= int(player1)
    player1 = choicedict[player1]
comp1 = choicedict[comp_choose()]

final = (player1,comp1)
finalcheck = {"Computer Wins":[("Rock","Paper"),("Scissors","Rock"),("Paper","Scissors")],"Player Wins":[("Rock","Scissors"),("Scissors","Paper"),("Paper","Rock")]}

print(f"{player1} is chosen by the player")
print(f"{comp1} is chosen by the computer")
for result, combination in finalcheck.items():
    if final in combination:
        print(result)
        break
else:
    print("Draw")  