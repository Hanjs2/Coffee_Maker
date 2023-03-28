from data import MENU, resources, profit


def resource_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f'Sorry not enough {item}')
            return False
    return True

def coin_check():
    total=int(input('How many quarters?: '))*.25
    total += int(input('How many dimes?: ')) * .10
    total += int(input('How many nickles?: ')) * .05
    total += int(input('How many pennies?: ')) * .01
    return total
def transaction(money_recieved,drink_cost):
    if money_recieved>= drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money")
        return False
def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}!! Enjoy:)")




should_cont = False
while not should_cont:
    def coffee_function():
        user_choice = input("What would you like? Latte, Cappuccino, Espresso?: ").lower()
        if user_choice == "off":
            should_cont = False
        elif user_choice == "report":
            should_cont = True
            print(f"Water:{resources['water']} ml")
            print(f"Milk:{resources['milk']} ml")
            print(f"Coffee:{resources['coffee']} g")
            print(f"Profit:${profit}")
        elif user_choice == 'latte' or user_choice == 'cappuccino' or user_choice == 'espresso':
            drink=MENU[user_choice]
            if resource_check(drink['ingredients']):
                payment = coin_check()
                if transaction(payment, drink["cost"]):
                    make_coffe(user_choice, drink['ingredients'])
        else:
            print("Invalid entry")
            return True

    coffee_function()
    restarter = input('Would you like to make another selection?: y or n ')
    if restarter == 'n':
        print('Enjoy your day')
        should_cont = False
        break

    else:
        coffee_function()
        should_cont = True







