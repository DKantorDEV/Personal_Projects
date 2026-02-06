import math

weight_choice = input("Would you like to input the weight as Grams or Pounds? ").lower()

if weight_choice in ["grams", "gram", "g"]:

    PENNY_VALUE_PER_G = 0.004
    NICKEL_VALUE_PER_G = 0.01
    DIME_VALUE_PER_G = 0.04409
    QUARTER_VALUE_PER_G = 0.04409

    penny_weight_g = float(input("How many grams in pennies do you have? "))
    nickel_weight_g = float(input("How many grams in nickels do you have? "))
    dime_weight_g = float(input("How many grams in dimes do you have? "))
    quarter_weight_g = float(input("How many grams in quarters do you have? "))

    print("\n-------- Calculating --------\n")

    penny_value_g = penny_weight_g * PENNY_VALUE_PER_G
    nickel_value_g = nickel_weight_g * NICKEL_VALUE_PER_G
    dime_value_g = dime_weight_g * DIME_VALUE_PER_G
    quarter_value_g = quarter_weight_g * QUARTER_VALUE_PER_G
    total_in_g = penny_value_g + nickel_value_g + dime_value_g + quarter_value_g
    total_coins_g = int((penny_value_g / 0.01) + (nickel_value_g / 0.05) + (dime_value_g / 0.1) + (quarter_value_g / 0.25))

    print(f"You have ${penny_value_g:.2f} in pennies")
    print(f"You have ${nickel_value_g:.2f} in nickels")
    print(f"You have ${dime_value_g:.2f} in dimes")
    print(f"You have ${quarter_value_g:.2f} in quarters")
    print(f"Your total is ${total_in_g:.2f}")
    print(f"That's about {total_coins_g} coins!")


elif weight_choice in ["pounds", "pound", "lbs", "lb"]:

    PENNY_VALUE_PER_LB = 1.8144
    NICKEL_VALUE_PER_LB = 4.5359
    DIME_VALUE_PER_LB = 19.999
    QUARTER_VALUE_PER_LB = 19.999

    penny_weight_lb = float(input("How many lbs in pennies do you have? "))
    nickel_weight_lb = float(input("How many lbs in nickels do you have? "))
    dime_weight_lb = float(input("How many lbs in dimes do you have? "))
    quarter_weight_lb = float(input("How many lbs in quarters do you have? "))

    print("\n-------- Calculating --------\n")

    penny_value_lb = penny_weight_lb * PENNY_VALUE_PER_LB
    nickel_value_lb = nickel_weight_lb * NICKEL_VALUE_PER_LB
    dime_value_lb = dime_weight_lb * DIME_VALUE_PER_LB
    quarter_value_lb = quarter_weight_lb * QUARTER_VALUE_PER_LB
    total_in_lb = penny_value_lb + nickel_value_lb + dime_value_lb + quarter_value_lb
    total_coins_lb = int((penny_value_lb / 0.01) + (nickel_value_lb / 0.05) + (dime_value_lb / 0.1) + (quarter_value_lb / 0.25))

    print(f"You have ${penny_value_lb:.2f} in pennies")
    print(f"You have ${nickel_value_lb:.2f} in nickels")
    print(f"You have ${dime_value_lb:.2f} in dimes")
    print(f"You have ${quarter_value_lb:.2f} in quarters")
    print(f"Your total is ${total_in_lb:.2f}")
    print(f"That's about {total_coins_lb} coins!")

else:
    print("\nThat was not a valid response to the question.")




# How many coins they have and estimated total value.
# Round all # printed out to the nearest whole number.