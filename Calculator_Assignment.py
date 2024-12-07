def arithmetic_calculation():

    first_number = float (input('input the first number you want to calculate: '))
    second_number = float (input ('input the second number you want to calculate: '))
    symbol = input ('input the aritmetic symbol of the operation you wish to perform: ')

    if symbol == '+':
        added = first_number + second_number
        return added
    elif symbol == '-':
        subtracted = first_number - second_number
        return subtracted
    elif symbol == '*':
        multiplied = first_number * second_number
        return multiplied
    elif symbol == '/':
        if second_number == 0:
            return "Maths error! Can not divide by Zero"
        divided = first_number / second_number
        return divided
    else:
        return "Error! there is a problem, check your numbers and symbol again"

# rounded my answers to 2 decimal places
print(round(arithmetic_calculation(),2))


