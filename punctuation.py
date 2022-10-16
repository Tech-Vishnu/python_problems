# Punctuations are defined here
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Getting input from user
my_str = input("Enter the string:")


no_punct = "" #Base string to which the final string with no punctuations is added
for char in my_str: #Iterating through every character in string
   if char not in punctuations:  # Removing punctuations from string
       no_punct = no_punct + char  #Adding characters by neglecting all punctuations

print(no_punct) #Displaying the final string without punctuations
