# words = []

# while True:
#     word = input("Enter a word (type 'enough' to stop): ")
#     if word == "enough":
#         break
#     words.append(word)

# sorted_words = sorted(words, key=len)
# print(sorted_words)




# names = ["Nino", "Luka", "Giorgi", "Ana", "Mariam"]
# sorted_names = sorted(names)
# print(sorted_names)




# numbers = [12, 5, 87, 1, 33, 19, 76]
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)



# sorted() არის Python-ის ჩაშენებული ფუნქცია, რომელიც გამოიყენება სიის ან სხვა ტიპის მონაცემის დასალაგებლად.




# def dating_range(age):
#     if age <= 14:
#         min_age = age - 3
#         max_age = age + 3
#     else:
#         min_age = age // 2 + 7
#         max_age = 2 * (age - 7)
#     return str(min_age) + "-" + str(max_age)



# def julies_age(x, y):
#     brother_age = x / (y - 1)
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



def alphabet_position(text):
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            position = ord(lower_char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)
