"""
Description: Module 05 Functions demonstration
Author: Owen Maxwell
Date: July 4th 2025
Usage: To run individual functions.

"""

# Inititial outline displaying function structure

#def greet():
#    print("Hello, World!")

# Function outlines on powerpoint(pp) page 8 "usage"

# after the parenthesis "-> None" is used, None is where
# you would put what the def would return if applicable
# (string, Integer, Float, Boolean)
#       In later modules, when we learn about objects, 'none' is a 
#        keyword that represents an empty Object that has no value.

def greet()->None: # No Parameter/Input
    """
    Description:
        Prints a greeting message to the console.
    Returns:
        None aka: no value is returned
    Arguments:
        No arguments
    """
    print("Hello, world!")

    # a docstring (""" """) is implemented in the function above to
    # outline its purpose and operation through a description.

# Function will not execute unless it has been called

#greet()

# Function has now been called.

#printing docstring

#print(greet.__doc__)

# bby using .__doc__ the docstring contained inside
# the function is printed in the output

# demo print the docstring of the print function.

#print(print.__doc__)

# A function can have mult parameters by listing them
# within the parenthesis separated by commas.

def greet_name(name: str)->None:
    """
    Prints a greeting which includes
    the value of the name argument.
    Args:
        name (str): The name of the 
        person to greet.
    Returns:
        None
    """
    print(f"Hello, {name}!")

# greet_name testing
# By inputting a name in a string format as an argument
# we can select the name to be printed by the function

#greet_name("Annie")
#greet_name("Bobert")
#greet_name("Lysanderoth, Last of His Name")

# print out greet_name docstring

#print(greet_name.__doc__)

# MULTIPLE ARGUMENTS

def greet_name_age(name: str, age: int)->None:
    """
    Prints a greeting which includes the values
    of the name and age arguments.
    Args:
        name(str): The name of the person to greet.
        age(int): The age of the person to greet.
    Returns:
        None
    """
    print(f"Hello, {name}, you are {age} years old!")

#greet_name_age("Annie", 20)

# RETURN VALUES

# after the arguements we have '-> float' as that is the
# data type that the result of the operation will be.

def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns the result of the specified operation
    based om the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Returns:
        result(float): result of the specified operation 
        based on the two operands.
    """
    if operation == "+":
        result = operand1 + operand2
    if operation == "-":
        result = operand1 - operand2
    # by simply returning the value nothing will happen,
    # we still need to catch the result.
    return result

# first we have to catch the result, then use it.
result = math_operation(5,5,'+') # catch
#print(f"the result is {result}") # use

result = math_operation(5,2,'-')
#print(f"the result is {result}")


# Raising Exceptions

def math_operation_exception(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns the result of the specified operation
    based om the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Returns:
        result(float): result of the specified operation 
        based on the two operands.
    Raises:
        ValueError: "Invalid operation." When op is not '+' or '-'.
    """
    try:
        if operation == "+":
            result = operand1 + operand2
        
        elif operation == "-":
            result = operand1 - operand2
        else:
        # manually raising an exception for invalid operation.
            raise ValueError("Invalid operation.")
    except ValueError as e:
            print("Error: ", e)
    return result

# Knowing that math_operation_exception can potentially raise an exception,
# all calls to it should be enclose in try-except blocks.

# an alternative way to call with try-except
"""
try:
    print(math_operation_exception(20,2,"%"))
except ValueError as e:
    print("Mismatch operator,", e)
"""
# math_operation_exception docstring
#print(math_operation_exception.__doc__)

# operaton functions properly since it uses 
# '+' as its arguement.

#result = math_operation_exception(5,5,'+') # catch
#print(f"the result is {result}") # use

# operation will raise an exception since
# '*' is an invalid arguement.

#result = math_operation_exception(5,2,'*')
#print(f"the result is {result}")


# DEFAULT PARAMETER VALUES

def math_operation_defaultval(operand1: int, operand2: int, operation: str = '+') -> float:
    """
    Returns the result of the specified operation
    based om the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform, default = '+'
    Returns:
        result(float): result of the specified operation 
        based on the two operands.
    Raises:
        ValueError: "Invalid operation." When op is not '+' or '-'.
    """
    try:
        if operation == "+":
            result = operand1 + operand2
        
        elif operation == "-":
            result = operand1 - operand2
        else:
        # manually raising an exception for invalid operation.
            raise ValueError("Invalid operation.")
    except ValueError as e:
            print("Error: ", e)
    return result

# use math_operation_defaultval without providing an operation value
"""
try:
    print(math_operation_defaultval(55,88))
except ValueError as e:
    print(e)
"""