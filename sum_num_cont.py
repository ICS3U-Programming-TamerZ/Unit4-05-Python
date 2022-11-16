#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Nov. 10, 2022
# This program calculates the sum of numbers using
# a continue statement


def main():

    # Initializing sum variables
    sum_string = ""
    sum_int = 0

    # Gets the total amount of numbers to be added
    total_numbers_str = input("Enter the amount of numbers to enter: ")

    # Tries casting the total amount of numbers to an integer
    try:
        total_numbers_int = int(total_numbers_str)

    # Exception thrown if the total number is not an integer
    except:
        print("You must enter a positive integer.")
        input("Please restart.")

    if total_numbers_int > 0:
        # Loop executed if the total number is greater than 0
        while total_numbers_int > 0:
            # Gets the user's number
            user_number_str = input("Enter a number to add to the sum: ")
            print("\n")

            # Casts user's number to an integer
            try:
                user_number_int = int(user_number_str)
            except:
                print("You must enter a valid number.\n")
                continue
            else:

                # If there is only one number left
                if total_numbers_int == 1:

                    # Tells the user the number added to the sum
                    print(f"Added {user_number_int} to the sum\n")

                    # Adds the user's number to the string
                    sum_string += user_number_str

                    # Prints equation
                    print(f"{sum_string}\n")

                    # Adds the integer form of the number to the sum
                    sum_int += user_number_int

                    # Decrements the amount of remaining numbers
                    total_numbers_int -= 1

                    continue

                elif user_number_int == 0:
                    # Tells the user the number added to the sum
                    print(f"Added 0 to the sum\n")
                    continue

                elif user_number_int < 0:
                    # Tells the user the number added to the sum
                    print("You must enter a positive number.")
                    continue

                # For numbers greater than 0 and 1
                else:

                    # Tells the user the number added to the sum
                    print(f"Added {user_number_int} to the sum\n")

                    # Adds the user's number to the string
                    sum_string += user_number_str + "+"

                    # Prints equation
                    print(f"{sum_string}\n")

                    # Adds the integer form of the number to the sum
                    sum_int += user_number_int

                    # Decrements the amount of remaining numbers
                    total_numbers_int -= 1

                    continue
    else:
        print("You must input more than 0 numbers to enter\n")
        input("Please restart")

    print("==========")
    print(f"{sum_string} = {sum_int}")
    print(f"Sum = {sum_int}")


if __name__ == "__main__":
    main()
