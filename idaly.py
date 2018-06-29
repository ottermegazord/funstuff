#
# list = ['a', 'b', 'c', 'd', 'a', 'a', 'j', 'j']
# a = list.reverse()
# dict = {}
#
# while(len(list)):
#
#     print(list)
#     target = list[0]
#     dict[target] = 1
#     list.remove(target)
#     print(len(list))
#
#     for i in range(0, len(list)):
#         if (list[i] == target):
#             dict[target] = dict[target] + 1
#
#     for j in range (1, dict[target]):
#         list.remove(target)
#
# print(dict)


array = ['a', 'c', 'j', 'k', 'a', 'k']

output = {}

while (len(array)):
    alpha = array[0]
    output[alpha] = 1 # counter
    array.remove(alpha)
    print(output)

    for i in range (0, len(array)):
        if array[i] == alpha:
            output[alpha] = output[alpha] + 1

    for j in range(1, output[alpha]):
        array.remove(alpha)

print(output)







