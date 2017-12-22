largest = None
smallest = None
while True:
    num = input("Enter a Number: ")
    if num == 'done':
        break
    else:
        try:
            num = float(num)
            if largest is None or num > largest:
                largest = num
            if smallest is None or num < smallest:
                smallest = num
        except:
            print("Enter Number.")
            continue

print(largest, smallest)
