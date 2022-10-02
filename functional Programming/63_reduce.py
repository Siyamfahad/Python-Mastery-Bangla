


#The reduce() function accepts a function and a sequence and
#returns a single value calculated



from functools import reduce


letter = ['world']
num = [1,2,3,4,5]

word = reduce(lambda x,y:x+y,num)
print(word)