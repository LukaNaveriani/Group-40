# def is_isogram(string):
    
#     st_low = string.lower()
#     if string == "":
#         return True
#     for i in st_low :
#         if st_low.count(i) >= 2:
#             return False
#     return True




# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# def vaporcode(s):
#     s=s.upper()
#     l=[]
#     s=s.replace(" ","")
#     for i in s:
#         l.append(i)
#     return "  ".join(l)

def unscramble_eggs(word):
    pattern = "egg"
    result = ""
    i = 0
    while i < len(word):
        if word[i:i+3] == pattern:
            i += 3
        else:
            result += word[i]
            i += 1
    return result