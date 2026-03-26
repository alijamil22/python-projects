MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO1:  Ask user which flavour they want?  NOTES: It should display this.  DONE
#TODO2:  Turn off the coffee machine when type 'off'.   DONE
#TODO3:  When user enter report in the prompt choose_flavour then it should output current report
#        like Water 100 g, milk 50 g, coffee 87 g, money: $2.50 DONE
#TODO4:  When user select flavour then it should check if resources are enough to make drink.If any one resource 
#        is depleted then it should print 'Sorry there is not enough water' DONE
#TODO5:  If there are enough resources then it should check for coins. It program ask user to enter coins
#TODO6:  Quarter = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01.
#TODO7:  Calculate the value of coins
#TODO8:  check for enough coins
#           Note create a money variable
#TODO9:  If the coins are not enough then it should print 'Sorry there is not enough water'
#TODO10: But if the user has inserted enough money, then the cost of the drink gets added to the 
#        machine as the profit and this will be reflected the next time “report” is triggered.
#TODO11: If the user has inserted too much money, the machine should offer change.  
#TODO12: If the transaction is successful and there are enough resources to make the drink the 
#        user selected, then the ingredients to make the drink should be deducted from the 
#        coffee machine resources
#TODO13: Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”

# It takes user input and check if they enter report 
profit = 0
def is_enough(resour,ingre):
    for ingredients,required_amount in ingre.items():
        available_amount = resour.get(ingredients,0)
        if available_amount < required_amount:
            print(f"Not enough {ingredients}")
            return False
    return True
def value(quart,dim,nic,pen):
    total = (quart*0.25)+(dim*0.10)+(nic*0.05)+(pen*0.01)
    return total
is_on = True
while is_on:
    choose_flavour = input("What would you like? (espresso/latte/cappuccino)").lower()
    #report
    if choose_flavour == "report":
        print(f" Water: {resources['water']}g \n Milk: {resources['milk']}g \n Coffee: {resources['coffee']}g\n coins: {resources['coins']}")
        
    # if user enter off then stop
    elif choose_flavour == "off":
        is_on = False
    # Check for resources, if one resources depleted stop the process
    elif choose_flavour in MENU:
        m_r_ingredient = MENU[choose_flavour]["ingredients"]
        if is_enough(resources,m_r_ingredient):
            print("You have enough resources")
            print("Please enter coins:")
            quarter = int(input("Please enter quarter"))
            dimes = int(input("Please enter quarter"))
            nickels = int(input("Please enter quarter"))
            Pennies = int(input("Please enter quarter"))
            total_coins_value = value(quarter,dimes,nickels,Pennies)
            if total_coins_value < MENU[choose_flavour]["cost"]:
                print("Sorry not enough coins")
            elif total_coins_value == MENU[choose_flavour]["cost"]:
                profit = total_coins_value
                resources["coins"] = profit
            elif total_coins_value > MENU[choose_flavour]["cost"]:
                remaining = total_coins_value - MENU[choose_flavour]['cost']
                print(f"here is you remaining {remaining}")
        else:
            print("Insufficient resources")
    else:
        print("Invalid choice")
