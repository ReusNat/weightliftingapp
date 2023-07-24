from testin import test_input, multi_in
lifts = {
    '1':'Tricep extention',
    '2':'Incline bench',
    '3':'Incline dumb bell bench',
    '4':'Chest fly',
    '5':'Bench dips (Easy mode)',
    '6':'Dips (small person friendly)',
    '7':'Overhead tricep extention',
    '8':'Seated overhead press',
    '9':'Standing overhead press', 
    '10':'Dumb bell overhead press', 
    '11':'Barbell overhead press' 
        }
workout = ['Primary','', []]
def push():
    print('Pick your main:')
    print('1) Flat bench')
    print('2) Dumb bell flat bench')
    print('3) Close grip flat bench')
    main = input('> ')
    if test_input(3, main) is True:
        if main == '1':
            workout[1] = 'Flat bench'
        elif main == '2':
            workout[1] = 'Flat bench'
        else:
            workout[1] = 'Dumb bell flat bench'
    else:
        return 'bad'

    print('Pick your secondaries (pick 4):')
    print('ex: 1,3,6,10')
    for l in lifts:
        print(f'{l}) {lifts[l]}')
    secondary = input('> ').split(',')
    
    if multi_in(11, 4,secondary) is True:
        for lift in secondary:
            workout[2].append(lifts[lift])
    else:
        return 'bad'

    return workout
