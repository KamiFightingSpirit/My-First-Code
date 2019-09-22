from math import factorial
from sys import exit

def orderDoesNotMatter():
    
    while True:
        try:
            combinationOrPermutation = input("Does order matter? Please enter Y/N: ")
            break
        except ValueError:
            print("You did not enter Y/N ")
            
    while True:
        try:
            n = int(input("Please enter an integer for n: "))
            break
        except ValueError:
            print("You did not enter an integer ")
    while True:
        try:
            r = int(input("Please enter an integer for r: "))
            break
        except ValueError:
            print("You did not enter an integer ")
    
  
    while True:
        try:
            numberOfWays = (factorial(n)/(factorial(n-r) * factorial(r)))
            break
        except ValueError:
            r = input("There are 0 combinations of r > n, please enter a new r, to exit please type 'Y': ")
            if r.lower() == 'y':
                exit()
            else: 
                r = int(r)
                    
    return numberOfWays

nChooseR = orderDoesNotMatter()
print("The number of combination is: ")
print(nChooseR)
