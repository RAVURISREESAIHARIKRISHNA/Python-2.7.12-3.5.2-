import random
import sys

secret=random.randint(1,10)
print("\t\t**************NUMBER GAME**************\t\t\n\n")
#print("\t\tYou HAve Only 5Chances")
count=2
while count>=1:
  print("\t\tYou have only {} Chance(s) Left".format(count))
  print("Enter a Number:")
  enter=int(input())
  count-=1
  if(enter==secret):
    print("Hey!!\nYou Nailed it!!\nThe Secret Number is {}".format(str(secret)))
    sys.exit()
  if(enter+2>secret):
    print("Just Close...\nThe Number is a liitle Greater...\n")
    continue
  if(enter+2<secret):
    print("Just Close..\nThe Number is a little Smaller..\n")
    continue
  if(enter<secret):
    print("The number is Larger...Better Luck Next Time!")
    continue
  if(enter>secret):
    print("The Number is Smaller...Better Luck Next Time!")
    continue
print("You Loose...")
