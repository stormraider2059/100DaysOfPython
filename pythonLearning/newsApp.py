#News App built using the News API. All the news contents are fetched from the API. Copyright newsapi.org @2023. All rights reserved.
#I am publishing this to GitHub for educational purposes only. Do not use my API key for commercial purposes.

import requests 
import json

url1=('https://newsapi.org/v2/everything?q=tesla&from=2023-07-26&sortBy=publishedAt&apiKey=86413db0a963461f87b99d25090ac2ee')
url2=('https://newsapi.org/v2/everything?q=apple&from=2023-08-25&to=2023-08-25&sortBy=popularity&apiKey=86413db0a963461f87b99d25090ac2ee')
url3=('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=86413db0a963461f87b99d25090ac2ee')
url4=('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=86413db0a963461f87b99d25090ac2ee')
url5=('https://newsapi.org/v2/everything?domains=wsj.com&apiKey=86413db0a963461f87b99d25090ac2ee')

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)
response5 = requests.get(url5)

data1=json.loads(response1.text)
data2=json.loads(response2.text)
data3=json.loads(response3.text)            
data4=json.loads(response4.text)
data5=json.loads(response5.text)

def TeslaNews():
    print("**Tesla News**\n")
    print("Total Results:\n",data1['totalResults'])               
    print("Author:\n",data1['articles'][0]['author'])               
    print("Title:\n",data1['articles'][0]['title'])
    print("Description:\n",data1['articles'][0]['description'])
    print("URL:\n",data1['articles'][0]['url'])
    print("Published At:\n",data1['articles'][0]['publishedAt'])
    print("Content:\n",data1['articles'][0]['content'])
    print("\n------------------------------------------------------------\n")

def AppleNews():
    print("**Apple News**\n")
    print("Total Results:\n",data2['totalResults'])               
    print("Author:\n",data2['articles'][0]['author'])               
    print("Title:\n",data2['articles'][0]['title'])
    print("Description:\n",data2['articles'][0]['description'])
    print("URL:\n",data2['articles'][0]['url'])
    print("Published At:\n",data2['articles'][0]['publishedAt'])
    print("Content:\n",data2['articles'][0]['content'])
    print("\n------------------------------------------------------------\n")
    
def BusinessNews():
    print("**Business News**\n")
    print("Total Results:\n",data3['totalResults'])               
    print("Author:\n",data3['articles'][0]['author'])               
    print("Title:\n",data3['articles'][0]['title'])
    print("Description:\n",data3['articles'][0]['description'])
    print("URL:\n",data3['articles'][0]['url'])
    print("Published At:\n",data3['articles'][0]['publishedAt'])
    print("Content:\n",data3['articles'][0]['content'])
    print("\n------------------------------------------------------------\n")
    
def TechCrunchNews():
    print("**TechCrunch News**\n")
    print("Total Results:\n",data4['totalResults'])               
    print("Author:\n",data4['articles'][0]['author'])               
    print("Title:\n",data4['articles'][0]['title'])
    print("Description:\n",data4['articles'][0]['description'])         
    print("URL:\n",data4['articles'][0]['url'])
    print("Published At:\n",data4['articles'][0]['publishedAt'])
    print("Content:\n",data4['articles'][0]['content'])
    print("\n------------------------------------------------------------\n")
    
def WallStreetJournalNews():
    print("**Wall Street Journal News**\n")
    print("Total Results:\n",data5['totalResults'])               
    print("Author:\n",data5['articles'][0]['author'])               
    print("Title:\n",data5['articles'][0]['title'])
    print("Description:\n",data5['articles'][0]['description'])
    print("URL:\n",data5['articles'][0]['url'])
    print("Published At:\n",data5['articles'][0]['publishedAt'])
    print("Content:\n",data5['articles'][0]['content'])
    print("\n------------------------------------------------------------\n")
    
print("\n********** Welcome to the News App! We use the News API to get the latest news from around the world. **********\n")

def newsChoice():
    print("What type of news do you want to read? \n1. Tesla News \n2. Apple News \n3. Business News \n4. TechCrunch News \n5. Wall Street Journal News\n6. Exit\n")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        TeslaNews()
        newsChoice()
    elif choice == 2:
        AppleNews()
        newsChoice()
    elif choice == 3:
        BusinessNews()
        newsChoice()
    elif choice == 4:
        TechCrunchNews()
        newsChoice()
    elif choice == 5:
        WallStreetJournalNews()
        newsChoice()
    elif choice == 6:
        print("Thank you for using the News App!\n")
        exit(0)
    else:
        print("Invalid Choice! Please choose a number between 1 and 5.\n")
        newsChoice()
        
newsChoice()