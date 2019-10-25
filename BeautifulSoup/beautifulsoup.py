from bs4 import BeautifulSoup


with open('./index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

print(soup.get_text())
