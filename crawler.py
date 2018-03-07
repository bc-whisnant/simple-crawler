from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.pythonforbeginners.com"

content = urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())



