import time

Greet='''
================================
|  Good Morning or Afternoon   |                                                                       
================================ 
'''
print(Greet)
time.sleep(2)
 
Question='''
=================
|Is it Morning: |
=================
'''
print(Question)
time.sleep(2)



def call():
  Day=input("Please input day:")
  f=(Day)
  return f


Respond=f'''
====================
|Yay, Good {call()}|
===================
'''
print(Respond)
time.sleep(2)

Explain='''
=======================================================================
|Today, I will be helping you to Calculate The Hypotenus of a Triangle|
|using the Famous Pythagoras Theorem                                  |
=======================================================================
'''
for letter in Explain:
  print(letter,end='')
  time.sleep(0.007)

time.sleep(2)
Begin='''
===============
|Let\'s Begin |
===============
'''
print(Begin)
time.sleep(2)

formula='''
===================
| FORMULA:        |
|________________ |
|   _____________ |
|c=√Opp^2 + Adj^2 |
|                 |
|        OR       |
|                 |
|c^2=Opp^2 + Adj^2|
================== 
''' 
for line in formula:
  print(line, end='')  
  time.sleep(0.012)
time.sleep(2)
print("This is going to be fun.") 
print()

answer = 'yes'


while answer.lower() == 'yes':
  try: 

    opp=float(input("Enter The opposite of the triangle:"))

    adj=float(input("Enter The adjcent of the triangle:"))

    d=round((opp**2 + adj**2)**0.5 , 2)

    Calculate= f'''
          __________
    c = √{opp}^2 + {adj}^2
        
        ____
    c= √{opp**2} + {adj**2}
          ___
    c = √ {opp**2 + adj**2}

    c = {d}

    Therefore, the hypotenus of triangle with sides {opp} and {adj} is {d}

    '''

    for line in Calculate:
        print(line,end='')
    time.sleep(0.024)

      
    print("🎉🎉Congratulation🎉🎉")
    time.sleep(2)
    print("You now Understand the Maths Calculation of The Almighty Pythagoras Theorem   ")
    time.sleep(3)
    answer = input("For the Fun of it, Why not try Another Number? (yes/no): ")

    while answer.lower() not in ('yes','no') :
      print("Invaild input")
      answer = input("Come on, You can do better....Try again ? (yes/no): ")

    if answer == "no":
      print("ARE YOU SURE? WELL,It was fun while it lasted 😥. ")
      time.sleep(2)
      print("Please, Give yourself An Applause..............👏👏")
      time.sleep(3) 
      print("That was Great, Wasn't it?\nHave wonderful day.")
      time.sleep(3)
      print("OH,And one more thing")
      time.sleep(2)
      print("DON'T FORGET TO STAY POSTIVE WHILE CALCULATING NUMBERS")
      time.sleep(2)
      print("AND ALWAYS, I MEAN ALWAYS.")
      time.sleep(2)
      print("WEAR A SMILE😁😁😀")

  except Exception as e:
    print("❕❕❕WHAT AN ERROR❕❕❕")
    answer = input("Want to Restart Again?(yes/no): ")
  
    while answer.lower() not in ('yes','no') :
      answer = input("Please input a yes or a NO: ")

    if answer == "no":
      print("ARE YOU SURE? WELL,It was fun while it lasted 😥.")
      time.sleep(2)
      print("Please, Give yourself An Applause..............👏👏")
      time.sleep(3) 
      print("That was Great, Wasn't it?\nHave wonderful day.")
      time.sleep(3)
      print("OH,And one more thing")
      time.sleep(2)
      print("DON'T FORGET TO STAY POSTIVE WHILE CALCULATING NUMBERS")
      time.sleep(2)
      print("AND ALWAYS, I MEAN ALWAYS.")
      time.sleep(2)
      print("WEAR A SMILE😁😁😀")
