import re
count = 0
chand = input('Enter a regular expression: ')
for line in open('../mbox-short.txt'):
    line = line.rstrip()
    #x = re.findall(chand, line)
    if re.search(chand, line):
        count = count + 1
print(count)
