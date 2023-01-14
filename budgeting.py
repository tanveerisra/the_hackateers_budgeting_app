 # getting food budget
foodBudget = input("Please set a budget for food: ")
foodBudgetFloat = float(foodBudget)

# getting entertainment budget
entBudget = input("Please set a budget for entertainment: ")
entBudgetFloat = float(entBudget)

# getting transportation budget
transBudget = input("Please set a budget for transportation: ")
transBudgetFloat = float(transBudget)


# initializing variables
foodSpending = 0
entSpending = 0
transSpending = 0

# getting user input 
spent = input("Please input a purchase amount. If you have entered all your purchases, enter '0': ")
spentFloat = float(spent)

# checking if spent is 0
while spentFloat != 0: 

    cat = input("What category is this purchase for? ")
    category = cat.lower()

    if category == "food":
        foodSpending = foodSpending + spentFloat
        

    elif category == "entertainment":
        entSpending = entSpending + spentFloat
        

    elif category == "transportation":
        transSpending = transSpending + spentFloat

    else: 
        print("Invalid category. Purchase not logged.")
        

    spent = input("Please input a purchase amount. If you have entered all your purchases, enter '0': ")
    spentFloat = float(spent)

# Getting total spending
totalSpending = foodSpending + entSpending + transSpending
print("This is how much you have spent in total", totalSpending)

# food spending
print("This is how much you have spent on food", foodSpending)
if foodSpending < foodBudgetFloat:
    print("Food spending was under budget by ", foodBudgetFloat-foodSpending)
else :
    print("Food spending was over budget by ", foodSpending-foodBudgetFloat)
    
# entertainment spending
print("This is how much you have spent on entertainment", entSpending)
if entSpending < entBudgetFloat:
    print("Entertainment spending was under budget by ", entBudgetFloat-entSpending)
else :
    print("Entertainment spending was over budget by ", entSpending-entBudgetFloat)    

# transportation spending
print("This is how much you have spent on transportation", transSpending)
if transSpending < transBudgetFloat:
    print("Transportation spending was under budget by ", transBudgetFloat-transSpending)
else :
    print("Transportation spending was over budget by ", transSpending-transBudgetFloat)


