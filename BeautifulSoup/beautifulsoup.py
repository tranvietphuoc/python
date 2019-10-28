from bs4 import BeautifulSoup


with open('./index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')



soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())


for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.title)
