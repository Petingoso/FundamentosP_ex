def remove_multiplos(list, number):
    updatedList = []
    for i in list:
        if i%number!=0:
            updatedList.append(i)
    
    return updatedList

print(remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3))