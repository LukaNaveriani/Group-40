# 1) ცვლადის განმარტება
# ცვლადი არის მეხსიერების უჯრედი, რომელსაც აქვს სახელი და მასში შეგვიძლია მონაცემების შენახვა.

# 2) ცვლადის განახლება 4-ჯერ
x = 10
x = 20
x = 30
x = 40
print(x)  # ბოლოს x = 40

# 3) შეცდომა ცვლადის სახელთან დაკავშირებით
# 1number = 5  # SyntaxError: invalid syntax
# ცვლადის სახელი არ შეიძლება იწყებოდეს ციფრით.

# 4) მონაცემთა ტიპები
# Integer (int) - მთელი რიცხვი (მაგ: 5)
# Float (float) - ათწილადი რიცხვი (მაგ: 3.14)
# String (str) - ტექსტი (მაგ: "Hello")
# Boolean (bool) - ჭეშმარიტი ან მცდარი (True/False)

# 5) ცვლადები სახელისთვის, გვარისთვის, ასაკისთვის
name = "გიორგი"
surname = "კობახიძე"
age = 25
print(name, surname, "არის", age, "წლის")

# 6) სხვადასხვა ტიპის ცვლადები და მათი ტიპის გამოთვლა
num = 10  # int
decimal = 10.5  # float
text = "Hello"  # str
print(type(num), type(decimal), type(text))

# 7) type() ფუნქცია
# type() აბრუნებს ცვლადის მონაცემთა ტიპს.

# 8) მომხმარებლის შეყვანილი ტექსტი
user_input = input("შეიყვანე ტექსტი: ")
print("შენ შეიყვანე:", user_input)

# 9) მომხმარებლის სახელის, გვარის და ასაკის შეყვანა
user_name = input("შეიყვანე შენი სახელი: ")
user_surname = input("შეიყვანე შენი გვარი: ")
user_age = input("შეიყვანე შენი ასაკი: ")
print(user_name, user_surname, "არის", user_age, "წლის")

# 10) მონაცემთა ტიპების გარდაქმნა
# int -> str: str(10)
# str -> int: int("10")
# float -> int: int(10.5)

# 11) მომხმარებლის სახელი შეადარე ჩემსას
user_name = input("შეიყვანე შენი სახელი: ")
if user_name == name:
    print("ჩვენ ერთი სახელი გვაქვს!")
else:
    print("ჩვენი სახელები განსხვავებულია")

# 12) ლოგიკური ოპერატორები
# and - ორივე პირობა უნდა იყოს True
# or - საკმარისია ერთ-ერთი პირობა იყოს True
# not - აბრუნებს საპირისპიროს

# 13) მომხმარებლის სახელი ან გვარი შეადარე
if user_name == name or user_surname == surname:
    print("მომხმარებლის სახელი ან გვარი ემთხვევა ჩემისას")

# 14) მათემატიკური ოპერატორები
print(5 + 3, 10 - 2, 15 / 3, 4 * 2, 10 % 3)

# 15) მომხმარებლის შეყვანილი რიცხვების შედარება
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
if num1 > num2:
    print("პირველი მეტია")
elif num1 < num2:
    print("მეორე მეტია")
else:
    print("რიცხვები ტოლია")

# 16) მომხმარებლის სახელი შებრუნებით (for-ით)
reversed_name = ""
for char in user_name:
    reversed_name = char + reversed_name
print(reversed_name)

# 17) პირობითი ოპერატორები
# if, elif, else - გადაწყვეტილების მიღებისთვის

# 18) ასაკის შემოწმება
user_age = int(input("შეიყვანე შენი ასაკი: "))
if user_age >= 18:
    print("თქვენ ხართ სრულწლოვანი")
elif 0 <= user_age < 18:
    print("თქვენ ხართ არასრულწლოვანი")
else:
    print("სისტემაში ხარვეზია")

# 19) სახელის ასოების რაოდენობის შედარება
user_name_length = 0
for char in user_name:
    user_name_length += 1

my_name_length = 6  # გიორგის 6 ასო აქვს
if user_name_length == my_name_length:
    print("თქვენს და ჩემს სახელს ერთნაირი სიგრძე აქვს")
else:
    print("კარგი სახელია!")

# 20) რიცხვის ლუწ-კენტი
num = int(input("შეიყვანე რიცხვი: "))
if num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")

# 21) მარტივი კალკულატორი
operation = input("აირჩიე მოქმედება (+, -, *, /): ")
num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("არასწორი ოპერაცია")

# 22) აკადემიის შემოწმება
academy = input("რომელ აკადემიაში სწავლობ? ")
if academy.lower() == "goa":
    print("შენ ნამდვილი ჩადი და პროგრამისტი ხარ!")
else:
    print("შემოუერთდი GOA-ს!")

# 23) მისალოცი შეტყობინება
name = input("შეიყვანე შენი სახელი: ")
print("მოგესალმები,", name, "!")

# 24) მართკუთხედის ფართობი
width = float(input("შეიყვანე სიგანე: "))
height = float(input("შეიყვანე სიმაღლე: "))
area = width * height
print("მართკუთხედის ფართობი არის:", area)
