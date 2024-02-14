from functools import reduce
number = 1234
number = str(number)
chars = []
for char in number:
    char = int(char)
    chars.append(char)
sum_of_nums = reduce(lambda x, y: x + y, chars)
print(sum_of_nums)