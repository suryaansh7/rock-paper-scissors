import random
k=input("enter 1 for rock r rock ,2 for paper and 3 for scissors")
s=int(k)
rock='''
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
print("u chose")
if(int(s)==1):
    print(rock)
elif(int(s)==2):
    print(paper)
else:
    print(scissors)

game=[rock, paper, scissors]
com=random.randint(0,2)
print("comp chose")
print(com)
print(game[com])
if(s==1):
    if(com==0):
        print("draw")
    elif(com==1):
        print("u lose")
    else:
        print("u win")
elif(s==2):
    if(com==0):
        print("u win")
    elif(com==1):
        print("draw")
    else:
        print("u lose")
elif(s==3):
    if(com==0):
        print("u lose")
    elif(com==1):
        print("u win")
    else:
        print("draw")
