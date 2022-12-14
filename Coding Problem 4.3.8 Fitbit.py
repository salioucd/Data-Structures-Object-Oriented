#Imagine you're writing some code for an exercise tracker.
#The tracker measures heart rate, and should display the
#average heart rate from an exercise session.
#
#However, the tracker doesn't automatically know when the
#exercise session began. It assumes the session starts the
#first time it sees a heart rate of 100 or more, and ends
#the first time it sees one under 100.
#
#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).
#
#You may assume that the list will only cross the 100 beats
#per minute threshold once: once it goes above 100 and below
#again, it will not go back above.


#Add your function here!


def average_heart_rate(rates):
    
    #As we go through the heart rates, we're going to need to
    #keep track of three things: as usual with calculating an
    #average, we need a sum and a count:
    total = 0
    count = 0
    
    #But we also need to track whether the current heart rate
    #should be included in the average. The problem says we'll
    #always start out below 100 beats, so we always start by
    #_not_ counting these measurements in our average:
    measuring = False
    
    #Now, we iterate through each rate in the list...
    for rate in rates:
        
        #And we first check to see if it's time to start
        #measuring. If the current rate is over 100, then we
        #set measuring to True:
        if rate >= 100:
            measuring = True
        
        #Imagine, though, that we have been measuring, and we
        #just encountered our first value less than 100. That
        #means we should stop measuring:
        else:
            measuring = False
        
        #Because we assume that the values over 100 are all
        #consecutive, we can check this every time: we don't
        #need to worry about whether we've gone over and under
        #once before.
        #
        #Now, if we're measuring, we add the current rate to
        #our running total, and 1 to our current count:
        if measuring:
            total += rate
            count += 1
    
    #After going through all the rates, we return the average.
    #Remember, the instructions said to use floor division for
    #this:
    return total // count


#This is the harder way to do this, but it's more in line with
#the instructions. For the easier way, see sample_answer_2.py.

def average_heart_rate(rates):
    
    #We initialize our counters:
    total = 0
    count = 0
    
    #We iterate through the rates as before:
    for rate in rates:
        
        #But instead of keeping track of a measuring variable,
        #we instead just check each value individually:
        if rate >= 100:
            total += rate
            count += 1
        
    #Then, we return the average:
    return total // count



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
