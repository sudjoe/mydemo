# 1st : printing printing
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about "))


# Here's some new strange stuff, remember type it exactly.
# 2nd : Printing Printing Printing
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan \nFeb \nMar \nApr \nMay \nJun \nJul \nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


# 3rd

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# 4th

print("How old are you?", end =' ')
age = input()
print("How tall are you?", end =' ')
height = input()
print("How much do you weigh?", end =' ')
weight = input()
print(f'So, youre {age} old, {height} tall and {weight} heavy.')
