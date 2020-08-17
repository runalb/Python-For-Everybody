import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
pos = int(input("Enter position:"))

print("Retrieving:",url)
for i in range(0,count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cn = 0
    ps = 0
    for tag in tags:
        ps = ps +1
        if ps == pos:
            print("Retrieving:", str(tag.get('href',None)))
            url = str(tag.get('href',None))
            ps = 0
            break
