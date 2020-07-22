# Function that reverses any string input by user
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
