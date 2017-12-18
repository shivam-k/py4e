fhand = open('../mbox-short.txt')
for line in fhand:
    lx = line.rstrip()
    print(lx.upper())
