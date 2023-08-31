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


Name=input("NAME:")
print("My,My")
time.sleep(1)
print(f"Your Name is {Name}")
time.sleep(2)
print(f"{Name}, That's a LOVELY NAME.")
time.sleep(3)

print(f"Okay {Name}, Are you ready?")
answer=input("Enter Yes or No:")
answer=answer.lower()
if answer=="yes":
  print("YEAH👍😁👍👍👍")
elif answer=="no":
  print("Don't worry, You going to have fun👌👌👌 ")
time.sleep(2)

print(f"So {Name},We are going to Focus on two subjects\nMATH or ENGLISH")




# FOR MULTILINNING STRINGS
# multi = '''Hi, 
# I am a multiline string😁

# Nice to meet you
# '''
# test = "lol"

# print(multi)

# game =f"""
# ================================
# |   Helooooo                   |
# |   Good to be hearrr          |
# |   {test}                   |
# ================================
# """
# print( game)


# a = 9
# b = 12
# d = (a**2 + b**2) ** 0.5

# Hi= f'''
#      __________
# c = √{a}^2 + {b}^2
#     ____
# c= √{a**2} + {b**2}
#      ___
# c = √ {a**2 + b**2}

# c = {d}

# Therefore, the hypotenus of tria with sides {a} and {b} is {d}

#  '''
# print(Hi)