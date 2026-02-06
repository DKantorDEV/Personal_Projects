import math

# Initial condition to start the program
calculate_again = True

print("\n------ Mean, Median, Mode Calculator ------\n")


# --- Function Definitions ---

def calculate_mean(mean_list):
    total = sum(mean_list)
    result = total / len(mean_list)
    print(f"The Mean is {result}")


def calculate_median(median_list):
    median_list.sort()
    length_of_list = len(median_list)
    middle_index = length_of_list // 2

    # Logic for Odd vs Even lists
    if length_of_list % 2 != 0:
        median = median_list[middle_index]
    else:
        # Average the two middle numbers
        median = (median_list[middle_index - 1] + median_list[middle_index]) / 2

    print(f"The Median is {median}")


def calculate_mode(mode_list):
    counts = {}
    for num in mode_list:
        counts[num] = counts.get(num, 0) + 1

    highest_freq = max(counts.values())
    modes = [num for num, count in counts.items() if count == highest_freq]

    if len(modes) == len(mode_list):
        print("No mode: All numbers appear only once.")
    else:
        print(f"The mode(s) is {modes}")


# --- Main Program Loop ---

while calculate_again:
    # Get inputs
    user_choice = input("\nDo you want to calculate the Mean, Median or Mode?: ").lower().strip()
    users_numbers = input("Numbers you want to calculate with (Separated by a ','): ")

    # Convert string to list of integers
    try:
        user_list = [int(x.strip()) for x in users_numbers.split(",")]
    except ValueError:
        print("Error: Please only enter numbers separated by commas.")
        continue

    # Execute the chosen function
    if user_choice == "mean":
        calculate_mean(user_list)
    elif user_choice == "median":
        calculate_median(user_list)
    elif user_choice == "mode":
        calculate_mode(user_list)
    else:
        print("That is not a valid option.")

    # Check if user wants to continue
    print("\n-------------------------------------------")
    again_or_exit = input("Do you want to calculate more numbers? (Y/N): ").lower().strip()

    if again_or_exit != "y":
        print("\n------ Exiting Calculator ------")
        calculate_again = False