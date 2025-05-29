# def pig_it(text):
#     words = text.split()
#     result = []
#     for word in words:
#         if word.isalpha():
#             result.append(word[1:] + word[0] + "ay")
#         else:
#             result.append(word)
#     return " ".join(result)


def digital_root(n):
    n=str(n)
    sum=0
    for i in n:
        sum+=int(i)
        if len(str(sum))>1:
            sum=int(str(sum)[0]) + int(str(sum)[-1])
    return sum