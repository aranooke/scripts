from tkinter import *;
from tkinter import ttk;
import requests;
import re;
from bs4 import BeautifulSoup;
def get_info():
    url =  "https://mignews.com/";
    page = requests.get(url);
    soup = BeautifulSoup(page.text,"html.parser");
    allTime = soup.findAll("div",class_="text-color-dark");
    allNews = soup.findAll("div",class_="btn btn-secondary btn-xs rounded-0");
    textBlock,newsBlock = [],[];
    for itr in allTime:
        #print(itr.text);
        textBlock.append(itr.text);
    for itr in allNews:
        #print(itr.text);
        newsBlock.append(itr.text);
    #print(textBlock)
    return [textBlock,newsBlock];

def start_tale(url,block,clas):
    url =  url;
    page = requests.get(url);
    soup = BeautifulSoup(page.text,"html.parser");
    allTime = soup.findAll(block,class_=clas);
    result = [];
    print(allTime);
    for itr in allTime:
        result.append(itr);
        print(itr.text);
    return result;
def get_ukraine():
    start_tale("https://www.pravda.com.ua/rus/news/",
               "div","article_header");
    
get_ukraine();

def get_ukrnews(frm,row = 2):
    res = start_tale("https://www.pravda.com.ua/rus/news/",
               "div","article_header");
    for i in res:
        ttk.Label(frm,text=i).grid(column = row);
        row+=1;
    
def kinter():
   
    result = get_info();
    root = Tk();
    frm = ttk.Frame(root, padding=10);
    root.title("Our news to read");
    root.attributes("-topmost",1);
    frm.grid();
    row,column = 2,1;
    ttk.Label(frm,text="Последние новости с израильского сайта mig news").grid(column = 0,row = 0);
    for itr in result[0]:
        ttk.Label(frm,text=itr).grid(column = 0,row = row);
        row+=1;
    
    
    row = 1;
    for itr in result[1]:
        pass;
        #ttk.Label(frm,text=itr).grid(column = column,row = 0 );
        #column+=1;
    
    
    root.mainloop();

kinter();
