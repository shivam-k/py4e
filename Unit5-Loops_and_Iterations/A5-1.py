count=0;
tot = 0;
while True:
    num = input("Enter a Number: ")
    if num == 'done':
        break
    else:
        try:
            num = float(num)
            count = count+1;
            tot = tot + num
        except:
            print("Enter Number.")
            continue

print(tot, count, tot/count)
