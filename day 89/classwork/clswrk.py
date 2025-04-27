# def digital_root(n):
#     n=str(n)
#     sum=0
#     for i in n:
#         sum+=int(i)
#         if len(str(sum))>1:
#             sum=int(str(sum)[0]) + int(str(sum)[-1])
#     return sum




# def format_poem(poem):
#     poem=poem.split('. ')
#     result=".\n".join(poem)
#     return result


def shortest_steps_to_num(num):
    current_numbers = [(1, 0)]  
    visited = set()  

    while current_numbers:
        current, steps = current_numbers.pop(0)

        if current == num:
            return steps
        
        if current < num and current not in visited:
            visited.add(current)
            current_numbers.append((current + 1, steps + 1))
            current_numbers.append((current * 2, steps + 1))
            