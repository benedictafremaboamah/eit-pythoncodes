from operator import length_hint
from xml.dom.pulldom import START_ELEMENT


age=19
# if statement
if age< 18:
    print("Still growing")
elif age>= 18 and age < 21:
    print("You are an adolescent")
else:
    print("You are an adult")

#for in statement
users=["Frema", "Akosua", "Kwasi", "Abdul"]
for user in users:
    print(user)

# while statement
num=10
stepper=0
while (stepper<10):
    print (stepper)
    stepper +=1

# while statement printing even numbers
num=10
stepper=0
while (stepper<num):
    if (stepper % 2)== 0:
        print (stepper)
    stepper +=1
    
# printing length   
users=["Frema", "Akosua", "Kwasi", "Abdul"]
index=0
length= len(users)
while index<length:
    print(users[index])
    index +=1
