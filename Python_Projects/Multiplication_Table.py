def get_table_size():
    """Ensures user provides valid values"""
    while True:
        try:
            size = int(input("Enter the size of the table: "))
            if size > 0:
                return size
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid Input! Please enter a whole number!")

# ---------------------------------------------------------------------------------------------------------------------

def display_table(size):
    """Handles the alignment/display/printing of the table"""
    print("\n" + "----", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print("\n" + "--" * (size * 4 + 4))

    for row in range(1, size + 1):
        print(f"{row:2} |", end="")
        for col in range (1, size + 1):
            print(f"{row * col:4}", end="")
        print()

# ---------------------------------------------------------------------------------------------------------------------

def main():
    print("\n-------- Multiplication Table --------\n")
    size = get_table_size()
    display_table(size)

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()