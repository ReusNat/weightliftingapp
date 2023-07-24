from testin import test_input, multi_in
lifts = {
    '1':'Incline bench',
    '2':'Dumb bell incline bench',
    '3':'Tricep extention',
    '4':'Shoulder press',
    '5':'Dumb bell shoulder press',
    '6':'Lat pull down',
    '7':'Dumb bell curls',
    '8':'Hammer curls',
    '9':'Chest fly',
    '10':'Bar bell rows'
        }
workout = ['Primary', '', []]
def fub():
    print('Pick your main:')
    print('1) Flat bench')
    print('2) Dumb bell flat bench')
    main = input('> ')
    if test_input(2, main):
        if main == '1':
            workout[1] = 'Flat bench'
        else:
            workout[1] = 'Dumb bell flat bench'
    else:
        return 'bad'

    print('Pick your secondaries (pick 5):')
    print('ex: 1,3,6,10,9')
    for l in lifts:
        print(f'{l}) {lifts[l]}')
    secondary = input('> ').split(',')
    
    if multi_in(10, 5,secondary):
        for lift in secondary:
            workout[2].append(lifts[lift])
    else:
        return 'bad'

    return workout

