try:
    number = input("Enter a number: ")
    if(int(number) %2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
except TypeError:
    print("AssertionError: more than one argument is provided")
except ValueError:
    print("AssertionError: argument is not an integer")