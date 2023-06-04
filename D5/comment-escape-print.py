#This is a 'Single-Line Comment'
print("This is a print statement.")

print("Hello World !!!") #Printing Hello World

print("Python Program")
#print("Python Program")

#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
    


"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# print("This doesnt "execute")
print("This will \" execute")

"""
print(object(s), sep=separator, end=end, file=file, flush=flush)
Other Parameters of Print Statement
1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. Default is sys.stdout
Parameters 2 to 4 are optional
"""