fname = input('Enter File Name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opend:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines', fname)
