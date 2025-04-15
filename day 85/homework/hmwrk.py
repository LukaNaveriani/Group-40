# def addition(numbers):
#     return sum(numbers)




# name = "ლუკა"
# surname = "ნავერიაი"
# age = 25

# print(f"ჩემი სახელია {name}, ჩემი გვარია {surname} და მე ვარ {age} წლის")





# def calculate():
#     num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#     num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
#     operation = input("შეიყვანეთ (+, -, *, /): ")

#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             return "ნულზე გაყოფა არ შეიძლება!"
#     else:
#         return "არასწორი ოპერაცია!"

#     return f"შედეგი არის: {result}"






# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_primes_up_to(n):
#     total = 0
#     for i in range(2, n + 1):
#         if is_prime(i):
#             total += i
#     return total
