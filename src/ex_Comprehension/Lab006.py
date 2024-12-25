# square_dict = dict()
# for num in range(1,11):
#     square_dict[num] = num*num
# print(square_dict)
#
# square_dict = {num: num*num for num in range(1,11)}
# print(square_dict)

# old_price = {'coffee':1.02, 'milk':2.5, 'butter':2.5}
# dollar_to_pounds = 0.76
# new_price = {items:value*dollar_to_pounds for (items,value) in old_price.items()}
# print(new_price)

# original_dict = {'jack':22, 'michael':43, 'jhon':24, 'guido':47}
# even_dict = {k:v for (k,v) in original_dict.items() if v % 2 == 0}
# print(even_dict)

# original_dict = {'jack':22, 'michael':33, 'jhon':24, 'guido':47}
# even_dict = {k:v for (k,v) in original_dict.items() if v % 2 != 0 if v < 40}
# print(even_dict)

# original_dict = {'jack':22, 'michael':33, 'jhon':24, 'guido':47}
# even_dict1 = {k:("Old" if v > 40 else "Young")
#               for(k,v) in original_dict.items()}
# print(even_dict1)

# dictionary = {
#     k1:{k2:k1*k2 for k2 in range(1,6)} for k1 in range(2,5)
# }
# print(dictionary)

# dictionary = dict()
# for k1 in range(11,16):
#     dictionary[k1] = {k2:k1*k2 for k2 in range(1,6)}
# print(dictionary)

dictionary = dict()
for k1 in range(11,16):
    dictionary[k1] = dict()
    for k2 in range(1,6):
        dictionary[k1][k2] = k1*k2
print(dictionary)