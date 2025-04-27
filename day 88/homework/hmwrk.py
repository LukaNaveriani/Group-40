# def generate_hashtag(s):
#     if s =="":
#         return False
#     s=s.split()
    
#     result="#"
#     for i in s:
#         result+=i.capitalize()
    
#     if len(result)>140:
#         return False

#     return result


# def divide_by_digit_sum(n):
#     digit_sum = sum(int(digit) for digit in str(n))
#     return n / digit_sum if digit_sum != 0 else "Division by zero error"




# def is_perfect_square(n):
#     if n < 0:
#         return False
#     x = 0
#     while x * x < n:
#         x += 1
#     return x * x == n



# def most_frequent_number(lst):
#     frequency = {}
#     for num in lst:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     return max(frequency, key=frequency.get)



# def hide_vowels(word):
#     vowels = "aeiouAEIOU"
#     return ''.join(['*' if char in vowels else char for char in word])



# def is_palindrome(word):
#     reversed_word = ""
#     for char in word:
#         reversed_word = char + reversed_word
#     return word == reversed_word


def to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
