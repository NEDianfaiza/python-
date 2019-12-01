#Question1:

'''dic={
    'first_name':input("Enter First Name"),
    'last_name':input("Enter Last Name"),
    'age':int(input("Enter Age")),
    'city':input("Enter City")
}
print(dic)
dic["qualification"]="High Academic Level"
print(dic)
del dic["qualification"]
print(dic)'''

#Question2:

'''cities={
    'Karachi':{
        'country':"Pakistan",
        'population':"14.91 million",
        'fact':"It is called City of Lights"
    },
    'Chicago':{
        'country':"USA",
        'population':"2.716 million",
        'fact':"It has an iconic John Hancock Center, 1,451-ft."
    },
    'Dubai':{
        'country':"United Arab Emirates",
        'population':"3.137 million",
        'fact':"It has Burj Khalifa, an 830m-tall tower."
    }
}
print(cities['Karachi'])
print(cities['Chicago'])
print(cities['Dubai'])'''

#Question3:

'''while True:
    age = int(input("Enter Age:"))
    if age<=3:
        print('Ticket is free')
    elif age>3 and age<=12:
        print('Ticket is of $10')
    else:
        print('Ticket is of $15')'''

#Question4:

'''def favorite_book(title):
    print('One of my favorite books is',title)

favorite_book('Cinderella')'''

#Question5:

import random
count = 0
a = random.randint(1, 30)
for count in range(3):
    inp = int(input("Enter Number between 1 to 30:"))
    if inp==a:
        print("Correct")
        break
    elif a>inp:
        print("Hidden num is greater than input")
    elif a<inp:
        print("Hidden num is smaller than input")

