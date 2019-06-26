# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:22:08 2019
Webscraper for 2700chess.com
Used to show live ratings of the top chess players
@author: Richard Chen 
"""
#Framework used to parse HTML
from bs4 import BeautifulSoup as soup
# Used to grab the URL
from urllib.request import urlopen as req
#Prompts user to select chess ratings list to be viewed
my_url = input('Which chess ratings would you like to view? Male:(M) , Male Top 100(M2), Female(F), Female Top 50 (F2):')
#Prompters user to input again if user does not enter any of the lists
while(my_url!='M' and my_url!='M2' and my_url!='F' and my_url!='F2"'):
    my_url = input('Invalid option! Which chess ratings would you like to view? Male(M) , Male Top 100(M2), Female(F), Female Top 50 (F2):')
#Assorted urls for each of the lists 
if my_url=='M':
    my_url= 'https://2700chess.com/'
elif my_url=='M2':
    my_url= 'https://2700chess.com/?per-page=100'
elif my_url=='F':
    my_url= 'https://2700chess.com/women'
elif my_url=='F2':
    my_url='https://2700chess.com/women?per-page=50'
# Opening up connection, grabbing the page
uClient = req(my_url)
#Stores the content into a variable
page_html= uClient.read()
#Close the content 
uClient.close()
#Html parser
page_soup= soup(page_html,"html.parser")
#searches for the table body from 2700chess
B= page_soup.findAll('tbody')
#array that has all of the player's information from the site 
C= B[0].findAll('tr') 
#Header  
#Testing for the lengthh of the number of top players on each url
#len(C)
print("Top Players")
#For loop that wil print the list of all of the players
for index, value in enumerate(C):
    #Searching through HTML for hidden searched tag
    search = C[index].findAll('span',{"class":"hidden searched"})
    #Location of player's name
    name = search[0].next
    #Location of player's country 
    country = search[1].text
    #Output plaer's name
    print((str(index+1) +' ' + name +' '),end='')
    #Search for player's rating
    search_rating = C[index].findAll('td',{'class':'live_standard_rating'})
    #Location of player's rating
    rating = search_rating[0].strong.text
    #Output player's rating
    print (country +' '+ 'Rating:' + rating)

    
    