# say_hello is a function that takes variable number of parameters, it's a variadic function
def say_hello(*names):
    # print type of names variadic variable using type() build-in function
    print("names type: ", type(names))   # it's a tuple!
    # declare a variable called formatter_names and
    # assign to it string coming from joining all the variable/s name by coma and a space
    # join is a build-in method to create a string out of a collection
    formatted_names = ", ".join(names)
    # return the formatted string using interpolation
    return f"Hello World! It's {formatted_names}."
