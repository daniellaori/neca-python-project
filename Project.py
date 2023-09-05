# ALGORTHIM THAT RECEIVES THE OPPISITE AND ADJCENT THEN CALCULATES THE HYPOTENUS
  #  For the End User to Understand the pythagoras theorem

# 


import time

Hello='''
================================
|  Good Morning or Afternoon   |                                                                       
================================ 
'''
print(Hello)
time.sleep(2)
 
G='''
=================
|Is it Morning: |
=================
'''
print(G)
time.sleep(2)



def call():
  a=input("Please input day:")
  f=(a)
  return f


H=f'''
====================
|Yay, Good {call()}|
===================
'''
print(H)
time.sleep(2)

L='''
=======================================================================
|Today, I will be helping you to Calculate The Hypotenus of a Triangle|
|using the Famous Pythagoras Theorem                                  |
=======================================================================
'''
for letter in L:
  print(letter,end='')
  time.sleep(0.007)

time.sleep(2)
Y='''
===============
|Let\'s Begin |
===============
'''
print(Y)
time.sleep(2)

S='''
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
for line in S:
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

    Hi= f'''
          __________
    c = √{opp}^2 + {adj}^2
        
        ____
    c= √{opp**2} + {adj**2}
          ___
    c = √ {opp**2 + adj**2}

    c = {d}

    Therefore, the hypotenus of triangle with sides {opp} and {adj} is {d}

    '''

    for line in Hi:
        print(line,end='')
    time.sleep(0.024)

      
    print("🎉🎉Congratulation🎉🎉\n Thank you. ")
    answer = input("Why not try another number? (yes/no): ")

    while answer.lower() not in ('yes','no') :
      print("Invaild input")
      answer = input("try again ? (yes/no): ")

    if answer == "no":
      print("Thank you, That is All")

  except Exception as e:
    print("Error")
    answer = input("try again ? (yes/no): ")
  
    while answer.lower() not in ('yes','no') :
      answer = input("try again ? (yes/no): ")

    if answer == "no":
      print("Thank you, That is All")