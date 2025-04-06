def dont_give_me_five(start,end):
    result = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            result += 1
    return result


# # def small_enough(array, limit):
#     for x in array:
#         if x > limit:
#             return False
#     return True


# def add_length(s):
#     words = s.split()
#     result = []
#     for word in words:
#         result.append(word + ' ' + str(len(word)))
#     return result


# ori magaliti ertaniti chaagdo




def sum_mix(arr):
    total = 0
    for element in arr:
        if str(element).isdigit():
            total += int(element)
        else:
            try:
                total += int(element)
            except:
                return total
    return total
