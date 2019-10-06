import re


email = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

pattern1 =  r'(^\w+)@([a-z0-9]+)\.([a-z]{2,4})'
regex = re.compile(pattern1)
# print(regex.findall(email,flags=re.IGNORECASE))
print(re.findall(pattern1, email, flags=re.IGNORECASE))

text = """Betty bought a bit of butter, 
But the butter was so bitter, 
So she bought some better butter, 
To make the bitter butter better."""
pattern2=r'\bb\w+'
print(re.findall(pattern2, text, flags=re.IGNORECASE))