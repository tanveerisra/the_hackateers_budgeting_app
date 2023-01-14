foodBudget = input("Please set a budget for Food: \n")
foodBudgetFloat = float(foodBudget)

entBudget = input("Please set a budget for Entertainment: \n")
entBudgetFloat = float(entBudget)

transportBudget = input("Please set a budget for Transportation: \n")
transportBudgetFloat = float(transportBudget)

#food purchases
foodPurchFloat = 1
foodPurchTotal = 0
valid = False

while foodPurchFloat != 0:

    if valid:
        foodPurchTotal += foodPurchFloat
    foodPurch = input("Please enter all Food purchases, type '0' if you are done: \n")
    try:
        foodPurchFloat = float(foodPurch)
        valid = True
    except:
        print("Invalid input.\n")
        valid = False

#entertainment purchases
entPurchFloat = 1
entPurchTotal = 0
valid = False

while entPurchFloat != 0:

    if valid:
        entPurchTotal += entPurchFloat
    entPurch = input("Please enter all Entertainment purchases, type '0' if you are done: \n")
    try:
        entPurchFloat = float(entPurch)
        valid = True
    except:
        print("Invalid input.\n")
        valid = False

#trasnportation purchases
transportPurchFloat = 1
transportPurchTotal = 0
valid = False

while transportPurchFloat != 0:

    if valid:
        transportPurchTotal += transportPurchFloat
    transportPurch = input("Please enter all Transport purchases, type '0' if you are done: \n")
    try:
        transportPurchFloat = float(transportPurch)
        valid = True
    except:
        print("Invalid input.\n")
        valid = False

print("Food Budget: $%.2f\n" % foodBudgetFloat)
print("Entertainment Budget: $%.2f\n" % entBudgetFloat)
print("Transportation Budget: $%.2f\n" % transportBudgetFloat)

print("Your total for Food purchases is $%.2f\n" % foodPurchTotal)
print("Your total for Entertainment purchases is $%.2f\n" % entPurchTotal)
print("Your total for Transportation purchases $%.2f\n" % transportPurchTotal)

#budget calculations vs purchases
foodDiff = foodBudgetFloat - foodPurchTotal
entDiff = entBudgetFloat - entPurchTotal
transportDiff = transportBudgetFloat - transportPurchTotal

# food stuff
if foodPurchTotal > foodBudgetFloat:
    print("You spent $%.2f over your Food budget.\n" % abs(foodDiff))
elif foodPurchTotal < foodBudgetFloat:
    print("You spent $%.2f under your Food budget.\n" % abs(foodDiff))
elif foodPurchTotal == foodBudgetFloat:
    print("You spent neither above or over your Food budget. Good job!\n")

# entertainment stuff
if entPurchTotal > entBudgetFloat:
    print("You spent $%.2f over your Entertainment budget.\n" % abs(entDiff))
elif entPurchTotal < entBudgetFloat:
    print("You spent $%.2f under your Entertainment budget.\n" % abs(entDiff))
elif entPurchTotal == entBudgetFloat:
    print("You spent neither above or over your Entertainment budget. Good job!\n")

# transport stuff
if transportPurchTotal > transportBudgetFloat:
    print("You spent $%.2f over your Transport budget.\n" % abs(transportDiff))
elif transportPurchTotal < transportBudgetFloat:
    print("You spent $%.2f under your Transport budget.\n" % abs(transportDiff))
elif transportPurchTotal == transportBudgetFloat:
    print("You spent neither above or over your Transport budget. Good job!\n")

