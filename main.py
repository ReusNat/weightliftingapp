# Programmer: Nathan Reusch
import fub, lb, ab, push, pull
from testin import test_input

workoutsheet = 'workout.txt'
print('Welcome to Gainstown where all weights are light and the muscles are large')

while True:
    print('Let\'s get this workout built!')
    inten = input('Intensity:\n1) Light\n2) Moderate\n3) Heavy\n>  ')
    if not test_input(3, inten):
        continue

    if inten == '1':
        inten = ['Light', ['5x8', '4x12', 'Once']]
    elif inten == '2':
        inten = ['Moderate', ['5x6','4x10', 'Twice']]
    else:
        inten = ['Heavy', ['4x4','4x8', 'Three times']]

    print('What are we working?')
    print('1) Full Upper Body')
    print('2) Lower Body')
    print('3) Abs')
    print('4) Push')
    print('5) Pull')
    option = input('> ')
    if not test_input(5, option):
        continue
    
    optionDict = {
            '1':[fub.fub, 'Full Upper Body'],
            '2':[lb.lb,'Lower body'],
            '3':[ab.ab,'Abs'],
            '4':[push.push,'Push'],
            '5':[pull.pull, 'Pull'],
            }

    workout = optionDict[option][0]()
    if workout == 'bad':
        continue
    

    with open(workoutsheet, 'w') as w:
        w.write(f'Intensity: {inten[0]}\n')
        w.write(f'Muscle group: {optionDict[option][1]}\n')

        if workout[0] != 'Primary':
            w.write(f'Complete {inten[1][2]} through to complete the workout\n')
            w.write('Do each of these for 1 minute:\n')
            for l in workout:
                w.write(f'{l}\n')

        else:
            if 'pull ups' in workout[1]:
                inten[1][0] = ''
            w.write(f'Primary: {inten[1][0]} {workout[1]}\n')
            w.write('Secondary:\n')
            for lift in workout[2]:
                w.write(f'{inten[1][1]} {lift}\n')

    print(f'Workout made, it can be seen by opening {workoutsheet}')
    print('Would you like to make another? (y/n)')
    ans = input('> ').lower()
    if ans == 'n':
        break

