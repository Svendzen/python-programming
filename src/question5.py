# Declaring three variables as empty lists
# These will store positive numbers, negative numbers and zeros respectively
positives, negatives, zeroes = [], [], []


def request_integer():
    """
    Takes integer inputs from the user and adds the number
    to a list of positives, negatives or zeroes
    """
    while True:
        user_input = input("Enter an integer (blank to quit): ")
        if user_input.strip() == "":  # both empty string and space will work because of strip()
            break  # break because we want our loop to stop here and not run the rest of the code
        try:
            # try to convert to int
            user_input = int(user_input)

            # if positive number
            if user_input > 0:
                positives.append(user_input)
            # if negative number
            elif user_input < 0:
                negatives.append(user_input)
            # else it must be a zero
            else:
                zeroes.append(user_input)
        except ValueError:
            # handle error if an int was not provided
            print("Only positive and negative numbers are allowed.")


def display_integers():
    """
    Displays all integers in the order of positives, zeroes, then negatives.
    The numbers remain in the order they were entered in each group.
    """
    number_string = ""  # all the numbers gets appended to this string
    for p in positives:
        number_string += str(p) + " "
    for z in zeroes:
        number_string += str(z) + " "
    for n in negatives:
        number_string += str(n) + " "
    print("The numbers were:\n", number_string)     # then printed out in order


request_integer()
display_integers()
