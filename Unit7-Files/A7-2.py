fname = input('Enter File Name: ')
try:
    fhand = open(fname)
except:
    print('That is not a valid file:', fhand)
count = 0
tot = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        val = float(line[pos+1:])
        tot = tot + val
print('Average Spam confidence: ', tot/count)
