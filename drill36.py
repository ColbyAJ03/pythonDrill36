# The Tech Academy #
#   Python Course  #
#     Drill 36     #
#    Alex Colby    #

from random import randint

# steps 1 - 3
def assignVariables():
    myInt = 5
    myString  = "Hello World!"
    myFloat = 12.345
    printVariables(myInt,myString,myFloat)

# step 4
def printVariables(myInt,myString,myFloat):
    print("\nMy integer is: {}. \nMy float is: {}. \nMy String is: {}".format(myInt,myFloat,myString))
    doMath(myInt,myFloat)

# step 5 (+= to be used later in steps 8-9)
def doMath(myInt,myFloat):
    mathInt = randint(5,40)
    addInt = (myInt + mathInt)
    subInt = (mathInt - myInt)
    multInt = (myInt * mathInt)
    divFloat = (float(mathInt) / float(myInt))
    remInt = (mathInt % myInt)

    # print math results
    print("\n{} + {} = {}".format(myInt,mathInt,addInt))
    print("{} - {} = {}".format(mathInt,myInt,subInt))
    print("{} * {} = {}".format(myInt,mathInt,multInt))
    print("{} / {} = {}".format(mathInt,myInt,divFloat))
    print("The remainder for {} / {} = {}".format(mathInt,myInt,remInt))
    statementOperators(addInt,subInt,multInt,remInt)

# steps 6-7
def statementOperators(addInt,subInt,multInt,remInt):
    if  addInt > 10 and subInt > 10:
        print("Both addition and subtraction results are greater than 10")
    elif addInt > 10 or subInt > 10:
        print("One of the addition or subtraction results is greater than 10")
    else:
        print("Neither the addition or subtraction value is greater than 10")
    if not remInt == 0:
        print("There is a remainder")
    elif remInt == 0:
        print("There is no remainder")
    getLoopy()

# steps 8-9
def getLoopy():
    x = 1
    while x <= 5:
        print(x)
        x += 1 # step 5
    for y in range(1,6):
        print(y)
    createList()

# step 10
def createList():
    myList = ["Five", "Four", "Three", "Two", "One", "Zero"]
    for number in myList:
        print(number)
    createTuple()

# step 11
def createTuple():
    myTuple = (1, "2", 3, "4", 5)
    for value in myTuple:
        print(value)
    printString()

# step 12
def stringReturn():
    randomInt = randint(0,10)           
    myString = "This is a random number between 1 and 10: " + str(randomInt) # chose a method other than .format()
   
    return myString

# step 13
def printString():
    newString = stringReturn()
    print(newString.upper())

# start the program
if __name__ == "__main__":
    assignVariables()
    
