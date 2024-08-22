lines = []
print('\033[2J')

while True:
    line = input('')
    if line == 'EXIT':
        break
    lines.append(line)

with open(input(''), 'w') as file:
    for line in lines:
        file.write(f'{line}\n')
