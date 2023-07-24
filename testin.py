def test_input(numOptions, option):
    try:
        option = int(option)
        if option > numOptions or option < 1:
            print(f'{option} is not a valid option')
            return False
        return True
    except ValueError:
        print(f'{option} is not a valid option')
        return False

def multi_in(numOptions, picks, options):
    if picks != len(options):
        print('You didn\'t select the right number of options!')
        return False
    for option in options:
        try:
            option = int(option)
            if option > numOptions or option < 1:
                print(f'{option} is not a valid option')
                return False
        except ValueError:
            print(f'{option} is not a valid option')
            return False
        return True

