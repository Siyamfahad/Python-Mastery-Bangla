



'''
r - opens a file for reading (default mode)
w - opens a file for writing (creates new file if it does not exist)
a - opens a file for appending at the end of the file
b - opens a file in binary mode
+ - opens a file for updating (read and write both)
'''

with open("new_file.txt",'r+') as f:
    print(f.read())
    f.write("I am writing this again")




