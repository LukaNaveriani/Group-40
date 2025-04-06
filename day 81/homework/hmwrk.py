def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"

# def century(year):
#     return (year + 99) // 100


# def no_space(s):
#     return s.replace(" ", "")


def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    
    if age == 0:
        return "You were born this very year!"
    elif age > 0:
        if age == 1:
            return "You are 1 year old."
        else:
            return "You are " + str(age) + " years old."
    else:
        if age == -1:
            return "You will be born in 1 year."
        else:
            return "You will be born in " + str(-age) + " years."
