#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!

#course_info function
def course_info(my_tuple):
    names = [] #list to store names
    age = [] #list to store age
    my_dict = {} #empty dictionary
    
    for i in range(len(my_tuple)): #iterating over the tuple
        names.append(my_tuple[i][0]) # store names in names list
        age.append(my_tuple[i][1]) #store age in age list
    
    average_age = sum(age)/len(age) # calculate the average age
    my_dict['students'] = names # add student names to the dictionary
    my_dict['avg_age'] = average_age # add average add to the dictionary
    
    return my_dict # return the dictionary
  
  #-----------------------------------------------------------------------------------------------------------------
  
  def course_info(student_list):
    
    #There are two high-level ways we can do this: we could
    #create the list and float first, and create the
    #dictionary last; or, we could create the dictionary
    #first and change it directly.
    #
    #The first one is probably a little easier, so let's
    #start there. First, we create an empty list for the
    #student names, and a sum to add up all their ages:
    
    students = []
    total_age = 0
    
    #Then, we want to iterate through the list of tuples:
    
    for student_tuple in student_list:
        
        #For each one, we want to add the name to the list
        #and add the age to total_age. To make this easier,
        #let's first unpack the tuple. Remember, the name
        #is first and the age is second:
        
        student_name, student_age = student_tuple
        
        #This unpacks the first item of student_tuple to
        #student_name, and the second item to student_age.
        #
        #Now, let's add student_name to the list:
        
        students.append(student_name)
        
        #...and add the age to total_age:
        
        total_age += student_age
        
    #That's all we need to do inside the loop! When the
    #loop is done running, students will be a list of all
    #the names, and student_age will be the sum of their
    #ages. Now all we need to do is divide student_age by
    #the number of students, and then create the dictionary.
    #We can do this all at once:
    
    student_info = {"students": students, "avg_age": total_age/len(student_list)}
    
    #We can do that calculation for avg_age in-line, or we
    #could separate it out into a separate calculation.
    #
    #Finally, we return our result:
    
    return student_info
  
            

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'avg_age': 20.5, 'students': ['Jackie', 'Marguerite']}
print(course_info([("Jackie", 20), ("Marguerite", 21)]))
