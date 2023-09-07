import time
Gill= "Hello "
print(Gill.upper(),)
time.sleep(1)
print("Welcome to your doom😈😈")
time.sleep(1)
i=0
while i < 6:
  print("HaHaHaHa")
  if i==2:
     break
  i+=1
time.sleep(3)
print("Sorry\nGood Morning")
time.sleep(3)
print("Is it morning where you are?")
time.sleep(3)
print("PLease input day.")
time.sleep(3)

day = ["Morning","Afternoon", "Evening",  ]
while True:
  a = input("Enter a day: ")
  a=a.capitalize()
  if a in day:
    print(f"Good {a}")
    break
  else:
      print("That is not a day\nPlease input a Day: ")
  time.sleep(2)
time.sleep(3)


print("My Name is Selica")
time.sleep(3)
print("I will be helping you learn.")
time.sleep(3)
print("I would love to know your name")
time.sleep(1)
print("Please don't be shy")


# Ask for name
# Result, say that's a lovely {q}
# Say okay what would you want to learn frist
# for the user to see pick  Math or English
# result say{w}
# okay......Drum roll
# here we go


Name=input("NAME: ")
print("My,My")
time.sleep(1)
print(f"Your Name is {Name}")
time.sleep(2)
print(f"{Name}, That's a LOVELY NAME.")
time.sleep(3)

print(f"Okay {Name}, Are you ready?")
answer=input("Enter Yes or No: ")
answer=answer.lower()
if answer=="yes":
  print("YEAH👍😁👍👍👍")
elif answer=="no":
  print("Don't worry, You going to have fun👌👌👌 ")
time.sleep(2)

print(f"So {Name}, We are going to Focus on two subjects")
time.sleep(2)
print("MATH or ENGLISH")
Subject=input("Enter option: ")

while Subject not in ("Math or English"):
  print("Please input 'Either Math or English'")
  Input=input("Math or English: ")
  if 'Math' in Input.capitalize():
    break
time.sleep(1)

print(f"Okay {Name}, {Input} it is!")
time.sleep(2)
print("Now, There are Sub Subjects we have for now.\n I will show you the list")
time.sleep(2)
List='''
1. BODAMS
2. Profit and Loss
3. Percentages
4. Trigonometry
5. LCM (Least Common Multiple)
'''
time.sleep(2)
print('Now, You have the Freedom to pick which one you want to learn\nUnderstand now.')
time.sleep(2)
Sub=input("Pick one, Please: ")
time.sleep()
sub=['BODMAS', 'Profit and Loss', 'Percentages', 'Trigonometry', 'LCM']
while True:
  first=sub[0]
  if first in sub:
    print(f"You picked {first}")
    break







