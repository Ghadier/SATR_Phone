
print('Hello!')

name_or_num = input('\nWhat would you like to search for:\nnumber or name? ')
valid_ans = ['number', 'name']
while name_or_num.lower() not in valid_ans:
    name_or_num = input("Invalid inputs! \nPlease type 'number' or 'name': ")


keys = ['1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777']
values = ['amal', 'mohammed', 'khadijah', 'abdullah', 'rawan', 'faisal', 'layla']
phone_dictionary = dict(zip(keys, values))

print('-'*40)

if name_or_num.lower() == "number":
    while True:
        try:
            search_num = input('Enter the phone number:\nXXXXXXXXXX\n')
            int(search_num)
            while len(search_num) != 10:
                search_num = input('This is invalid number\nEnter 10 digits:\nXXXXXXXXXX\n')
        except ValueError:
            print('This is invalid number!')
            continue
        else:
            break

    if search_num in keys:
        print('This phone number belong to:', phone_dictionary[search_num])
    else:
        print('Sorry, the number is not found!')

elif name_or_num.lower() == "name":
    while True:
        try:
            search_name = input('Enter the name: ')
            while search_name.isinstance() != string:
                search_name = input('This is invalid name\nEnter the name again: ')
        except ValueError:
            print('Sorry, this is not a name!')
            continue
        else:
            break

    if search_name.lower() in values:
        for number, name in phone_dictionary.items():
            if name == search_name:
                print('This name has a phone number: ', number)
    else:
        print('Sorry, the name is not found!')

print('-'*40)
