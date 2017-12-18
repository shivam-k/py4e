fname = input('Enter File Name: ')
try:
    fname = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened:', fname)
