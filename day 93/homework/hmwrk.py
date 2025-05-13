# def check(seq, elem):
#     return elem in seq


# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse=True)))


# def is_pangram(s):
#     s = s.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return all(letter in s for letter in alphabet)


# def get_domain_name(url):
#     parsed_url = url
#     domain = parsed_url.netloc.split('.')[0]
    
#     if domain.startswith('www'):
#         domain = domain[4:]
    
#     return domain


# def dating_range(age):
#     if age <= 14:
#         min_age = age - 3
#         max_age = age + 3
#     else:
#         min_age = age // 2 + 7
#         max_age = 2 * (age - 7)
#     return str(min_age) + "-" + str(max_age)


# def julies_age(x, y):
#     brother_age = x / (1 - y)
#     julie_age = brother_age + x
#     return julie_age


# def count_zeros(n):
#     count = 0
#     for i in range(1, n + 1):
#         count += str(i).count('0')
#     return count



# def remove_vowels(s):
#     vowels = "aeiouAEIOU"
#     return ''.join(char for char in s if char not in vowels)


# def duplicate_encode(word):
#     word_lower = word.lower()
#     return ''.join('(' if word_lower.count(c) == 1 else ')' for c in word_lower)

# def alphabet_position(text):
#     result = []
#     for char in text:
#         lower_char = char.lower()
#         if lower_char.isalpha():
#             position = ord(lower_char) - ord('a') + 1
#             result.append(str(position))
#     return ' '.join(result)


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




