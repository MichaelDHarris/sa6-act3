list1 = [1,2,3,4,5,6]
list2 = [2,4,6,8,10,12]
intersection = list(filter(lambda x:x in list2, list1))
print(intersection)