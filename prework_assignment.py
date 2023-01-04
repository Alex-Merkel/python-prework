# Question 1 (Write a function to print "hello_USERNAME!"):
def hello_name(user_name):
    """Print "hello_USERNAME!" with USERNAME as input."""
    print("\nhello_" + user_name.upper() + "!")

hello_name("user")


# Question 2 (A function first_odds that prints the odd numbers from 1-100):
def first_odds():
    """Prints the odd numbers from 1-100 without returning."""
    # Could also do "100" instead of "101" below, but wanted to check 100 to "see" if odd.
    odd_num = range(1,101,2)
    for num in odd_num:
        print(num)

first_odds()


# Question 3 (Please write a Python function, max_num_in_list):
def max_num_in_list(a_list):
    """Returns the max number of a given list."""
    max_num = max(a_list)
    return max_num

print(max_num_in_list([1,7,105,2341,6,145]))


# Question 4(A function to return if the given year is a leap year):
def is_leap_year(a_year):
    """Return "True" if given year is a leap year."""
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False
print(is_leap_year(1900))
        

# Question 5(Check to see if all numbers in list are consecutive):
def is_consecutive(a_list):
    """Check a list to see if the numbers are consecutive or not."""
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False

print(is_consecutive([7, 3, 5, 6, 4]))
