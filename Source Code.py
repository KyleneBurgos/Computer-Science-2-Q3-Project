import random as rand
import math
import time

points = 0
artifact = 1 #Expanded in the future
lives = 100
protection = 1 #Expanded in the future

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
        5: {"symbol": randSymbol3,  "min": 1, "normMax":200, "advMax":25, "powMax":5, "exp":2},
        6: {"symbol": randSymbol3,  "min": 1, "normMax":500, "advMax":50, "powMax":9, "exp":3} }
    
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

def question(grade, multiplier, attempts):

    global points, lives #so it can actually be modified
    config = mathProblems(grade)
    symbol = config["symbol"]()
    num1, num2 = genNumbers(symbol, config)
    correct = calculate(num1, num2, symbol)

    print(f"{num1} {symbol} {num2} = ?")
    while attempts != 0:
        try:
            
            answer = int(input(">>     "))
        except ValueError:
            print("Uhm.. What? Input the right format of answer")
            continue

        if answer == correct:
            points += (1*multiplier*artifact)
            print("")
            print("Verdict: Correct!")
            print(f"Points: {points}")
            break
        else:
            attempts -= 1
            points -= 1
            print("")
            print("Verdict: Wrong!")
            print(f"Attempts left: {attempts}")

        print("")
        if attempts == 0:
            lives -= (5*protection)
            print(f"Lives: {lives}")



while lives > 0:
    print("""Are you ready to enter the stages of math?
Well even if you aren't, then we are starting!
""")

    print("-----Stage 1: Easy-----")
    for i in range(1,6):
        question(1,1,3)
        print("")
    print("Great, you are doing well so far. Lets crank up the difficulty!")
    print("-----Stage 2: Medium-----")
    for i in range(1,6):
        question(4,1,3)
        print("")
    lives += 20
    print("Im surprised you survived that. Good luck, you'll need these lives.")
    print(f"Lives = {lives}%")
    print("")
    print("-----Stage 3: Hard-----")
    for i in range (1,4):
        print("Sudden Death")
        question(6,1,1)
        print("")   
        
    print("Oh well since you actually passed that somehow.. great job!")
    space(5)
    print("-----Score Board-----")
    print(f"Points: {points}")
    print(f"Lives: {lives}")
    print("Evaluating..")
    time.sleep(2)
    
    if points >= 13 and lives >= 100:
        print("Flawless!")
    else:
        print("Good Job!")
        
    space(2)
    
    check = int(input("Would you like to continue or exit? (1 to continue, 2 to exit):     "))
    if check == 1:
        print("Restarting..")
        lives = 100
        points = 0
        continue
    else:
        print("Exiting...")
        break
