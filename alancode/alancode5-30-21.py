###################################################################
# Alan Schuster
# Disease Program
# Detect Diseases
# Today
###################################################################

##matching disease name array ## added your mom, fortnite, and schuster gang
diseaseNames = ["Explosive Finger", "Autumn Scurvy", "Chilling Fever", "Avian Foot", "Arachnid Parasite", "Dragon Paralysis", "Ugly Eye", "Quivering Foot", "Your mom disease", "Fortnite Disorder", "Schuster-Gang Syndrome"]
##disease symptom data ## added death, fortnite, and age
# [max fever 102, min fever 103, dry cough, wet cough, headache, backache, stomach ache, nausea, sneeze, death, fortnite, age]
diseaseSymptoms = [
[1,0,1,0,0,0,1,0,0,0,0,0], # explosive finger
[0,0,0,1,1,0,0,1,0,0,0,0], # autumn scurvy
[0,1,0,0,0,1,0,1,1,0,0,0], # chilling fever
[0,0,1,0,0,1,0,0,1,0,0,0], # avian foot
[1,0,0,1,0,0,1,0,0,0,0,0], # arachnid parasite
[0,1,0,0,0,1,0,1,1,0,0,0], # dragon paralysis
[0,0,1,1,0,0,1,0,0,0,0,0], # ugly eye
[0,0,0,0,0,1,0,0,1,0,0,0], # quivering foot
[0,1,0,1,1,1,1,1,1,1,0,0], # your mom disease
[1,0,1,0,1,1,0,1,0,0,1,1], # fortnite disorder
[0,0,0,0,0,0,0,0,0,0,0,1]  # schuster-gang syndrome
]
##user data array
userData = [0,0,0,0,0,0,0,0,0,0,0,0]
#gathering user data
name =         input("What is your name? ")
if             input("Do you have a fever? ") == "yes":
    fever =    input("How high is your fever? ")
else:
    fever =    False
if             input("Do you have a cough? ") == "yes":
    cough =    input("Is it wet or dry? ")
else:
    cough =    False
headache =     input("Do you have a headache? ")
backache =     input("Do you have a backache? ")
stomachache =  input("Do you have a stomach ache? ")
nauseous =     input("Do you feel nauseous? ")
sneeze =       input("Are you sneezing? ")
death =        input("Are you dead? ")
fortnite =     input("Do you play fortnite? ")
age =          input("How old are you? ")

#converting responses to actually usable data

##fever conversion
if fever == False:
    userData[0] = 0
    userData[1] = 0
elif int(fever) <= 102:
    userData[0] = 1
else:
    userData[1] = 1

##cough conversion
if cough == False:
    userData[2] = 0
    userData[3] = 0
elif cough == "dry":
    userData[2] = 1
else:
    userData[3] = 1

##headeache conversion
if headache == "yes":
    userData[4] = 1
#backache conversion
if backache == "yes":
    userData[5] = 1
#stomachache conversion
if stomachache == "yes":
    userData[6] = 1
#nausea conversion
if nauseous == "yes":
    userData[7] = 1
#sneeze conversion
if sneeze == "yes":
    userData[8] = 1
#death conversion
if death == "yes":
    userData[9] = 1
#fortnite conversion
if fortnite == "yes":
    userData[10] = 1
#age conversion
if int(age) >= 16:
    userData[11] = 1

#potential symptoms array
potentialSymptomsIndexs = []

#looping through the different diseases because its a nested list
for g in range(len(diseaseSymptoms)):
    #checking the number of matched symptoms
    symptomMatchCounter = 0
    #checking every user input against that disease and if its more than 7 they add a potential disease array
    for i in range(len(userData)):
        if userData[i] == diseaseSymptoms[g][i]:
            symptomMatchCounter += 1
    if symptomMatchCounter >= 7:
        potentialSymptomsIndexs.append(g)

#tell the user their potential diseases
print(name+"you may have the following: ")
for j in range(len(potentialSymptomsIndexs)): # i loop through it and also check if its the last one because i dont want a comma on the last item
    if j == len(potentialSymptomsIndexs) - 1:
        print(diseaseNames[potentialSymptomsIndexs[j]], end='') #end='' makes it so i dont have to print a single string i just tell python to put it on the same line
    else:
        print(diseaseNames[potentialSymptomsIndexs[j]]+", ", end='')
