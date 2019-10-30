from bs4 import BeautifulSoup
import requests


req = requests.get('https://vi.wikipedia.org/wiki/Python_(ng%C3%B4n_ng%E1%BB%AF_l%E1%BA%ADp_tr%C3%ACnh)')
soup = BeautifulSoup(req.text, 'lxml')
# with open('./index.html') as f:
#     soup = BeautifulSoup(f, 'html.parser')

# print(soup.get_text())

for sub_heading in soup.find_all('a'):
    print(sub_heading.text)