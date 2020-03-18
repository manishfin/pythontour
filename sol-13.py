# Ex-15
# Use urllib2 module to get html content from this link:
# http://www.mattmakai.com/links-learning-web-fundamentals.html
# Python has beautifulsoup library to parse html.
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Print all anchor tags, exclude relative links

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mattmakai.com/links-learning-web-fundamentals.html")
soup = BeautifulSoup(html, 'html.parser')
links = [link for link in soup.find_all('a') if not link.get('href').startswith('/')]
print(links)