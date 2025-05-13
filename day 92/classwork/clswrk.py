# def reverse_words(text):
#     words = text.strip().split()
#     reversed_words = words[::-1]
#     return ' '.join(reversed_words)


# def reverse_words(text):
#     words = text.split()
#     reversed_words = []
#     for i in range(len(words) - 1, -1, -1):
#         reversed_words.append(words[i])
#     return ' '.join(reversed_words)


# def even_chars(st):
#     if len(st) < 2 or len(st) > 100:
#         return "invalid string"
#     return [st[i] for i in range(1, len(st), 2)]


# def count_red_beads(n):
#     if n<2:
#         return 0
#     red_beads=n-1
#     total_red=red_beads*2
#     return total_red




# server eroors migdebs ar mishvebs






def even_fib(n):
    a, b=0,1
    total=0
    
    while a <n:
        if a % 2 ==0:
            total+=a
        a, b= b, a+b
    return total