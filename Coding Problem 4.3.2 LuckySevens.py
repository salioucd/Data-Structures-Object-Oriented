#Write a function, called lucky_sevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.


#Write your function here!
def lucky_sevens(li):
    n=len(li)
    for i in range(n):
        if(len(li)>=3 and i<n-1 and i<n-2):
            if(li[i]==7 and li[i+1]==7 and li[i+2]==7):
                return True
    return False




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))


#Sample Answer 1
#There are a lot of different ways we could do this. Let's
#look at three: a for loop, a for-each loop, and an advanced
#method. We'll start with the for loop.

def lucky_sevens(a_list):
    
    #The goal of using a for loop is to give us access to the
    #indices of each item in the list. There are three
    #consecutive 7s in the list if the current item is 7, the
    #next item is 7, and the one after it is 7. So, if we use
    #a for loop, we can check all three indices.
    #
    #First, we iterate over each character in the list:
        
    for i in range(len(a_list) - 2):
        
        #Note that we stop two characters from the end. Why?
        #Well, if we haven't found three consecutive 7s by
        #the time we get to the second-to-last item, then
        #we're not going to: there can't be three straight 7s
        #in the last two items. Plus, if we try to check the
        #next item when we're already checking the last item,
        #an error will arise.
        #
        #Next, we could use an and statement, or some nested
        #conditions. Let's do the latter. First we ask, is the
        #current character a 7?
                
        if a_list[i] == 7:
            
            #If it was, is the next character a 7?
            
            if a_list[i+1] == 7:
                
                #If it was, is the character *after* that a 7?
                
                if a_list[i+2] == 7:
                    
                    #If so, we're done! We found three straight
                    #7s!
                    
                    return True
                
    #Then, the only way we reach the line below is if we never
    #returned True above. So, if we reach the end of that loop
    #and haven't exited the function, then we didn't find three
    #straight 7s:
    
    return False


#What about with a for-each loop? Check out sample_answer_2.py to
#see!

print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))




#Sample Answer 2
#Now let's try it with a for-each loop.

def lucky_sevens(a_list):
    
    #The challenge with using a for-each loop is that we have
    #no way to look up the next character in the string because
    #we don't have the index of the character we're looking at.
    #We could track it manually, but then we're basically just
    #doing a for loop.
    #
    #Instead, let's keep a counter of how many consecutive 7s
    #we have found so far:
    
    consecutive_7s = 0
    
    #Now, we loop through the items in the list:
        
    for num in a_list:
        
        #If this is a 7, we want to increment the number of
        #consecutive 7s we've found:
        
        if num == 7:
            consecutive_7s += 1
        
        #If it isn't, then we need to reset our counter of
        #consecutive 7s to 0 -- otherwise we're counting the
        #total number of 7s, not the consecutive ones:
        
        else:
            consecutive_7s = 0
        
        #Now, that means that if we find three 7s in a row,
        #but then find something else, consecutive_7s will
        #be reset to 0. So, we need to check if we've found
        #three straight inside the loop:
        
        if consecutive_7s == 3:
            return True
        
        #Note that this could have been placed inside the
        #conditional on line 23 as well: it can't be true
        #unless the current item is 7.
        
                
    #Then, same as before, the only way we reach the line below
    #is if we never returned True above. So, if we reach the end
    #of that loop and haven't exited the function, then we didn't
    #find three straight 7s:
    
    return False


#Those are two ways to do this with a loop. However, there's
#another way you might have thought of, but couldn't get to work.
#Let's see how that works.


print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))




#Sample Answer 3

#When you were first thinking about this problem, you might have
#thought, "Well if I merge them all into a string, I can just
#do return "777" in a_list_as_string". You might have also
#thought, "I can do ''.join(a_list) to convert it to a string!"
#
#If you tried that, clever! However, you found that it wouldn't
#work. join() only works on lists of strings. You could have
#then run a loop on each item in a_list, converting it to a
#string, and then returning "777" in a_list, as shown below:
#
#def lucky_sevens(a_list):
#    
#    for i in range(len(a_list)):
#        a_list[i] = str(a_list[i]))
#    return "777" in a_list
#
#However, the problem here is that you're modifying the list.
#Remember, lists are mutable, so this actually changes the values
#of the list. We probably didn't want to do that. Instead, we
#can make use of a handy Python function called map():

def lucky_sevens(a_list):
    
    #map() takes two arguments: a function and a list. It returns
    #a new list created by applying that function to each item in
    #that list:
    
    a_list_as_strings = map(str, a_list)
    
    #So, this effectively duplicates the code in the comment above,
    #but without changing a_list. It applies the function str() to
    #each item in a_list, and returns a list of the results.
    #
    #Then, we can check if "777" is in the result of joining that
    #list of strings:
    
    a_list_as_one_string = "".join(a_list_as_strings)
    return "777" in a_list_as_one_string

    #All of which could becompressed down to one line:
    #return "777" in "".join(map(str, a_list))


#Don't worry if this is confusing -- the map() function is a little
#out of scope for our material. Note, though, that if you had Googled
#"Python join list of ints", you'll find an answer that explains how
#to use the function. If you need to do something you don't know how
#to do, search for a solution!


print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))




