import math


def change_calculator():

    print("\n------ Change Calculator ------\n")

    money_received = float(input("How much money received: $"))
    total_cost = float(input("How much was the total: $"))
    change_total = int((money_received - total_cost) * 100)

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while change_total >= 1:

        if change_total >= 25:
            change_total -= 25
            quarters += 1
        elif change_total >= 10:
            change_total -= 10
            dimes += 1
        elif change_total >= 5:
            change_total -= 5
            nickels += 1
        elif change_total >= 1:
            change_total -= 1
            pennies += 1
        else:
            break

    print(f"Return {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s) and {pennies} pennie(s).\n")



still_running = True

while still_running:

    change_calculator()
    ask_user = input("Calculate more change? (Y) or (N): ").lower()

    if ask_user == "y":
        still_running = True
    else:
        print("\n------ Exiting Calculator ------")
        still_running = False