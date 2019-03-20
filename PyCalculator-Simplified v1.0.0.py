print("Welcome To PyCalculator-Simplified Version 1.0.0 Calculator")
print("")
print("")
print("")
print("Please select one of the following numbers for your sum.")
print("")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
sumType = input("")

#addition code
if sumType == "1":
   addFiNumber = int(input("First Number To Add:   "))
   addSeNumber = int(input("Second Number To Add:   "))
   sum = addFiNumber + addSeNumber
   print("The answer to your sum is", sum)
   
#subtraction code 
if sumType == "2":
    takeFiNumber = int(input("First Number To Be Subtracted From:   "))
    takeSeNumber = int(input("Number To Take Away From First Number:   "))
    sum = takeFiNumber - takeSeNumber
    print("The answer to your sum is", sum)
    
#multiplication code
if sumType == "3":
    multFiNumber = int(input("First Number To Be Multiplied By:   "))
    multiSeNumber = int(input("Second Number To Multiply The First Number By:   "))
    sum = multiFiNumber * multiSeNumber 
    print("The answer to your sum is", sum)
    
#division code
if sumType == "4":
    divFiNumber = int(input("First Number To Be Divided From:   "))
    divSeNumber = int(input("Second Number To Divide The First Number By:   "))
    sum = divFiNumber / divSeNumber 
    print("The answer to your sum is", sum)
