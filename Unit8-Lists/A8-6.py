store = []

while True:
    x = input('Enter the number: ')
    if x == 'done': break
    try:
        x = float(x)
    except:
        continue
    store.append(x)

print(max(store))
print(min(store))
