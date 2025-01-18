# In python, we use variables to store values.
# Variables are like containers that hold values.
message = "Hello, python interpreter!"
print(message)

# And we can change the value of a variable.
message = "Hello, world!"
print(message)

# Names of variables must start with a letter or an underscore.
# They can contain letters, numbers and underscores.
# They are case-sensitive.
# They should be descriptive.
message = "one simple message"
print(message)
message = "another simple message"
print(message)

# We cam modify the upper or lower case of a string.
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# We can combine strings using the + operator.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# We can add whitespace to strings with tabs or newlines.
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

# We can strip whitespace from strings.
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())
favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())

# We can use single or double quotes to define strings.
quote = "Albert Einstein once said, 'A person who never made a mistake never tried anything new.'"
print(quote)
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)

# We can use the str() function to convert numbers to strings.
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# We can use the int() function to convert strings to numbers.
age = "23"
print(age)
print(int(age))
