# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:56:29 2020

@author: pooja
"""

import json
from os import path
import time


def write(data, filename='data.json'):
    with open("data.json",'w') as file:
            json.dump(data,file,indent=4)
            
def check(data):
 for key,value in data.items():    # items on Py 3k
      for k,v in value.items():
        if k=="Ctime":  
          return k
          break            
            
def TTL(data):
   
    h=data
   
    for key in list(h):    # items on Py 3k
      for k in list(h[key]):
        if k=="toTime":
           n3=check(h)
           n=h[key][n3]
           n1=n+h[key][k]
           if n1<time.time():
               del h[key]
               write(h)
               break
           else:
               break
         
            
b='y'            
while b=='y':
  print("\nEnter your choice:")
  print("\t1)Create\n\t2)Read\n\t3)Delete")
  ch=input("enter:")

  if ch=='1':
    
    i=input("Do you want to apply time to live on key?? y/n:")
    if(i=='n'):
     if not path.exists('data.json'):
                data={}
                ch1=input("enter the key:")
                ch2=input("enter the name:")
                ch3=input("enter the roll:")
                ch4=input("enter the dpt:")
                ch5=input("enter the year:")
                data={ch1:{"name":ch2,"roll":ch3,"dpt":ch4,"year":ch5}}
                write(data)   
                
     else:
     
               a='y'
               while a=='y':
                   with open("data.json") as file:
                    p=json.load(file)
                    ch1=input("enter the key:")
                    if ch1 in p:
                        print("key is already exist!!!!  use another key")
                    else:    
                        ch2=input("enter the name:")
                        ch3=input("enter the roll:")
                        ch4=input("enter the dpt:")
                        ch5=input("enter the year:")
                        data={ch1:{"name":ch2,"roll":ch3,"dpt":ch4,"year":ch5}}
                        p.update(data)
                        write(p)
                   a=input("do you want to add more key? y/n:")
    
    else: 
        if not path.exists('data.json'):
                data={}
                t=time.time()
                ch1=input("enter the key:")
                ch2=input("enter the name:")
                ch3=input("enter the roll:")
                ch4=input("enter the dpt:")
                ch5=input("enter the year:")
                print("to time:\n")
                print("\t1)In seconds\n\t2)In minutes\n\t3)In Hours\n\t4)In Days")
                c1=input("Enter:")
                if c1=='1':
                    tt=int(input("enter seconds:"))
                elif c1=='2':
                    t1=int(input("enter minutes:"))
                    tt=60*t1
                elif c1=='3':
                    t1=int(input("enter hours:"))
                    tt=60*60*t1
                elif c1=='4':
                    t1=int(input("enter days:"))
                    tt=60*60*24*t1
                data={ch1:{"name":ch2,"roll":ch3,"dpt":ch4,"year":ch5,"Ctime":t,"toTime":tt}}
                write(data)   
                
        else:
     
               a='y'
               while a=='y':
                   with open("data.json") as file:
                    p=json.load(file)
                    t=time.time()
                    ch1=input("enter the key:")
                    if ch1 in p:
                        print("key is already exist!!!!  use another key")
                    else:    
                        ch2=input("enter the name:")
                        ch3=input("enter the roll:")
                        ch4=input("enter the dpt:")
                        ch5=input("enter the year:")
                        print("to time:\n")
                        print("\t1)In seconds\n\t2)In minutes\n\t3)In Hours\n\t4)In Days")
                        c1=input("Enter:")
                        if c1=='1':
                          tt=int(input("enter seconds:"))
                        elif c1=='2':
                          t1=int(input("enter minutes:"))
                          tt=60*t1
                        elif c1=='3':
                          t1=int(input("enter hours:"))
                          tt=60*60*t1
                        elif c1=='4':
                          t1=int(input("enter days:"))
                          tt=60*60*24*t1
                        data={ch1:{"name":ch2,"roll":ch3,"dpt":ch4,"year":ch5,"Ctime":t,"toTime":tt}}
                        p.update(data)
                        write(p)
                   a=input("do you want to add more time to live key? y/n:")
        
               
  elif ch=='2':
        
         if path.exists('data.json'):
               a='y'
               while a=='y':
                   with open("data.json") as file:
                    p=json.load(file)
                    TTL(p)
                    ch1=input("enter the key:")
                    if ch1 in p:
                        print(p[ch1])
                       
                    else:
                        print("this key do'nt exst!!!!")
                   a=input("do you want to read more key? y/n:")
              
         else:
             print("Database is empty!!!!!!")
    
  elif ch=='3':
        if path.exists('data.json'):
               a='y'
               while a=='y':
                   with open("data.json") as file:
                    p=json.load(file)
                    TTL(p)
                    ch1=input("enter the key:")
                    if ch1 in p:
                        del p[ch1]
                        print("key is removed!!")
                       
                    else:
                        print("this key do'nt exst!!!!")
                    write(p)    
                   a=input("do you want to delete more key? y/n:")
        
        else:
            print("Database is empty!!!!!!")
        
  b=input("Do you want to continue?? y/n:")             
           
         
        
            
               
              
        

    

    
    