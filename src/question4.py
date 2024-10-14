from random import randint


def generate_random_ints():
    """
    Generate a list of 10 random integers between 1 and 50.
    """
    list_of_ints = []  # start with empty list
    # loop 10 times
    for i in range(10):
        list_of_ints.append(randint(1, 50)) # append number between 1 and 50
    return list_of_ints


# Example use of generate_random_ints()
ints = generate_random_ints()
print(ints)


def substitute(int_list):
    """
    Substitute elements in the given list that are divisible by 5 with their squares.
    """
    # Iterate over the indices of int_list
    for j in range(len(int_list)):
        # if int_list[j] is divisible by 5...
        if int_list[j] % 5 == 0:
            # int_list[j] becomes squared
            int_list[j] = int_list[j] ** 2  # exponentiation operator used for squaring
    return int_list


# Example use of Substitute() using the list of ints from generate_random_ints()
substituted_ints = substitute(ints)
print(substituted_ints)
