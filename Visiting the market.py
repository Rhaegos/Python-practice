#Code that determines odd or even days to visit market based on NIRC
#This is based on implementation of staggered visits by Singapore Government to reduce COVID exposure to the community and enable better tracking
date = int(input("Enter day of month (number): "))
nirc = int(input("What is the last digit of your nirc? "))

if date == 0:
  print("Date does not start with zero!")
elif nirc % 2 == 0 and date % 2 == 0 and nirc <= 10 and date <= 32:
  print("Today is a good day to visit the market!")
elif nirc % 2 != 0 and date % 2 == 0 and nirc <= 10 and date <= 32:
  print("Your nirc is odd hence you can't visit the market today!")
elif nirc % 2 == 0 and date % 2 != 0 and nirc <= 10 and date <= 32:
  print("Your nirc is even hence you can't visit the market today!")
else:
  print("(Invalid number entered! Please check your nirc and date!")
