
DIGITS = "0123456789ABCDEF"

def get_valid_base(prompt_to_user):
    while True:
        try:
            base = int(input(prompt_to_user))
            if 16 >= base >= 2:
                return base
            print("Please pick a base (2- 16): ")
        except ValueError:
            print("Invalid. Pick a base from 2 to 16.")

# -------------------------------------------------------------------------------------------------------------------

def get_valid_number(base):
    while True:
        user_number = input("What is your desired number?: ").upper()
        valid_input = True

        for char in user_number:

            if char not in DIGITS:
                break

            if DIGITS.index(char) >= base:
                valid_input = False
                break

        if valid_input:
            return user_number
        else:
            print(f"Invalid number for base {base}!")

# -------------------------------------------------------------------------------------------------------------------

def to_base_10(number_str, source_base):
    """Converts a string number from source_base to decimal (int)."""
    total = 0
    for char in number_str:
        value = DIGITS.index(char)
        total = (total * source_base) + value
    return total

# -------------------------------------------------------------------------------------------------------------------

def from_base_10(number, target_base):
    """Converts a decimal (int) to a string in target_base."""
    if number == 0:
        return "0"

    result_chars = []
    while number > 0:
        remainder = number % target_base
        result_chars.append(DIGITS[remainder])
        number = number // target_base

    # Reverse the list to get the correct order
    return "".join(reversed(result_chars))

# -------------------------------------------------------------------------------------------------------------------

def ask_to_continue():
    """Returns True if the user wants to convert another number."""
    while True:
        choice = input("\nConvert another number? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

# -------------------------------------------------------------------------------------------------------------------

def main():
    print("--- Base Jumper: Number Converter ---")

    while True:
        # 1. Get Inputs
        current_base = get_valid_base("Enter the current base (2-16): ")
        num_str = get_valid_number(current_base)
        target_base = get_valid_base("Enter the target base (2-16): ")

        # 2. Convert to Base 10 (The Hub)
        decimal_val = to_base_10(num_str, current_base)

        # 3. Convert to Target Base (The Spoke)
        final_result = from_base_10(decimal_val, target_base)

        # 4. Display Result
        print("-" * 40)
        print(f"Result: {final_result} (Base {target_base})")
        print("-" * 40)

        if not ask_to_continue():
            print("Exiting program. Goodbye!")
            break

# -------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nUser forced exit.")