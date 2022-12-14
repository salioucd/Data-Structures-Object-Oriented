#Recall in an earlier problem you were given two lists: one
#list was a student's answers to a test, and the other was
#the answer key. Your goal was to return a score
#representing the number of problems the student got correct.
#
#Let's do that again, but with dictionaries instead of lists.
#Write a function called calculate_score. calculate_score
#should take two parameters: a dictionary of student answers
#and a dictionary of correct answers. Both dictionaries should
#have integers as their keys, and one-character strings as
#their values.
#
#calculate_score should count how many questions the student
#got right. Or, in more precise terms, calculate_score should
#count how many keys for which the associated value is the
#same in the student's dictionary and in the answer key
#dictionary.
#
#As before, it is possible that there will be more answers in
#one than the other. This means that these answers don't
#belong to the same test! If that happens, return -1.


#Add your function here!
def calculate_score(student_answers, correct_answers):
    if len(student_answers) != len(correct_answers):
        return -1
    count = 0
    for question in student_answers:
        if question not in correct_answers:
            return -1
        if student_answers[question] == correct_answers[question]:
            count += 1
    return count

#----------------------------------------------------------------------------------

#-----------------------------------------------------------
#First, we define the function:
def calculate_score(student, correct):
    
    #Next, I'm going to check to see if the lengths of the
    #two dictionaries are the same. If not, we'll go ahead
    #and return -1:
    if not len(student) == len(correct):
        return -1
    
    #You might be tempted to do this with error handling, and
    #you'd be pretty close: after all, if we try to access a
    #key that doesn't exist in one dictionary, then an error
    #will occur, and we could handle that and return -1.
    #
    #The problem with that approach is: how do we know which
    #dictionary to iterate through? If we iterate through the
    #shorter one, then we'll never try to access a key that
    #doesn't exist because we're not checking the keys of the
    #longer one. So, it's better to just handle this case
    #manually.
    
    #Next, since we're counting something, we'll initialize a
    #counter:
    total = 0
    
    #Now, we want to iterate through all the key-value pairs in
    #either dictionary. It doesn't really matter which, so I'll
    #go through the student's:
    for (question, answer) in student.items():
        
        #With this loop, we know that 'answer' is the student's
        #answer to the question given by 'question'. So, we need
        #to see if the answer corresponding to the same key from
        #the answers is the same.
        #
        #Here's how we can do that:
        if answer == correct[question]:
            
            #That simple line is somewhat complex. answer is the
            #answer we already know the student put. correct is
            #the dictionary of correct answers. question is the
            #number of the problem, which we can use as a key to
            #the correct dictionary to find its value for that
            #question.
            #
            #If they're the same, we add one to the score:
            total += 1
    
    #And at the end, we return the total score:
    return total

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))




