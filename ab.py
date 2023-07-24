from testin import test_input, multi_in
lifts = {
    '1':'Crunches',
    '2':'Russian twist',
    '3':'Penguin',
    '4':'Mountain climber',
    '5':'Scissor kick',
    '6':'Leg raises',
    '7':'Flutter kick',
    '8':'Bicycle',
        }
workout = []
def ab():
   print('How many would you like to do?')
   print('1) 3\n2) 5\n3) 7')
   num = input('> ')
   if test_input(3, num):
       for l in lifts:
           print(f'{l}) {lifts[l]}')
       if num == '1':
           picks = input('Pick 3\n> ').split(',')
           if multi_in(8, 3, picks):
               for l in picks:
                   workout.append(lifts[l])
           else:
               return 'bad'
       elif num == '2':
           picks = input('Pick 5\n> ').split(',')
           if multi_in(8, 5, picks):
               for l in picks:
                   workout.append(lifts[l])
           else:
               return 'bad'
       else:
           picks = input('Pick 7\n> ').split(',')
           if multi_in(8, 7, picks):
               for l in picks:
                   workout.append(lifts[l])
           else:
               return 'bad'
       return workout
   else:
       return 'bad'
