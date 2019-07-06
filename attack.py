#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 08:57:58 2019

@author: bhumika
"""

print("Attack!")
print("Welcome to Attack, let us go through the rules")
print("lets roll! Your dice:")

import random

mylist1 = []

mylist2 = []
mylist3 = []

asidelist = []

lista = [1]

totalscore = [24]
            
for i in range(5):
        e = random.randint(1,6)
        mylist1.append(e)
print(mylist1)

a = None
    
while a != "below 11" and a!= "above 24":
    
    a = input("Choose below 11 or above 24 ")
    
    if a == "below 11":
        print("ok!")
    elif a == "above 24":
        print("Ok!")
    else:
        print("Not valid selection, chose below 11 or above 24")
 
while len(asidelist) != 5: 
    
    check = False
        
    while check is False:
    
        b = list(map(int, input("Which number(s) to set aside? ").split()))
        
        check = all(num in mylist1 for num in b)
    
        print(check)
    
        if check is True:
            for item in b:
                asidelist.append(item)
        else:
            print("Not your dice! Try again")
            
 
    print("total so far = ", sum(asidelist))
    
    print("next roll")
    
    mylist1 = []
    
    def rolldice ():
        for i in range(5 - len(asidelist)):
            f = random.randint(1,6)
            mylist1.append(f)
            print(mylist1)
            
    rolldice()
    
y = sum(asidelist)    

if a == "below 11":
    if y < 11:
        print("You attack by", 11 - y, "points")
    else:
        print ("You lose", y - 11, "points")
else:
    if y > 24:
        print("You attack by", y - 24, "points")
    else:
        print ("You lose", 24 - y, "points")

print("My turn now!")
    