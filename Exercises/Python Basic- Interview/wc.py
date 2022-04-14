def reverse(w):  #function reverse is created with 'w' as argument                                                                             
    length = len(w)  #length of 'w' is stored in variable length
    s = length  # 's' is assigned the value of variable of variable 'length' created above

    new_list = [None]*length 

    for item in w: 
        s = s - 1
        new_list[s] = item     #reverse in action
    return new_list
  
def word_count_dict(filename):  #function is being created
  word_count = {}  #'{}' creates a dictionary
  input_file = open(filename,'r') #file is opened in read mode
  for line in input_file:
    words = line.split()  # creates a list , comma separated on the basis of argument , by default space
    reverse_words = reverse(words) #reverse function is called 
    print (reverse_words)
    for word in words:
      word = word.lower() #coversion to lower case
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  # file is closed 
  return word_count

def print_words(filename):
  word_count = word_count_dict(filename) #function is being called
  words = sorted(word_count.keys())  #sort according to keys
  for word in words:
    print (word, word_count[word])

def get_count(word_count_tuple): #get_count is itself a method here,it takes word_count.items() as an argument. 
  return word_count_tuple[1] #word_count_tuple[0] is the key and word_count_tuple[1] is the value.we want to sort by values, we use word_count_tuple[1]

def print_top(filename):
  word_count = word_count_dict(filename)
  items = sorted(word_count.items(), key=get_count, reverse=True) #sort in descending order according to keys 
  for item in items[:20]:
    print (item[0], item[1])

print_words('D:/UpX/DS-FoundationJan17/Week2/Assignments/Assignment1Solutions/wc_file.txt')  # to print words with its count
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')  # to print top 20 words in count
print_top('D:/UpX/DS-FoundationJan17/Week2/Assignments/Assignment1Solutions/wc_file.txt') 
