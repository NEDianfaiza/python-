# Program 1

'''x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))
operation=int(input("Enter Operation:"))
if operation==1:
    add=x+y
    print(add)
elif operation==2:
    sub=x-y
    print(sub)
elif operation==3:
    mult=x*y
    print(mult)
elif operation==4:
    div=x/y
    print(div)
elif operation==5:
    power=x**y
    print(power)'''

# Program 2

'''List = [0, 2, "b", 6, "r", 4]

def parseIntegers(mixedList):
    List1 = [i for i in mixedList if isinstance(i, int)]
    print(List1)

parseIntegers(List)'''

#Program 3

'''dict = {5:100, 6:200}
dict.update({8:300})
print(dict)'''

# Program 4

'''def Sum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
dict = {'a': 100, 'b': 200, 'c': 300}
print(Sum(dict))'''

# Program 5

'''def repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated



l= [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(repeat(l))'''

#Program 6

d = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
def key(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key(4)
key(7)
