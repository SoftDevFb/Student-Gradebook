sName = []
inputName = ''
sGrades = []
inputGrades = 0
name = 'y'
while name == 'y':
    inputName = input("what is the name")
    sName.append(inputName)
    print (sName)
    inputGrades = float(input("what are the grades?"))
    sGrades.append(inputGrades)
    print (sGrades)
    name = input("cont?")
    
for i in range(0, len(sName)):
    print (sName[i], sGrades[i])
    inputGrades = i
average = sum(sGrades) / len(sGrades)
print ("The highest grade is", max(sGrades))
print ("The lowest Grade is", min(sGrades))
print ("The average grade is", average)
