# def greet(name):
#     return None if not name else "hello " + name + "!"


# def arr_check(arr):
#     for item in arr:
#         if type(item) != list:
#             return False
#     return True

# def nth_even(n):
#     return 2 * (n - 1)




def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalnum():  
            count += 1
    return count