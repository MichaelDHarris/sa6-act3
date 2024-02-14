list_of_str = ['test', 'computer', 'python', 'code']
list_of_str.sort() #get into alphabetical order
list_of_str.sort(key=lambda word: len(word)) #sort on length
print(list_of_str)