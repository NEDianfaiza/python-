#program 1

num = int(input('number?'))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#program 2

string=str(input("Enter string:"))
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
   

#program 3

list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 == 0: 
       print(num, end = " ") 

#program 4

my_str =str(input('Enter a string'))
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


#program 5

num = int(input('enter a number'))
if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")



#program 6

def func():
    List=[]
    a=int(input("Enter No of items:"))
    for i in range(0,a):
        i=input("Enter Items:")
        List.append(i)
    print(List)
func()









































