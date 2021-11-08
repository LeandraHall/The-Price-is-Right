#This code will print the winning bid in comparison to the 
#randomly generated retail price between 1 and 1000 based
#on five unique unser-inputted bids

#Imports the function needed to randomly generate a 
#retail price
import random

#The function which houses the code to complete the purpose
#of this program
def priceIsRight(B1,B2,B3,B4,B5):
    #Variables needed to complete the code
    retailPrice = random.randint(0,1000)
    B1 = guess1
    B2 = guess2
    B3 = guess3
    B4 = guess4
    B5 = guess5
    #The list that houses all the guesses
    bidList = [B1, B2, B3, B4, B5]
    
    #A loop that iterates through each element of the list
    #to determine if it's greater than the retail price or
    #not and performs specific actions for each outcome
    for bid in bidList:
        if bid > retailPrice:
            index = bidList.index(bid)
            bidList[index] = 0
            #Stops the loop if each element in the bidList
            #is greater than the retail price
            if all(bid == 0 for bid in bidList):
                break
    
        if bid < retailPrice:
            index = bidList.index(bid)
            finalDiff = []
            diffX = retailPrice - bid
            bidList[index] = diffX
            #Creates a new list with all the differences 
            #not equal to zero
            for bid in bidList:
                finalDiff.append(bid)
    
    #An if branch that determines how the program should
    #proceed based on the elements in bidList
    if all(bid == 0 for bid in bidList):
        print("None of your bids were close to the retail price.", end="")
        print(" of $" + retailPrice)
    else:
        #Eliminates any zeroes in the finalDiff list
        finalDiff = [diff for diff in finalDiff if diff != 0]
        #Converts each element in both lists into strings
        for bid in bidList:
            str(bid)
        for diff in finalDiff:
            str(diff)
        
        #Picks the smallest value in the FinalDiff list and 
        #assigns it to a variable
        winningDiff = min(finalDiff)
        #Searches for the index in bidList with the winning
        #difference stored in the winningDiff variable
        Index = bidList.index(winningDiff)
        
        #Generates a print statement based on the index in bidList
        #containing the winningDiff
        #Note: I tried using a loop to condense the code but I
        #kept receiving syntaxErrors that I could not resolve
        if Index == 0:
            print("Congratulations! Your bid of $", end="")
            print(str(B1) + " is the closest to the retail price ", end="")
            print("of $" + str(retailPrice) + "!")
        if Index == 1:
            print("Congratulations! Your bid of $", end="")
            print(str(B2) + " is the closest to the retail price ", end="")
            print("of $" + str(retailPrice) + "!")
        if Index == 2:
            print("Congratulations! Your bid of $", end="")
            print(str(B3) + " is the closest to the retail price ", end="")
            print("of $" + str(retailPrice) + "!")
        if Index == 3:
            print("Congratulations! Your bid of $", end="")
            print(str(B4) + " is the closest to the retail price ", end="")
            print("of $" + str(retailPrice) + "!")
        if Index == 4:
            print("Congratulations! Your bid of $", end="")
            print(str(B5) + " is the closest to the retail price ", end="")
            print("of $" + str(retailPrice) + "!")
        
        
#The user generated inputs for the function                
guess1 = int(input("What is your first guess of the retail price between 1 and 1000?  "))
guess2 = int(input("What is your first guess of the retail price between 1 and 1000?  "))
guess3 = int(input("What is your first guess of the retail price between 1 and 1000?  "))
guess4 = int(input("What is your first guess of the retail price between 1 and 1000?  "))
guess5 = int(input("What is your first guess of the retail price between 1 and 1000?  "))

#The function call
priceIsRight(guess1, guess2, guess3, guess4, guess5)