import random as rand
import math
import time

points = 0

lives = 100

symbols1 = ("+","-")
symbols2 = ("*","/")
symbols3 = ("^", "√")
    
def space(x):
    for i in range(x):
        print("")
            
def randSymbol1():
    return symbols1[rand.randint(0,1)]

def randSymbol2():
    combinedSymbols1 = symbols1 + symbols2
    return combinedSymbols1[rand.randint(0,3)]

def randSymbol3():
    combinedSymbols2 = symbols1 + symbols2 + symbols3
    return combinedSymbols2[rand.randint(0,5)]

def miniMax(mini,maxi):
    return mini, maxi

def mathProblems(grade):
    config = {
        1: {"symbol": lambda: "+",  "min": 1, "normMax":10},
        2: {"symbol": randSymbol1,  "min": 1, "normMax":20},
        3: {"symbol": randSymbol1,  "min": 1, "normMax":50},
        4: {"symbol": randSymbol2,  "min": 1, "normMax":100, "advMax":12},
        5: {"symbol": randSymbol3,  "min": 1, "normMax":150, "advMax":20, "powMax":5, "exp":2},
        6: {"symbol": randSymbol3,  "min": 1, "normMax":300, "advMax":35, "powMax":9, "exp":3},
        7: {"symbol": randSymbol3, "min": 2, "normMax": 500, "advMax": 50, "powMax":9, "exp":3},
        8: {"symbol": randSymbol3, "min": 5, "normMax":750, "advMax": 85, "powMax": 12, "exp":4}}
    
    return config[grade]
    

def genNumbers(symbol,grade): #number generator that ensures no decimals and no negatives

    mini = grade["min"]

    if symbol in ("+", "-"):
        maxi = grade["normMax"]
        
    elif symbol in ("*", "/"):
        maxi = grade["advMax"]
        
    elif symbol in ("^", "√"):
        maxi = grade["powMax"]
        exp = grade["exp"]
    
    if symbol == "/":
        num2 = rand.randint(mini, max(2, maxi)) #doesnt make it divide by 0 since the limit is 2 to prevent undefined
        num1 = num2 * rand.randint(1, maxi // num2) #makes num1 a factor of num2 so no decimals
        
    elif symbol == "-":
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini,num1) #makes the num2 always smaller or equal to num1, preventing negatives

    elif symbol == "^":
        num1 = rand.randint(mini,maxi)
        num2 = exp
        
    elif symbol == "√":
        num2 = rand.randint(2,exp)
        num1 = rand.randint(2,maxi)**num2
    else:
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini,maxi)
        
    return num1, num2        
        
def calculate(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        return num1 // num2
    elif symbol == "^":
        return num1 ** num2
    elif symbol == "√":
        return round(num1 ** (1/num2))

def question(grade, multiplier, attempts, state):

    config = mathProblems(grade)
    symbol = config["symbol"]()
    num1, num2 = genNumbers(symbol, config)
    correct = calculate(num1, num2, symbol)

    print(f"{num1} {symbol} {num2} = ?\n")
    while attempts != 0:
        try:
            answer = int(input(">>     "))
        except ValueError:
            print("Uhm.. What? Input the right format of answer\n")
            continue

        if answer == correct:
            state['points'] += (1*multiplier)
            print("")
            print("Verdict: Correct!")
            print(f"Points: {state['points']}\n")
            break
        else:
            attempts -= 1
            state['points'] -= 1
            print("")
            print("Verdict: Wrong!")
            print(f"Attempts left: {attempts}\n")

        print("")
        if attempts == 0:
            state['lives'] -= (50)
            print(f"Lives: {state['lives']}\n")

def runGame(playerName, state): #so that each person has their unique stuff
    
    print(f"Welcome, {playerName}! Let's begin.\n")

    choice = 0
    while state["lives"] > 0 and choice != 2:
        print("1. Play")
        print("2. Quit to menu")

        try:
            choice = int(input("Enter your choice.. >> "))
            
        except ValueError:
             print("I cant read this format..\n")
             continue

        if choice < 1 or choice > 2:
            print("Thats not in the choices..\n")
            continue
        
        elif choice == 2:
            break


        #Stage 1 place holder
        space(2)
        if choice == 1:
##            space(5)
##            print("Once upon a time, in a dorm far far away, you were studying all\n")
##
##            print("night and became thirsty while cramming for a math test tomorrow.\n")
##
##            time.sleep(3)
##
##            print("You decided to get up and grab a glass of fresh coffee.\n")
##
##            
##            print("As you made your way back to your desk...\n")
##            time.sleep(4)
##            print(",you tripped over a piece of scratch paper you\n")
##            print("were using to vent out your mathematical stress..\n")
##            space(2)
##
##            time.sleep(5)
##          
