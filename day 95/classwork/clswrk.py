# vowels = ["a", "e", "i", "o", "u"]

# def encode(st):
#     result = ""

#     for char in st:
#         if char in vowels:
#             result += str(vowels.index(char) + 1)
#         else:
#             result += char
    
#     return result

# encoded_str = encode("Hello World")
    
    
# def decode(st):
#     result = ""

#     for char in st:
#         if char.isdigit():
#             result += vowels[int(char) - 1]
#         else:
#             result += char
    
#     return result



# def spin_words(st):
#     st=st.split(" ")
#     result=[]
    
#     for i in st:
#         if len(i)>=5:
#             result.append(i[::-1])
#         else:
#             result.append(i)
#     return " ".join (result)



# def break_camel_case(s):
#     result = ''
#     for char in s:
#         if char.isupper():
#             result += ' ' + char
#         else:
#             result += char
#     return result






def bool_to_word(b):
    return "Yes" if b else "No"