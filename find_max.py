
def find_max(listofnum, func = lambda a, b: b if a < b else a):
    maxnum = 0
    for num in listofnum:
        maxnum = func(maxnum, num)
    print(maxnum)
test = [1,10,3,6,2,9,5]
find_max(test)