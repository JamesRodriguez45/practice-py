#Name: James Rodriguez
#Date: March 8, 2018

import time
from random import *

#Method writing practice test
def main1(x,y):
    if x>y:
        print(x)
    else:
        print(y)

#Work-in-Progress AI
def main2():
    #Question 1: Name
    x=str(input("Enter name: "))
    h=True
    
    while(h):
        if(len(x)-x.count(" ")>0):
            h=False
        else:
            x=str(input("Enter name: "))
    print("Welcome",x)

    time.sleep(2)

    #Question 2: Directory Path
    h=True
    while(h):
        y=str.lower(input("Would you like me to display current directory?: "))
        if(y=='yes'):
            print("Displaying current directory....")
            time.sleep(3)
            #Using ''' in order to display multiple print lines using 1 print command
            print('''ERROR
I do not have direct access to current directory''')
            h=False
        elif(y=='no'):
            print('''Understood
Reloading last question...''')
            time.sleep(3)
        else:
            print('''I did not understand your input:''',y,'''
Reloading last question...''')
            time.sleep(3)

    #Question 3: Solve Simple Math DID NOT TEST YET
    h=True
    while(h):
        a=randint(1,100)
        b=randint(1,100)
        h1=True
        while(h1):
            print('''You are presented with two numbers
''', a, "and", b, '''
Which is the greater number?''',c=int.lower(input()))
            if c==a or c==b:
                h1=False
            else:
                print("You entered an incorrect response. Try again.")
        del(h1)
        if c==a:
            if a>b:

#----------------------------Main Code------------------------------
main2()
