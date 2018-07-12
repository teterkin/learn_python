try:
    # learn_python = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print("Division by zero.")
    print(error)
    exit(-1)
except ValueError as error:
    print("Invalid input.")
    print(error)
    exit(-1)
print("You entered number: " + str(number))
exit(0)
