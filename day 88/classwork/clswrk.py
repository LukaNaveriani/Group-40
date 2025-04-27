# def sum_array(arr):
#     if not arr or len(arr) <=1:
#         return 0
#     total=0
#     highest=arr[0]
#     lowest=arr[0]
    
#     for i in arr:
#         total+=i
#         if i > highest:
#             highest=i
#         if i < lowest:
#             lowest=i
    
#     result=total - highest - lowest
#     return result




def generate_hashtag(s):
    if s =="":
        return False
    s=s.split()
    
    result="#"
    for i in s:
        result+=i.capitalize()
    
    if len(result)>140:
        return False

    return result