# def better_than_average(class_points, your_points):
#     total = 0
#     count = 0
#     for score in class_points:
#         total += score
#         count += 1
#     total += your_points
#     count += 1
#     average = total / count
#     if your_points > average:
#         return True
#     else:
#         return False


# def kata_13_december(lst):
#     result = []
#     for num in lst:
#         if num % 2 != 0:
#             result.append(num)
#     return result




# def divisors(n):
#     result = []
#     for i in range(2, n):
#         if n % i == 0:
#             result.append(i)
#     if result:
#         return result
#     else:
#         return str(n) + " is prime"



def split_pairs(s):
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            result.append(s[i] + s[i+1])
        else:
            result.append(s[i] + '_')
        i += 2
    return result
