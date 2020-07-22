# Create a function that asks the user for the length of the Fibonacci sequence required and returns a list
# Fibonacci sequence (Starting with 0 and 1)

def fibonacci(length):
  counter = 0
  a = [0, 1]
  while counter < length:
    a.append(a[len(a) - 1] + a[len(a) - 2])
    counter = counter + 1
    if counter == length:
      print(a)
fibonacci(int(input("Enter the length of Fibonacci sequence: ")))
