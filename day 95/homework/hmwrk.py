# def is_opposite(s1, s2):
#     return s1 != "" and s1.swapcase() == s2



# def vaporcode(s):
#     s=s.upper()
#     l=[]
#     s=s.replace(" ","")
#     for i in s:
#         l.append(i)
#     return "  ".join(l)






# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2!=0:
#             return i
        

def find_next_square(sq):
    root = int(sq ** 0.5)
    if root * root == sq:
        return (root + 1) ** 2
    else:
        return -1
