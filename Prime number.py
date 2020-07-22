# This function asks user for a number and determines if the number is prime or not
def is_prime(num):
  if num > 3 and num % 2 == 0:
    print("This number is not prime")
  elif num > 3 and num % 3 == 0:
    print("This number is not prime")
  else:
    print("This number is prime")

is_prime(int(input("Enter a number: ")))
