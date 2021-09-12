
print('Hello!')

keys = ['1111111111', '2222222222',
            '3333333333', '4444444444',
            '5555555555', '6666666666',
            '7777777777']
values = ['amal', 'mohammed', 'khadijah',
              'abdullah', 'rawan', 'faisal', 'layla']
phone_dictionary = dict(zip(keys, values))

name_or_num = input()

def phone_search(keys):
    while True:
        try:
            search_num = input('Enter the phone number:\nXXXXXXXXXX\n')
            int(search_num)
        except ValueError:
            print('Sorry, this is not a number!')
            continue
        else:
            break

    if search_num in keys:
        print('This phone number belong to:', phone_dictionary[search_num])
    else:
        print('Sorry, the name is not found!')

def name_search(search_name):

    for number, name in phone_dictionary.items():
        if search_name.lower() == name:
            return number

    return 'Sorry, the number is not found!'
    print('This name has this phone number:', name_search(search_name))
