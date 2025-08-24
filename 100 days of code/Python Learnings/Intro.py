
#? Introduction to Python:

#* Python Print function:

print("Hello! World") # printing strings
print(30) # printing integers
print(3.5) # printing floats
print(True) # printing boolean


#* Python Data types:

a = "God!"
print(a, type(a))

b = 100
print(b, type(b))

c = 3.13
print(c, type(c))

d = False
print(d, type(d))

#* Print Statements in Python:

print("Hello World! I am Tanishq!")
# print("Hello Im a Tanishq!" \
# and my friends want to see me succeed in life") # EOl while scanning string literal.

#* Commenting in Python:
# Use cases of commenting.
'''
▷ Suppose you're working on a project and want to add a precaution line like:
"Deprecated method please don't use this method."
• Comments are added for this purpose so that this very line doesn't get executed by 
compiler and also you provide the necessary warning message for other users.

Example:
# Author: tvnisxq
# Programming Language: Python
'''

# This is a single-line comment.
print("This is a print statement.")



#* Escape sequence characters:
#? To insert characters that cannot be directly used in a string, we use an escape sequence character.

'''
\n character
print("I am a good boy\n& this viewer is also a good boy")
'''

'''
\" -> Double Quote backslash escape sequence character.
An escape sequence character is a backslash \ followed by the character you want to insert.

 
print("Hey Im a \"good boy\" and\nthe person using this repo is also a good boy/girl")
print("Hey Im a \'good boy\' and\nthe person using this repo is also a good boy/girl")
'''

#* Print Statements in python
#? Parameters used in print statements(2 & 4 are optional):
'''
1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. Default is sys.stdout
'''

print("hello", 3, 37)
print("hello", 3, 37, sep="~") # separator parameter of print statements
print("hello", 3, 37, end="009") # end parameter of print statements.
'''
Note: Null is also a valid argument for end.
\n can also be used along with end parameter input or argument.
'''
print("hello", 3, 37, end="009")  
print("Tanishq")
