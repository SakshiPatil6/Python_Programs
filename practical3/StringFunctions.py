string=str(input("Enter string: "))
print("String: ",string)

#Returns the number of times a specified value occurs in a string
x=str(input("Enter char to count its occurence: "))
print(string.count(x))

#Converts a string into lower case
print("Lower Case string: ",string.lower())

#Converts a string into upper case
print("Upper Case string: ",string.upper())

#Returns a string where a specified value is replaced with a specified value
s1=str(input("Enter string to replace: "))
s2=str(input("Enter string to display: "))
string1=string.replace(s1,s2)
print("Replace string: ",string1)

#Converts the first character to upper case
print("Capitalize words: ",string.capitalize())
