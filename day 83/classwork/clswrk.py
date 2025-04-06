def greet():
    return "hello world!"


def make_upper_case(s):
    return s.upper()



def repeat_str(repeat, string):
    return string * repeat



def no_space(s):
    return s.replace(" ", "")


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1  
    return res


def maps(a):
    return [char * 2 for char in a ]


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"


def grader(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'



websites = ['codewars'] * 1000
