# def is_square(n):
#     if n < 0:
#         return False
#     root = int(n**0.5)
#     return root * root == n



#def nicknamegenerator(name):
#     if len(name) < 4:
#         return "Error: Name too short"
#     vowels = "aeiou"
#     if name[2].lower() in vowels:
#         return name[:4]
#     else:
#         return name[:3]


# def list_animals(animals):
#     result = ""
#     for i, animal in enumerate(animals, 1):
#         result += str(i) + ". " + animal + "\n"
#     return result


# def print_triangle():
#     n = int(input("Enter the height of the triangle: "))
#     for i in range(1, n + 1):
#         print('*' * i)


# def to_camel_case(text):
#     st = ""
#     s = ""
#     for i in text:
#         if i == "_" or i == "-":
#             st += i.replace(i," ")
#         else:
#             st += i
#     st = st.split(" ")
#     for i in range(len(st)):
#         if i >= 1:
#             s += st[i].capitalize()
#         elif i == 0:
#             s += st[i]
#     return s