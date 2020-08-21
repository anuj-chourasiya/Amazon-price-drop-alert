
import requests
import os.path
from bs4 import BeautifulSoup
import time
import json
import re
import smtplib
from Url_Agent import user_agent

global count
count=0
if os.path.exists("file_content.txt"): 
    os.remove("file_content.txt")

while True:

    Base_Url="http://anujchourasiya.com:8000"
    End_Point="/api"
    resp=requests.get(Base_Url+End_Point)
    data=resp.json()
    
    
    dict1={}
    #dictionary data for iteration
    for i in range(len(data)):
        
        email=data[i]['email']
        url=data[i]['url']
        #creating dictionary of specefic key for the first time
        if email not in dict1:
            dict1[email]={}
        dict1[email][url]=0

        
    dict2={}
    #dictionary data for storing data in a file
    for i in range(count,len(data)):
        
        
        email=data[i]['email']
        url=data[i]['url']
        if email not in dict2:
            dict2[email]={}
        dict2[email][url]=0
        #using count to see the no.of new urls added
        count+=1
        print("count",count)
    

    if  dict2:
                   
        with open('file_content.txt', 'a') as f:
            json.dump(dict2, f)
    #creating user agent to access amazon website from python program
    headers ={'User-Agent':'user_agent'}

    #iterating over emails
    for email,url_prize in dict1.items():

        #iterating over each urls in  email
        urls=dict1[email].keys()
        for url in urls:
           
            r = requests.get(url,headers=headers)
            
            data1=r.content
            soup=BeautifulSoup(data1,'html5lib')
            
            if (soup.select('#priceblock_ourprice')):
                
                d=soup.select('#priceblock_ourprice')[0].get_text().strip()
            else:
                d=soup.select('#priceblock_saleprice')[0].get_text().strip()
            p=d.split()[1]
            price=re.sub('[\,]','',p)
            print(price)
            print(email)
          
            if os.path.isfile('file_content.txt'):

                with open('file_content.txt','r') as fp:
                    obj=json.load(fp)
                
                
                read=float(obj[email][url])
                price=float(price)
                if(read==0):
                    obj[email][url]=price
                    with open('file_content.txt', 'w') as f:
                        json.dump(obj, f)

                elif price <read:
         
                   s = smtplib.SMTP('smtp.gmail.com', 587) 
                   s.starttls() 
                   s.login("******", "*******") 
                   message = "Dear customer your product prize  has been decreased to {} ".format(price)
                   s.sendmail("anujchourasiyadp@gmail.com", email, message) 
                   s.quit() 
                     
                else:
                    print("prize is still high\n")
                    


            

    time.sleep(20)

                                                     
