    import random as rand
import math
import time

points = 0
artifact = 1 #Expanded in the future
lives = 50
protection = 1 #Expanded in the future

symbols1 = ("+","-")
symbols2 = ("*","/")
symbols3 = ("^", "√")

def space(x):       #Adds blank lines
    for i in range(x):
        print("")
        
def randSymbol1():  #Picks randomly from values of 'symbols1', which is + and -
    return symbols1[rand.randint(0,1)]

def randSymbol2():  #Picks randomly from combined values of 'symbols1' and 'symbols2', which is +,-,* and /
    combinedSymbols1 = symbols1 + symbols2
    return combinedSymbols1[rand.randint(0,3)]

def randSymbol3():  #Picks randomly from combined values of 'symbols1','symbols2', and 'symbol3', which is +,-,*,/,^ and √
    combinedSymbols2 = symbols1 + symbols2 + symbols3
    return combinedSymbols2[rand.randint(0,5)]

def mathProblems(grade):    #Controls the difficulty of questions, each number corresponds to a grade level. 
    config = {
        1: {"symbol": lambda: "+",  "min": 1, "normMax":10},
        2: {"symbol": randSymbol1,  "min": 1, "normMax":20},
        3: {"symbol": randSymbol1,  "min": 1, "normMax":50},
        4: {"symbol": randSymbol2,  "min": 1, "normMax":100, "advMax":12},
        5: {"symbol": randSymbol3,  "min": 1, "normMax":200, "advMax":25, "powMax":5, "exp":2},
        6: {"symbol": randSymbol3,  "min": 1, "normMax":500, "advMax":50, "powMax":9, "exp":3} }
    
    return config.get(grade,config[1]) #if smth went wrong, default to Grade 1
    

def genNumbers(symbol,grade): #number generator that ensures no decimals and no negatives

    mini = grade["min"]     #smallest no. allowed

    if symbol in ("+", "-"):
        maxi = grade["normMax"]
        
    elif symbol in ("*", "/"):
        maxi = grade["advMax"]
        
    elif symbol in ("^", "√"):
        maxi = grade["powMax"]
        exp = grade["exp"]
    #based on each symbol
    if symbol == "+":
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini, maxi)
        correct = num1+num2

    elif symbol == "-":
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini,num1) #makes the num2 always smaller or equal to num1, preventing negatives
        correct = num1-num2 

    elif symbol == "*":
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini, maxi)
        correct = num1*num2

    elif symbol == "/": 
        num2 = rand.randint(mini, max(2, maxi)) #doesnt make it divide by 0 since the limit is 2 to prevent undefined
        correct = rand.randint (1,max(1, maxi// num2))  #multiplier (a.k.a  nswer)  turn mun1 into a factor of num2; prevents randint(1,0) which can make program crash
        num1 = num2 * correct                    #makes num2 a factor of num1 so no decimals
    
    elif symbol == "^":
        num1 = rand.randint(mini,maxi)
        num2 = exp
        correct = num1**num2

    elif symbol == "√":
        correct = rand.randint(2,8) # the base
        num2 = rand.randint(2,exp)
        num1 = correct**num2
    else:
        num1 = rand.randint(mini,maxi)
        num2 = rand.randint(mini,maxi)
        correct = num1+num2
    return num1, num2, correct        

def question(grade, multiplier, attempts):

    global points, lives                #so it can actually be modified
    config = mathProblems(grade)
    symbol = config["symbol"]()
    num1, num2, correct = genNumbers(symbol, config)

    print(f"{num1} {symbol} {num2} = ?")
    while attempts > 0:
        try:
            answer = int(input(">>     "))
        except ValueError:
            print("Uhm.. What? Input the right format of answer")
            continue

        if answer == correct:
            points += (multiplier*artifact)
            print("")
            print("Verdict: Correct!")
            print(f"Points: {points}")
            return
        else:
            attempts -= 1
            points -= 1
            print("")
            print("Verdict: Wrong!")
            print(f"Attempts left: {attempts}")
        print("")
    lives = max(0,lives - (5*protection))
    print(f"Lives: {lives}")

#_________________________Gameloop_________________________

while lives > 0:
    print("""Are you ready to enter the stages of math?
Well even if you aren't, then we are starting!
""")

    print("-----Stage 1: Easy (Grade 1-2) -----")
    for i in range(1,6):
        question(1,1,3)
        print("")

    print("Great, you are doing well so far. Lets crank up the difficulty!")
    print("-----Stage 2: Medium (Grade 3-4) -----")
    for i in range(1,6):
        question(4,1,3)
        print("")
    lives += 15
    print("Im surprised you survived that. Good luck, you'll need these lives.")
    print(f"Lives = {lives}")
    print("")
    print("-----Stage 3: Hard (Grade 5-6) -----")
    for i in range (1,4):
        print("Sudden Death")
        question(6,1,1)
        print("")   
        
    print("Oh well since you actually passed that somehow.. great job!")
    space(5)