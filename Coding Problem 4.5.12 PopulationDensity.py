#Write a function called population_density. The function
#should take one parameter, which will be a list of
#dictionaries. Each dictionary in the list will have three
#key-value pairs:
#
# - name: the name of the country
# - population: the population of that country
# - area: the area of that country (in km^2)
#
#Your function should return the population density of all
#the countries put together. You can calculate this by
#summing all the populations, summing all the areas, and
#dividing the total population by the total area.
#
#Note that the input to this function will look quite long;
#don't let that scare you. That's just because dictionaries
#take a lot of text to define.


#Add your function here!
def population_density(dictionary_list):


    total_population= 0

    total_area= 0

    for country in dictionary_list:

           total_population += country['population']

           total_area += country['area']

    population_density = total_population / total_area

    return population_density
  
  #------------------------------------------------------------
  
  #-----------------------------------------------------------
#First, we define the function:
def population_density(nations):
    
    #While this problem sounds different, really all we're
    #doing is calculating an average, just like we've done
    #before. The only difference is that instead of dividing
    #a sum by a count, we're dividing a population by an
    #area. So, we'll create initial counters for both:
    total_population = 0
    total_area = 0
    
    #Then, we'll iterate through each nation in the list:
    for nation in nations:
        
        #For each nation, we want to add its population to
        #the running total population. We can access that
        #with nation["population"] -- nation is the current
        #nation, which is a dictionary with the keys "name",
        #"population", and "area":
        total_population += nation["population"]
        
        #We can do the same thing with area, and add its area
        #to the running total area:
        total_area += nation["area"]
        
    #At the end, we return the population divided by the
    #area:
    return total_population / total_area


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))
