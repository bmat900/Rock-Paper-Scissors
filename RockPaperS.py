rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choose = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
choose = int(choose)

comp = random.randint(0,2)

if choose == 0:
  print (rock)
  if comp == 0:
    print ('Computer chose:\n' + rock)
  elif comp == 1:
    print ('Computer chose:\n' + paper)
  else:
    print ('Computer chose:\n' + scissors)
elif choose == 1:
  print (paper)
  if comp == 0:
    print ('Computer chose:\n' + rock)
  elif comp == 1:
    print ('Computer chose:\n' + paper)
  else:
    print ('Computer chose:\n' + scissors)
else:
  print (scissors)
  if comp == 0:
    print ('Computer chose:\n' + rock)
  elif comp == 1:
    print ('Computer chose:\n' + paper)
  else:
    print ('Computer chose:\n' + scissors)

if choose == comp:
  print ('You Draw')
elif choose == 0 and comp == 2:
  print ('You Won')
elif choose == 1 and comp == 0:
  print ('You Won')
elif choose == 2 and comp == 1:
  print ('You Won')
else:
  print ("You Loose")