#Webscraping Tutorial from https://www.youtube.com/watch?v=XQgXKtPSzUI
#will grab URL
from urllib.request import urlopen as uReq
#will parse html text
from bs4 import BeautifulSoup as soup 

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# Opening up connection, grabbing the page
uClient = uReq(my_url)
#off loads the contnt into a variable
page_html= uClient.read()
#Close the content 
uClient.close()
#html parsing 
page_soup = soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"item-container"})
container = containers[0]
divWithInfo=containers[0].find("div","item-info")
#Finds the div with the title and image 
for container in containers:
    brand = container.find("div","item-info").img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    print("brand: "+ brand)
    print("product_name: :"+product_name)
    print("shipping: " + shipping)