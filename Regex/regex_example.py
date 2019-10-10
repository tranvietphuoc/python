import re


email = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

pattern1 = r'(^\w+)@([a-z0-9]+)\.([a-z]{2,4})'
regex = re.compile(pattern1)
# print(regex.findall(email,flags=re.IGNORECASE))
print(re.findall(pattern1, email, flags=re.IGNORECASE))

text = """Betty bought a bit of butter, 
But the butter was so bitter, 
So she bought some better butter, 
To make the bitter butter better."""

pattern2 = r'\bb\w+'
print(re.findall(pattern2, text, flags=re.IGNORECASE))


def is_allowed_specific_char(string):
    pattern = r'[^a-zA-Z0-9.]'
    CharReg = re.compile(pattern)
    string = CharReg.search(string)
    return bool(string)


print(is_allowed_specific_char('ABCabc098.'))


def is_followed_by_b1(string):
    pattern = r'ab*?'  # a has followed by zero or more b
    string = re.search(pattern, string)
    return bool(string)


print(is_followed_by_b1('abbbbc'))


def is_followed_by_b2(string):
    pattern = r'ab+?'  # a has followed by one ore more b
    string = re.search(pattern, string)
    return bool(string)


print(is_followed_by_b2('accccc'))


def pattern_match1(string):
    pattern = r'a.*?b$'  # a is followed by anything, end with b
    return bool(re.match(pattern, string))


print(pattern_match1('aasdkjasd8b'))  # true


def pattern_match2(string):
    pattern = r'^\w.*'  # begining with a word
    return bool(re.search(pattern, string))


print(pattern_match2('grg,fsfklsf'))


def pattern_match3(string):
    pattern = r'\w*\S$'  # word end of string, with optional punctuation
    return bool(re.search(pattern, string))


print(pattern_match3('sdadasd.'))


def pattern_match4(text):
    pattern = r'(\w*z.\w*)+'  # words containing 'z'
    return bool(re.search(pattern, text))


print(pattern_match4('adasdasdad'))


def pattern_match5(text):
    pattern = r'\bz\b'
    return bool(re.search(pattern, text))


print(pattern_match5('adadhhhxh'))


pattern2 = r'\bb\w+'
print(re.findall(pattern2, text, flags=re.IGNORECASE))
