# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include  decimal.

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9]+', line):
        print(line)

print('################') # Divider

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a whitespace
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
