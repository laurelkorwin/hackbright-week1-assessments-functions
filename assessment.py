# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def calculate_cost(cost, state, tax=0.05):
    if state == "CA":
        tax = 0.07

    total_cost = cost + cost * tax

    return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

def is_berry(fruit):
    true_fruits = ['strawberry', 'cherry', 'blackberry']

    if fruit.lower() in true_fruits:
        return True
    else:
        return False

#Note: I am assuming that you'd like the function to return false if the fruit is not in the "true" fruits category.
#If not, you could also take out the else statement and just have the function return true if the fruit is in the group,
#and return none if it is not.

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):

    if is_berry(fruit):
        return '0'
    else:
        return '5'

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town_name):
    if town_name == "Los Altos":
        return True
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    full_name = "{} {}".format(first_name, last_name)

    return full_name

#OR - tell me which is better :)


def full_name2(first_name, last_name):
    full_name = first_name + ' ' + last_name

    return full_name

#OR ANOTHER WAY :)


def full_name3(first_name, last_name):
    full_name = ' '.join([first_name, last_name])

    return full_name
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town_name, first_name, last_name):

    full_name = full_name3(first_name, last_name)

    if is_hometown(town_name):
        print "Hi, {}, we're from the same place!".format(full_name)
    else:
        print "Hi, {}, where are you from?".format(full_name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x=1):

    def add(y):
        return x + y

    return add


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

print increment(5)
#When you just do it this way, it's like...WTF, you gave me a function and x but no y.
#OK, I'll print that this is basically function add and it's memory location...but I'm not doing ish until you give me a y value.
addfive = increment(5)
#Now you're saying - addfive is the function add, with x value 5.

print addfive(5)
print addfive(20)
#NOW you're saying ok, I'll give you addfive, and make y = 5 or 20 or whatever you want.


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def add_num(lst, num):
    new_list = lst.append(num)

    return new_list

#####################################################################
