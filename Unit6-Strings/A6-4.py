str = 'X-DSPAM-Confidence: 0.8475'

temp = str.find(':')
ctn = str[temp+1:]
print(ctn)
print(float(ctn))
