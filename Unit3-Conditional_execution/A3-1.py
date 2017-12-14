hours = input("Enter Hours:")
rate = input("Enter Rate: ")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Please Enter Number")
    exit()

if hours > 40:
    fact = int(hours/40)
    pay1 = fact*40*rate  #Regular Payment
    pay2 = (hours - fact*40)*rate*1.5   #Overtime Payment
    pay = pay1+ pay2
else:
    pay = hours*rate

print("Pay:", pay)
