
##program1

Total=500
phys=int(input('enter marks of pysics'))
maths=int(input('enter marks of maths'))
urdu=int(input('enter marks of urdu'))
isl=int(input('enter marks of Islamiat'))
eng=int(input('enter marks of English'))
percentage=((phys+maths+urdu+isl+eng)/500)*100
print(percentage)

if percentage>=90 and percentage<100:
    print('A+')
elif percentage>=80 and percentage<90:
    print('B')
elif percentage>=70 and percentage<80:
    print('C')
elif percentage>=60 and percentage<70:
    print('D')
elif percentage>=50 and percentage<60:
    print('E')
else:
    print('You are fail')

    
##program2  
number=int(input('enter any num'))
if number%2==0:
    print('The number is even')
else:
    print('The number is odd')

    
    
list=[1,2,3,4,5,6,7,8]
a=len(list)
print('number of elements in the list is' ,a)


##program4
sum=0
list=[2,4,5,6]
for i in list:
    sum+=i
print(sum)

##program5
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst))

##program6

a=[1,1,2,3,5,8,13,21,34,55,89]
list=[]
for i in a:
    if i<5:
        list.append(i)
print(list)        



























