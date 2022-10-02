



#filter() function

list1 = [32,87,9,3,8,65,98,90,50,53]

def find_odd(items):
    return items % 2 != 0

print(list(filter(find_odd,list1)))

