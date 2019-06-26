# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:22:08 2019
Webscraper for 2700chess.com
Used to show live ratings of the top chess players
@author: Richard Chen 
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

#my_url = input('Which chess ratings would you like to view? Male:(M) , Male Top 100(M2), Female(F), Female Top 50 (F2):')
#while(my_url!='M' and my_url!='M2' and my_url!='F' my_url!='F2"')
#my_url = input('Invalid option! Which chess ratings would you like to view? Male:(M) , Male Top 100(M2), Female(F), Female Top 50 (F2)')

#if my_url=='M':
my_url= 'https://2700chess.com/'
#    my_url= 'https://2700chess.com/?per-page=100'
#elif my_url=='F':
   # my_url= 'https://2700chess.com/women'
#elif my_url=='F2':
 #   my_url=='https://2700chess.com/women'
    
# Opening up connection, grabbing the page
uClient = req(my_url)
#off loads the contnt into a variable
page_html= uClient.read()
#Close the content 
uClient.close()

#leader_count = 0 
#top_tencount = 0 
#all_line_count = 0 

page_soup= soup(page_html,"html.parser")
#searches for the tbale body from 2700 chess
B= page_soup.findAll('tbody')
#an Array that has all of the information from the site 
C= B[0].findAll('tr')   
print("Top Players")
for index, value in enumerate(C):
    print(str(index+1) +' ' + C[index].a.text)
    
#get the lenght of the number of top players
#len(C)

#table = page_soup.findAll("div")
    
    