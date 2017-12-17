def count(str):
    ctn = 0
    for word in str:
        ctn = ctn + 1
    return(ctn)

temp = input('Enter String: ')
x = count(temp)
print('Words:', x)
