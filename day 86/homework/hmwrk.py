# def merge_lists(list1, list2):
#     return list1 + list2 


# def remove_vowels(word):
#     vowels = "aeiouAEIOUაეიოუ"
#     result = ""
#     for letter in word:
#         if letter not in vowels:
#             result += letter
#     return result



# def sum_odd_indexes(numbers):
#     total = 0
#     for i in range(1, len(numbers), 2):
#         total += numbers[i]
#     return total



# lst = [1, 2, 3, 2]
# lst.remove(2)

# lst = [10, 20, 30]
# x = lst.pop(1)

# lst = [1, 2, 3]
# lst.insert(1, 70)

# lst = [1, 2]
# lst.append(3)




# def even_odd_merge_sum(list1, list2):
#     evens = [x for x in list1 if x % 2 == 0]
#     odds = [x for x in list2 if x % 2 != 0]
#     merged = evens + odds
#     total = 0
#     for i in range(1, len(merged), 2):
#         total += merged[i]
#     return total




# def short_name(first_name, last_name):
#     return "My name is " + first_name[0] + "." + last_name[0]





name = "Luka"
surname = "Naverioni"
age = 14
height = 168
print("My name is {}, my surname is {}, I am {} years old, and my height is {} centimeters.".format(name, surname, age, height))