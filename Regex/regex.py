# in Python, we use module re to work with regular expression
# a regular expression is a special text string used for
# describling a search pattern

# basic example
import re

pattern = r'cookie'
sequence = 'cookie'
if re.match(pattern, sequence):
    print("match")
else:
    print('not match')

# The match() function returns a match object if the text matches the pattern. Otherwise it returns None
# r'....' is a raw string literal. example: r"\n" is a string with \ and n character. while "\n" is a normal newline character
# Wild card Characters: Special characters #############


# . - A period, matches any single character except newline character
re.search(r'c.ok.e', 'cookie').group()  # print 'cookie'. the group() function return the string matched by re. 
# \w - Lowercase w, matches any single letter, digit or underscore
re.search(r'co\wk\we', 'cookie').group()  # print 'cookie'. 
# \W - Uppercase W, matches any character not part of \w
re.search(r'c\Wke', 'c@ke').group()  # print 'c@ke'
# \s - Lowercase s, matches a single whitespace character like: space, newline, tab, return
re.search(r'Eat\scake', 'Eat cake').group()  # print 'Eat cake'
# \S - Uppercase s, matches any character not part of \s
re.search(r'Cook\Se', 'Cookie').group()  # print 'Cookie'
# \t - Lowercase t, matches tab
re.search(r'Eat\tcake', 'Eat cake').group()  # print 'Eat\tcake'
# \n - Lowercase n, matches newline
# \r - Lowercase r, matches return
# \d - Lowercase d, matches decimal digit 0-9
re.search(r'c\d\dkie', 'c00kie').group()  # print 'c00kie'
# ^ - Caret, matches a pattern at the start of the string
re.search(r'^Eat', 'Eat cake').group()  # print 'Eat'
# $ - Matches a pattern at the end of string
re.search(r'cake$', 'Eat cake').group()  # print 'cake'
# [abc] - Matches a or b or c
# [a-zA-Z0-9] - Matches any letter from (a-z) or (A-Z) or (0-9). Characters that are not within a range
# can be matched by complementing the set. If the first character of set is ^, all the characters that
# are not in the set will be matched
re.search(r'Number: [0-6]', 'Number: 5').group()  # print 'Number: 5'
print(re.search(r'Number: [^5]', 'Number: 0').group())  # print 'Number: 0'
# \A - Uppercase a, matches only at the start of the string. Work across multiple lines as well
re.search(r'\A[A-E]ookie', 'Cookie').group()  # print 'Cookie'
# \b - Lowercase b, matches only the begining or the end of the word
re.search(r'\b[a-e]ookie', 'cookie').group()  # print 'cookie'
# \ - Backslash. If the character following the backslash is a recognize escape character
# the the special meaning of the term is taken. However, if not, the \ character is treated like
# any other character and pass through
re.search(r'Back\\stail', 'Back\stail').group()  # This checks for '\' in the string instead of '\t' due to the '\' used
