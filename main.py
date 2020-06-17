'''
#Lists comprehension using sets exercise
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(set.intersection(a, b))


# list function to get first and last element of a list
# a = [5, 10, 15, 20, 25, 30]
#b = [1 + 0]
#print(b)
#a.append(a[len(a) - 1] + a[len(a) - 2])
#a.append(a[len(a) - 1] + a[len(a) - 2])
#a.append(a[len(a) - 1] + a[len(a) - 2])
#print(a)
#def first_last(list):
 # b = []
 # b.append(a[0])
 # a.reverse()
 # b.append(a[0])
 # print(b)
#first_last(a)

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

# Prime number function exercise

def is_prime(num):
  if num > 3 and num % 2 == 0:
    print("This number is not prime")
  elif num > 3 and num % 3 == 0:
    print("This number is not prime")
  else:
    print("This number is prime")

is_prime(int(input("Enter a number: ")))

# Removing duplicates
a = [1, 1, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#def remove_dup(list):
  #for element in list:
    #while list.count(element) > 1:
      #a.remove(element)
  #print(a)

#remove_dup(a)


# Function that reverses any string
def sentence_reverse(statement):
  convert_to_list = statement.split()
  b = len(convert_to_list)
  counter = 0
  while counter < b:
    x = 1
    reverse = []
    for element in convert_to_list:
      reverse.append(convert_to_list[b - x])
      counter = counter + 1
      x = x + 1
  result = " ".join(reverse)
  print(result)   
sentence_reverse(input("Please input a sentence: "))
'''

# Cows and bulls
import random
print(random.randint())