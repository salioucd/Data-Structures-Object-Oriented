#Do not change the line of code below. It's at the top of
#the file to ensure that it runs before any of your code.
#You will be able to access french_dict from inside your
#function.
french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

#Write a function called french2eng that takes in one string
#parameter called sentence. french2eng should look at each
#word in the sentence and translate it into French if it is
#found in the dictionary, french_dict. If a word is not found
#in the dictionary, do not translate it: use the original
#word. Then, the function should return a string of the
#translated sentence.
#
#You may assume that the sentence you're translating has no
#punctuation. However, you should convert it to lower case
#before translating.
#
#For example:
#
#  french2eng("Hello it's me") -> "bonjour it's moi"
#
#Hint: Use .split() to get a list of strings representing
#each word in the string, then use ' '.join to merge the
#translated list back into one string.
#
#Hint 2: Remember, lists are mutable, so we can change
#individual items in the list. However, to change an item
#in a list, we must change it using its index. We can
#write lines like my_words[1] = new_word.
#
#Hint 3: If you're stuck, try breaking it down into small
#parts. How do you access an item from a list? How do you
#look up a key in a dictionary? How do you change the
#value of an item in a list? How do you check if a key is
#in the dictionary?


#Write your function here!
def french2eng(sentence):
    english_words = sentence.split()
    french_words = []
    for word in english_words:
        word = word.lower()
        if word in french_dict:
            french_words.append(french_dict[word])
        else:
            french_words.append(word)
    return ' '.join(french_words)


#There are a few different ways to do this. We'll show two:
#one using join(), one using string concatenation. We'll
#start with the join() method.

def french2eng(sentence):
    
    #First we need to convert the sentence to lower-case:
    
    sentence = sentence.lower()
    
    #Next we need to split it by spaces:
    
    sentence_split = sentence.split(" ")
    
    #Next we need to iterate through each word. For this
    #method, though, we want to change the actual values
    #of the items in sentence_split, and as the hint
    #suggests, we can only do that by accessing them via
    #their index. So, we have to use a for loop:
    
    for i in range(len(sentence_split)):
        
        #Next, for each word in sentence_splits, we want
        #to check if it's in french_dict. If it is, we
        #want to replace the current word with the value
        #associated with it in french_dict:
        
        if sentence_split[i] in french_dict:
            sentence_split[i] = french_dict[sentence_split[i]]
        
        #We could also do this with a try-except that
        #attempts to perform the operation on line 34, and
        #if it fails due to a KeyError, does not change the
        #word.
    
    #At the conclusion of that loop, sentence_split is a
    #list of words from the original sentence, but any
    #words that were in french_dict have been replaced by
    #their french translation. So, now we just need to
    #join them back up into one string and return them:
    
    return " ".join(sentence_split)

    #If the list indices or join() method are throwing you
    #off, though, check out sample_answer_2.py for an
    #approach that uses a for-each loop without the join()
    #method.
    


#The alternative is that instead of changing the list and
#joining it at the end, we could build up our string to
#return over time. We'll have to deal with an extra space,
#but that's not a big deal:

def french2eng(sentence):
    
    #First we still need to convert the sentence to
    #lower-case:
    
    sentence = sentence.lower()
    
    #Next we still need to split it by spaces:
    
    sentence_split = sentence.split(" ")
    
    #This time, we're going to build up the correct string
    #over time. So, we need to start with an empty string
    #to which to add over time:
    
    result = ""
    
    #Now, we iterate through each string in the sentence...
    
    for word in sentence_split:
        
        #And if it's in french_dict, we add its translation
        #to our ongoing string:
        
        if word in french_dict:
            result += french_dict[word]
        
        #If it's not in the dictionary, then we just add the
        #original word:
        
        else:
            result += word
            
        #Then, we add a space so the words aren't all crammed
        #together:
        
        result += " "
        
    #At the end, we can return result.strip(), which strips
    #off any line breaks or spaces from either end of the
    #string:
    
    return result.strip()
    
 








#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: bonjour it's moi
print(french2eng("Hello it's me"))




