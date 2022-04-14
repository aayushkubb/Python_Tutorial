# -*- coding: cp1252 -*-

def clean(text): #passing text as argument 
    temp1 = text
    try:  #exception handling 
        temp1 = text.lower().replace('\s','').replace('\t','').replace('\n','').replace("\r","").replace(".","").replace(",","").replace(".,","").replace("&","").replace("-","").replace("+","").replace("'","").replace("[","").replace("]","").strip() #coverting to lower case and replacing spaces , tabs , punctuations , special characters 
        return temp1
    except:
        return temp1

string = """Why Apple Is In My Retirement Portfolio

Summary

Apple is a rare bird of a stock. It offers shareholders enormous growth, and could potentially become the next great dividend stock.
The company is the largest &&&&&& public company in the world, surpassing Exxon Mobil.
The raw fundamentals of this company are virtually incomparable.
Over the last several years, I have been all over the board when it comes to Apple (AAPL). During its parabolic  ------  ----- - - - - - rise in price about 2 years ago, I wrote several articles urging investors to take some chips off the table, and then when it hit some low points, I suggested it might be time to buy the stock, which I did, but not just for my growth portfolio. The stock seemed to have become a value stock with a rather strong + + + + + + dividend, so I placed it in 3 of my portfolios, and have held it ever since in 2 of the 3 portfolios I currently manage.

As of several months ago, I added APPL to my newest retirement portfolio, "Buy The Dips Portfolio", or BTDP. The stock is now [ [ [ [ [  going to be held for the very long term in at least 3 out of 4 of my various portfolios, mainly for dividend income investors, but with an eye towards another strong round of growth.

Apple Is More Than A Reborn Growth Stock, It Is Also A Future Dividend Champion

The recent shareholder-friendly moves ] ] ] ] ] ] that Apple has made should ignite even more intense interest in the stock for both dividend-seeking investors, as well as for growth investors.


"""
print (string)
print ("============================================================")
listA = ['apple','stock','success','growth','interest','investors','portfolio']

string_each_word_count = {} # dictionary is created 
listA_word_match_count = {}

string_clean = clean(string) #calling 'clean' function
print (string_clean)
print ("============================================================")
words = string_clean.split() 
print (words) #string is split into a list on the basis of default argument that is space 
print ("============================================================")
sting_words_count = len(words) # len function to count length
print (sting_words_count) 
print ("============================================================")
for word in words:
    if word in string_each_word_count: #returns true if 'word' s there in dictionary string_each_word_count
        string_each_word_count[word] += 1 #increment the counter
    else:
        string_each_word_count[word] = 1
print (string_each_word_count)
print ("============================================================")
for ele in words:
    ele = ele.lower() #conversion to lower case
    if ele in listA:
       if ele in listA_word_match_count: # returns true if a given key is there in the dictionary
          listA_word_match_count[ele] += 1 #increment the counter 
       else:
           listA_word_match_count[ele] = 1        

print (listA_word_match_count)    
print ("============================================================")
