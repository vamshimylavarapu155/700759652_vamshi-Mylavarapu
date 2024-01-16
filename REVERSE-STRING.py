l=input("Enter the string with a space between each character\n").split()
del(l[0])
del(l[4])
print(''.join(l[::-1]))