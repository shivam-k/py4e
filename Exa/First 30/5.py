smallest = None
print('Before:', smallest)
for i in [3, 41, 41, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i

print('Largest:', smallest)
