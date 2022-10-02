



#genarators


#iterator & iterable


list1 = [3,8,6]

# for i in list1:
#     print(i)

# i = iter(list1)
# print(next(i))
# print(next(i))
# print(next(i))

def num_gen(n):
    for i in range(1,n+1):
        yield i

numbers = num_gen(11)

for i in list1:
    print(i)

for i in list1:
    print(i)