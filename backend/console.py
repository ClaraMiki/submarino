import sys
sys.path.append('.')
from backend.model.submarine import Submarine

command = input('Digite um comando:\n')
submarine = Submarine()

for letter in command:
    if letter == 'R' or letter == 'L':
        submarine.update_direction(letter)
    elif letter == 'D' or letter == 'U':
        submarine.move_depth(letter)
    elif letter == 'M':
        submarine.move()
    else:
        print('Comando não existente.')
    
print('\n', submarine)