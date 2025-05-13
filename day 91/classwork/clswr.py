# def remove_duplicates(arr):
#     seen = set()
#     result = []
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result


# def to_alien_english(text):
#     translation = []
#     for char in text:
#         if char == 'a':
#             translation.append('o')
#         elif char == 'o':
#             translation.append('u')
#         else:
#             translation.append(char)
#     return ''.join(translation)



names = ["slavdiki", "nino", "ana", "luka", "mariam", "elene"]

sorted_names = sorted(names, key=len, reverse=True)

print(sorted_names)
