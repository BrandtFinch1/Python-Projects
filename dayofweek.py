day= input('Enter the day of the week: ')
if day == 'monday' or day == 'wednesday':
    alarm = '7:30 AM'
    carpool= True
    coding_class= True
    gym= False
elif day == 'tuesday' or day == 'thursday':
    alarm = '6:30 AM'
    carpool= True
    coding_class= False
    gym= False

else:
    alarm = 'Alarm OFF'
    carpool= False
    print('No carpool today.')
    coding_class= False
    print('No Coding Class Today')
    gym= True
    print('There is gym today')
print(alarm, carpool, coding_class, gym)

