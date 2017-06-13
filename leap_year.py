def LeapYear(year):
  if(year%4==0):
    if(year%100==0 and year%400==0):
      return 1
    return 1
  return 0
print("\nEnter a Year:\n")
year=int(input())
if(LeapYear(year)==1):
  print("\n{} is a Leap Year".format(str(year)))
else:
  print("\n{} is not a leap year".format(str(year)))
