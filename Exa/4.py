largest = None
print('Before:', largest)
for i in [3, 41, 41, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i

print('Largest:', largest)
