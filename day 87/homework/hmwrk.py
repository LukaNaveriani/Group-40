# def get_drink_by_profession(param):
#     param = param.lower()
    
#     if param == "jabroni":
#         return "Patron Tequila"
#     elif param == "school counselor":
#         return "Anything with Alcohol"
#     elif param == "programmer":
#         return "Hipster Craft Beer"
#     elif param == "bike gang member":
#         return "Moonshine"
#     elif param == "politician":
#         return "Your tax dollars"
#     elif param == "rapper":
#         return "Cristal"
#     else:
#         return "Beer"



# def square_sum(numbers):
#     sum=0
#     for i in numbers:
#         sum+=i**2
#     return sum


# def cookie(x):
#     if isinstance(x, str):
#         return "Who ate the last cookie? It was Zach!"
#     elif isinstance(x, ( float)):
#         return "Who ate the last cookie? It was Monica!"
#     else:
#         return "Who ate the last cookie? It was the dog!"



# def count_char_occurrences(s, char):
#     return s.count(char)





def string_clean(s):
    return ''.join([char for char in s if not char.isdigit()])