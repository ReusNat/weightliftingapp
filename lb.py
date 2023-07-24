from testin import test_input, multi_in
lifts = {
    '1':'Calf raises',
    '2':'Hamstring curl',
    '3':'Quad extentions',
    '4':'Split squat',
    '5':'Leg press',
    '6':'Hip abduction',
    '7':'Hid adduction',
    '8':'Stair stepper (5min, 10 min, 20 min)',
    '9':'Romanian dead lift (RDL)'
        }

workout = ['Primary', 'Squat', []]

def lb():
    print('Pick your secondaries (pick 4):')
    print('ex: 1,3,6,9')
    for l in lifts:
        print(f'{l}) {lifts[l]}')
    secondary = input('> ').split(',')
    
    if multi_in(9, 4,secondary) is True:
        for lift in secondary:
            workout[2].append(lifts[lift])
    else:
        return 'bad'

    return workout
