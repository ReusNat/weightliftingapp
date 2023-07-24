from testin import test_input, multi_in
lifts = {
    '1':'Dumb bell curls',
    '2':'Bar bell curls',
    '3':'Hammer curls',
    '4':'Dumb bell hammer curls',
    '5':'Reverse curls',
    '6':'Lat pull down',
    '7':'Dumb bell rows',
    '8':'Barbell rows',
    '9':'Pull ups',
    '10':'Reverse flies',
        }
workout = ['Primary','', []]

def pull():
    print('Pick your main:')
    print('1) Pull up (3, 4, 5 sets till failure)')
    print('2) Bar bell rows')
    print('3) Dumb bell rows')
    main = input('> ')
    if test_input(2, main):
        if main == '1':
            print('How many sets?')
            print('1) 3\n2) 4\n3) 5')
            sets = input('> ')
            if test_input(3, sets):
                if sets == '1':
                    workout[1] = '3 sets pull ups till failure'
                elif sets == '2':
                    workout[1] = '4 sets pull ups till failure'
                else:
                    workout[1] = '5 sets pull ups till failure'
        elif main == '2':
            workout[1] = 'Bar bell rows'
        else:
            workout[1] = 'Dumb bell rows'
    else:
        return 'bad'

    print('Pick your secondaries (pick 4):')
    print('ex: 1,3,6,10')
    for l in lifts:
        print(f'{l}) {lifts[l]}')
    secondary = input('> ').split(',')
    
    if multi_in(10, 4, secondary):
        for lift in secondary:
            workout[2].append(lifts[lift])
    else:
        return 'bad'

    return workout
