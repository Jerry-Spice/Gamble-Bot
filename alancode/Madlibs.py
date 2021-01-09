"""Madlibs.py"""

import random

def makeStory1(name1, name2, verb1, verb2, noun1, noun2):
    print("One day "+name1+" "+verb1+" into the forest. Their sibling "+name2+" follows them in. Soon they encounter a "+noun1+" which promptly "+verb2+". Finally they find a "+noun2+" and leave the forest.")
def makeStory2(name1, name2, verb1, verb2, noun1, noun2):
    pass
def makeStory3(name1, name2, verb1, verb2, noun1, noun2):
    pass

#makeStory1("Jerry","Kerry","walks","prances","mountain","cup")

while True:
    n1=input("Enter name 1: ")
    n2=input("Enter name 2: ")
    v1=input("Enter verb 1: ")
    v2=input("Enter verb 2: ")
    no1=input("Enter noun 1: ")
    no2=input("Enter noun 2: ")
    num = random.randint(1,3)
    if num == 1:
        makeStory1(n1,n2,v1,v2,no1,no2)
    elif num == 2:
        makeStory2(n1,n2,v1,v2,no1,no2)
    elif num == 3:
        makeStory3(n1,n2,v1,v2,no1,no2)
