def name_length(name):

    # This function will tell you how many letters are in a word

    print('What is your name?')

    # this print statement initiates the interaction between user and program
    # by prompting an input to the question : 'What is your name?'

    name = input()

    # here is the input function awaiting users input.
    # Program will not advance until data is input.
    # The variable 'name' is created with the input from the user
    #  to be stored as a value in said variable 'name'

    print('Hello', name, ',')

    # this print function greets the user by printing 'Hello'
    # and then the input from the 'name' variable
    # and then a comma is printed after the name ending the line
    #  directing the user's eye to the next line.

    if len(name) == 1:

        # the 'if' statement is used to get the word length in numeric form
        # and the proper response for the word 'character' by using the 'len' function.
        # This function counts the length of variable 'name'.
        # The comparison operator ' == ' is used to compare the answer
        # if it is a '1' or not for the proper response and not the assignment operator ' = '

        print(name, 'has', len(name), 'character.')

        # if the 'name' variable equals or is comparable to '1', then this statement here prints

    else:

        print('the name', name, 'has', len(name), 'characters.')

    # if the variable is anything other than '1', otherwise passing the 'if' statement,
    # this else statement will print this phrase for all things else


name_length('')

# the calling of the function 'name_length' will activate the program
# to initiate the function with a query. Since the function has a parameter,
# this one a variable, an argument is needed when you call the function.
# The value of the variable parameter is stored within the function
# so the argument entered when calling the function can vary.
# Here, only quotation marks around a null value is the argument
# and the answer holds true.
