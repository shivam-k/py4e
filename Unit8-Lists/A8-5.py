fhand = open('../mbox-short.txt')
count = 0
for lines in fhand:
    if lines.startswith('From '):
        lst = lines.split()
        print(lst[1])
        count = count + 1
print(count)
