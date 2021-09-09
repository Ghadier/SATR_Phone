print('Hello!')

def get_filter():
    name_or_num = input('Would you like to find the name or the number? type name or number: \n')
    valid_nn = ['name', 'number']
    while name_or_num.lower() not in valid_nn:
        name_or_num = input('Invalid inputs. Please enter: name or number\n')

    if name_or_num.lower() == 'number':
        phone_num = str(input('Please enter the phone number: \nXXXXXXXXXX \n'))
    else:
        phone_name = input('Please enter the name: \n')

    return phone_num

def valid_number(phone_num):
    keys = ['1111111111', '2222222222',
            '3333333333', '4444444444',
            '5555555555', '6666666666',
            '7777777777']
    values = ['amal', 'mohammed', 'khadijah',
              'abdullah', 'rawan', 'faisal', 'layla']
    phone_dictionary = dict(zip(keys, values))

    if len(phone_num) != 10 :
        phone_num= input('This is invalid number! Try again with 10 digital numbers:\nXXXXXXXXXX\n')
    elif phone_num in keys:
        print('This phone number belong to: ', phone_dictionary[phone_num])
    else:
        print('Sorry, the number is not found')

def main():
    while True:
        get_filter()
        valid_number(phone_num)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
