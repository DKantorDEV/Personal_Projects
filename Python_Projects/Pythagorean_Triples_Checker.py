a = int(input("Enter the first Side: "))          # Get user's input for a side, we will assign it to variable a
b = int(input("Enter the second Side: "))         # Get user's input for a side, we will assign it to variable b
c = int(input("Enter the third Side: "))          # Get user's input for a side, we will assign it to variable c

sides = []                                        # Empty list to store values
sides += [a, b, c]                                # Add the inputs into the list
sides = sorted(sides)                             # Sort the values

if sides[0]**2 + sides[1]**2 == sides[2]**2:      # If the zero index value squared + first index value squared
    print("It is a Pythagorean Triple")           # equals the second index value squared, print that it is a Triple.
else:
    print("It is NOT a Pythagorean Triple")       # Else print it is not