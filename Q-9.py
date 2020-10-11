a=input('Enter the string: ')
for i in a:
    if i == ' ':
        a=a.replace(i, '_')
    elif i=='_':
        a=a.replace(i, ' ')
print(a)