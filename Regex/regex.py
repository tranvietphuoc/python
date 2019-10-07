# in Python, we use module re to work with regular expression
# a regular expression is a special text string used for
# describling a search pattern

# basic example
import re


# pattern = r'cookie'
# sequence = 'cookie'
# regex = re.compile('\s+')
# if re.match(pattern, sequence):
#     print("match")
# else:
#     print('not match')

"""
BASIC SYNTAX:
.: One character except newline
\.: A period. \ escapes a special character
\d: One digit
\D: One non-digit
\w: One word character including digits
\W: One non-word character 
\s: One whitespace
\S: One non-whitespace
\b: Word boundary
\n: Newline
\t: Tab
==========================================
MODIFIERS
$: End of string
^: Start of string
ab|cd: Matches ab or de
[ab-d]: One character of: a, b, c, d
[^ab-d]: One character except: a, b, c, d
(): Items within parenthesis are retrieved
(a(bc)): Items within the sub-parenthesis are retrieved
==========================================
REPETITIONS
[ab]{2}: Exactly 2 continous occurrences of a or b
[ab]{2,5}: 2 to 5 continous occurrences of a or b
[ab]{2,}: 2 or more continous occurrences of a or b
+: One or more
*: Zero or more
?: 0 or 1
"""


s = r'\s+'
regex = re.compile(s)
text = """101 COM \t Computers
205 MAT \t Mathematics
309 ENG \t English"""

# re.sub()

print(re.sub(r'\s+', ' ', text))  # or
print(regex.sub(' ',text))  # substitute whitespaces in text with single space

# re.split()

print(re.split(r'\s+', text))  # or
print(regex.split(text))  # split text around 1 or more space characters

# re.findall()

regex_num = re.compile(r'\d+')
regex_char = re.compile(r'[A-Z]{3}')
regex_extra = re.compile(r'[A-Za-z]{4,}')
print(regex_char.findall(text))  # find all course codes
print(regex_extra.findall(text))  # find all course names
print(regex_num.findall(text))  # find all numbers within the text

# re.search()

text2 = """COM    Computers
205 MATH    Mathematics 189"""
s = regex_num.search(text2)

print(s)  # re.Match object
print('Starting position: ', s.start())
print('Ending position: ', s.end())
print(text2[s.start():s.end()])
print(s.group())  # equivalent to the line above

regex_string = r'([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
print(re.findall(regex_string, text))

# greedy matching regex

text_html = "<body>Regex Greedy Matching Example</body>"
print(re.findall('<.*>', text_html))  # print content of text_html
print(re.findall('<.*?>', text_html))
print(re.search('<.*?>', text_html).group())  # retrieve the first match 
