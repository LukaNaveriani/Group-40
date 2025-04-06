def fake_bin(x):
    result = ''
    for i in range(len(x)):
        if int(x[i]) < 5:
            result += '0'
        else:
            result += '1'
    return result

def check(seq, elem):
    return elem in seq


def string_to_array(s):
    if s == "":
        return ['']
    return s.split()

def reverse_seq(n):
    return list(range(n, 0, -1))



# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif (p1 == "rock" and p2 == "scissors") or \
#          (p1 == "scissors" and p2 == "paper") or \
#          (p1 == "paper" and p2 == "rock"):
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"
