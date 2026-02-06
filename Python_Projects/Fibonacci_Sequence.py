def ask_to_continue():
    """Asks if user wants to continue or exit"""
    while True:
        choice = input("Calculate another number? (Y) or (N): ")

        if choice in ["yes", "y", "Y"]:
            return True
        elif choice in ["no", "n", "N"]:
            return False
        else:
            print("Please enter 'Y' for yes or 'N' for no.\n")


# ---------------------------------------------------------------------------------------------------------------------

def valid_int():
    """This validates that the user input falls within the given parameters"""
    while True:
        try:
            n = int(input("\nWhat is the index you want the value of?: "))
            if n >= 0:
                return n
            print("Please enter 0 or higher.")
        except ValueError:
            print("Invalid! Enter a whole number!")

# ---------------------------------------------------------------------------------------------------------------------

def fibonacci_func(n):
    """This calculates the (n)th term's value"""

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0
    prev1 = 1
    current = 0

    for _ in range (2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return current

# ---------------------------------------------------------------------------------------------------------------------

def main():
    print("------ Fibonacci Sequence for (n)th term ------")

    while True:
        index = valid_int()
        result = fibonacci_func(index)

        print(f"The value at index {index} is: {result}")
        print("-" * 30)

        if not ask_to_continue():
            print("\nGoodbye!")
            break


# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nUser forced exit. Goodbye!")