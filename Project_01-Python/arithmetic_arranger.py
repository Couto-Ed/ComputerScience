# Rules function
def check_rules(num1, num2, operator):
    # Only digit exception
    try:
        int(num1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(num2)
    except:
        return "Error: Numbers must only contain digits."
    # More than 4 digit no. exception
    try:
        if len(num1) > 4 or len(num2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    # Operator must be + or - exception.
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""


def arithmetic_arranger(problems, displayMode=False):

    start = True
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    # Too many Problem exception
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    for prob in problems:
        # Splitting the Problem into separate strings
        separated_problem = prob.split()
        # storing number 1
        number1 = separated_problem[0]
        # Storing the operator sign
        operator = separated_problem[1]
        # storing number 2
        number2 = separated_problem[2]
        validation = check_rules(number1, number2, operator)
        if validation != "":
            return validation
        no1 = int(number1)
        no2 = int(number2)
        # space contains the max spaces required
        space = max(len(number1), len(number2))
        # For first arithmetic arragement
        if start == True:
            line1 += number1.rjust(space + 2)
            line2 += operator + ' ' + number2.rjust(space)
            line3 += '-' * (space + 2)
            if displayMode == True:
                if operator == '+':
                    line4 += str(no1 + no2).rjust(space + 2)
                else:
                    line4 += str(no1 - no2).rjust(space + 2)
            start = False
        # Other than first arithmetic arragement
        else:
            line1 += number1.rjust(space + 6)
            line2 += operator.rjust(5) + ' ' + number2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if displayMode == True:
                if operator == '+':
                    line4 += side_space + str(no1 + no2).rjust(space + 2)
                else:
                    line4 += side_space + str(no1 - no2).rjust(space + 2)
    # displayMode is Ture then append line4
    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
    