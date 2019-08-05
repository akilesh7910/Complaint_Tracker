from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url='https://it.trustpilot.com/review/www.sella.it?page=2'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers= page_soup.findAll("div",{"class" : "review-card"})

filename = "bS_complaints1.csv"
f = open(filename,"w")

headers = "name, review\n"

f.write(headers)


for container in containers:
    
    name_container = container.findAll("aside",{"class":"review__consumer-information"})
    name=name_container[0].a.div.div.text.strip()
    
    review_container = container.findAll("article",{"class":"review"})
    review=review_container[0].section.div.p.text.strip()
    
    

    print("\nname:" +name)
    print("\nreview:" +review)
    
    f.write(name + "," + review + "\n")

f.close()
    

    
    
