# This function removes duplicates from a given list
a = [1, 1, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def remove_dup(list):
  for element in list:
    while list.count(element) > 1:
      a.remove(element)
  print(a)
  
remove_dup(a)
