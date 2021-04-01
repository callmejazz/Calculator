# The most basic of basic calculators....nice

# adding function
def add(number1, number2):
    return number1 + number2


# minus function
def minus(number1, number2):
    return number1 - number2


# multiply function
def multiply(number1, number2):
    return number1 * number2


# divide function
def divide(number1, number2):
    return number1 / number2


# while True:
#     char = input("Enter q to Quit: ")
#
#     if char.lower() == 'q':
#         break

print("Please pick two numbers, but don't get too crazy -\n"
          "1. add\n"
          "2. minus\n"
          "3. multiply\n"
          "4.divide")

select = int(input("Select between 1, 2, 3, 4,: "))

numberSelection1 = float(input("Enter a number: "))
numberSelection2 = float(input("Enter another number, things are about to get crazy: "))

if select == 1:
    print(numberSelection1, "+", numberSelection2, "=", add(numberSelection1, numberSelection2))
elif select == 2:
    print(numberSelection1, "-", numberSelection2, "=", minus(numberSelection1, numberSelection2))
elif select == 3:
    print(numberSelection1, "*", numberSelection2, "=", multiply(numberSelection1, numberSelection2))
elif select == 4:
    if numberSelection2 != 0:
        print(numberSelection1, "/", numberSelection2, "=", divide(numberSelection1, numberSelection2))
    else:
        print("Cannot divide by 0")
else:
    print("Invalid input")

    # q = input('do you want to continue?: ')
    # if quit = 'q':
    # break

    # try:
    #     print(numberSelection1, "/", numberSelection2, "=", divide(numberSelection1, numberSelection2))
    # expect ZeroDivisionError:
    # print("Cannot divide by 0")
