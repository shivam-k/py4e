while True:
    line = input('> ')
    if line.startswith('#') or len(line) == 0:
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
