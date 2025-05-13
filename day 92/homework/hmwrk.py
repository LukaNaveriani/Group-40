# def sort_by_a_count(strings):
#     return sorted(strings, key=lambda s: s.count('a'))




# def sort_by_vowels_count(strings):
#     vowels = "aeiou"
#     return sorted(strings, key=lambda s: sum(1 for char in s if char in vowels), reverse=True)




# def sort_by_length(sentence):
#     return sorted(sentence.split(), key=len, reverse=True)



# def sort_by_threes_count(numbers):
#     return sorted(numbers, key=lambda x: str(x).count('3'), reverse=True)




# def sort_by_g_prefix(strings):
#     return sorted(strings, key=lambda s: s.lower().startswith('g'), reverse=True)



# def narcissistic(value):
#     digits = str(value)
#     num_digits = len(digits)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
#     return sum_of_powers == value



# def expanded_form(num):
#     num_str = str(num) 
#     length = len(num_str)
#     expand=[]

#     for i, digit in enumerate(num_str):
#         if digit != '0': 
#             expand.append(digit + '0' * (length - i - 1))

#     return ' + '.join(expand)


# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return names[0] + " likes this"
#     elif len(names) == 2:
#         return names[0] + " and " + names[1] + " like this"
#     elif len(names) == 3:
#         return names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     else:
#         return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"



def expand_string(s):
    result = []
    temp = ''
    last_num = 0
    
    for char in s:
        if char.isdigit():
            last_num = int(char)
        else:
            if last_num > 0:
                result.append(temp * last_num)
                temp = ''
                last_num = 0
            temp = char
            
    result.append(temp * last_num if last_num > 0 else temp)
    
    return ''.join(result)
