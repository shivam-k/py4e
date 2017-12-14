hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Enter Number")
    exit()

def computepay(hours, rate):
    if hours <= 40:
        pay = hours*rate
    else:
        frac = int(hours/40)
        pay1 = frac*40*rate
        pay2 = (hours - 40*frac)*rate*1.5
        pay = pay1 + pay2
    print("Pay:", pay)

computepay(hours, rate)
