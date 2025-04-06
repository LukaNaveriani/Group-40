def abbrev_name(name):
    name_split=name.split()
    first_letter=name_split[0][0].upper()
    second_letter=name_split[1][0].upper()
    
    letters=first_letter+"."+second_letter
    
    return letters
    

    # # def sum_array(a):
    # sum=0
    # for i in a:
    #     sum+=i
    # return sum


#     def count_sheeps(array_of_sheep):
#   count = 0
#   for sheep in array_of_sheep:
#       if sheep:
#           count += 1 
#   return count

# def summation(num):
#     return num * (num + 1) // 2

# def hero(bullets, dragons):
#      return bullets >= dragons * 2