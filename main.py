Water = 300
Milk = 200
Coffee = 100
Revenue = 0
Latte_cost = 2.5
Espresso_cost = 1.5
Cappuccino_cost = 3
end = False


# Subtracts the ingredients needed to make a latte from the ingredient's global variable
def make_latte():
    global Water
    Water -= 200
    global Milk
    Milk -= 150
    global Coffee
    Coffee -= 24


# Subtracts the ingredients needed to make an espresso from the ingredient's global variable
def make_espresso():
    global Water
    Water -= 50
    global Coffee
    Coffee -= 18


# Subtracts the ingredients needed to make a cappuccino from the ingredient's global variable
def make_cappuccino():
    global Water
    Water -= 250
    global Milk
    Milk -= 100
    global Coffee
    Coffee -= 24


# Receives input from user and sum everything in dollars
def insert_coin():
    Quarters = int(input("How many quarters?"))
    Dimes = int(input("How many dimes?"))
    Nickels = int(input("How many nickels?"))
    Pennies = int(input("How many pennies?"))
    total_coin = (Quarters * 0.25) + (Dimes * 0.1) + (Nickels * 0.05) + (Pennies * 0.01)
    return total_coin


# Prints the total ingredients the coffee machine has left
def report():
    global Water
    print(f"Water: {Water}ml")
    global Milk
    print(f"Milk: {Milk}ml")
    global Coffee
    print(f"Coffee: {Coffee}g")
    global Revenue
    print(f"Revenue: ${Revenue}")


while not end:
    drink = input("What would you like? (espresso/latte/cappuccino):")
    # Secret code to turn off the machine
    if drink == "off":
        end = True
    if drink == "report":
        report()

    if drink == "latte":
        if Water > 200 and Coffee > 24 and Milk > 150:
            # Calculate if the total coin inserted is larger than the drink cost
            coins_1 = insert_coin()
            if coins_1 > Latte_cost:
                # Calculates total change
                change_1 = round((coins_1 - Latte_cost), 2)
                # Adding the latte price to the total revenue
                Revenue += Latte_cost
                print(f"Here's ${change_1} in change")
                print("Here's your latte :D")
                make_latte()
            else:
                print("Sorry, that's not enough Revenue. Revenue refunded.")
        # Executes if there's not enough ingredients
        elif Water < 200 or Coffee < 24 or Milk < 150:
            if Coffee < 24:
                print("Sorry there is not enough coffee")
            elif Water < 200:
                print("Sorry there is not enough water")
            elif Milk < 150:
                print("Sorry there is not enough milk")

    if drink == "espresso":
        if Water > 50 and Coffee > 18:
            # Calculate if the total coin inserted is larger than the drink cost
            coins_2 = insert_coin()
            if coins_2 > Espresso_cost:
                # Calculates total change
                change_2 = round((coins_2 - Espresso_cost), 2)
                # Adding the espresso price to the total revenue
                Revenue += Espresso_cost
                print(f"Here's ${change_2} in change")
                print("Here's your espresso :D")
                make_espresso()
            else:
                print("Sorry, that's not enough Revenue. Revenue refunded.")
        # Executes if there's not enough ingredients
        elif Water < 50 or Coffee < 18:
            if Water < 50:
                print("Sorry there is not enough water")
            elif Coffee < 18:
                print("Sorry there is not enough coffee")

    if drink == "cappuccino":
        if Water > 250 and Coffee > 24 and Milk > 100:
            # Calculate if the total coin inserted is larger than the drink cost
            coins_3 = insert_coin()
            if coins_3 > Cappuccino_cost:
                change_3 = round((coins_3 - Cappuccino_cost), 2)
                # Adding the cappuccino price to the total revenue
                Revenue += Cappuccino_cost
                print(f"Here's ${change_3} in change")
                print("Here's your cappuccino :D")
                make_cappuccino()

            else:
                print("Sorry, that's not enough Revenue. Revenue refunded.")
        # Executes if there's not enough ingredients
        elif Water < 250 or Coffee < 24 or Milk < 100:
            if Water < 250:
                print("Sorry there is not enough water")
            elif Coffee < 24:
                print("Sorry there is not enough coffee")
            elif Milk < 100:
                print("Sorry there is not enough milk")

