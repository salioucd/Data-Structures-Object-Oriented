#Write a function called grade_scantron. grade_scantron should
#take as input two lists: answers and key. Each list contain
#strings. Each string will be only one letter, a character
#from A to E. grade_scantron should return how many questions
#the student got "right", where a student gets a question
#right if their answer for a problem matches the answer key.
#
#In other words, if value of the first item in answers matches
#the value of the first item in key, the student gets a point.
#If it does not, the student does not get a point.
#
#If the lists do not have the same number of items, return
#-1 to indicate that the answer key did not belong to the
#same test as the student's answers.\
#
#Hint: in the past, lots of people have tried to do this using
#the index() method. That won't work! You'll need to track the
#index yourself.

def grade_scantron(answers, key):
    
    #To start, if the lists aren't the same length, we can
    #go ahead and quit: we know what the answer will be.
    
    if not len(answers) == len(key):
        return -1
    
    #If the lists weren't the same length, then the function
    #ended on line 7. That's why we don't have to bother
    #with an else: we can only reach the code below if the
    #lists are the same length.
    #
    #Next, we want to keep a tally of how many problems the
    #student has gotten right:
    
    score = 0
    
    #Now for the bulk of the reasoning. It's tempting to use
    #two loops, but we don't need two: we want to compare the
    #items in the same spot in the two lists, so we use one
    #loop. Then, we put i into each list to find the item at
    #each index:
    
    for i in range(len(answers)):
        
        #i starts at 0 and goes until the last element of
        #the lists. We want to compare the answers in the
        #same spot:
        
        if answers[i] == key[i]:
            
            #And if they're the same, increment the score:
            
            score += 1
    
    #Then, after we're done (note the lack of indentation),
    #return the score:
    
    return score


test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))
