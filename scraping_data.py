# -*- coding: utf-8 -*-
"""Scraping_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mPEOqMJEtSfO7yxXPx8CZLubAOTHRk-d
"""

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup, Tag, NavigableString
import requests
import re

from google.colab import drive
drive.mount('/content/drive')

r1 = requests.get("https://en.wikipedia.org/wiki/List_of_philosophers_(A%E2%80%93C)")
r2 = requests.get("https://en.wikipedia.org/wiki/List_of_philosophers_(D%E2%80%93H)")
r3 = requests.get("https://en.wikipedia.org/wiki/List_of_philosophers_(I%E2%80%93Q)")
r4 = requests.get("https://en.wikipedia.org/wiki/List_of_philosophers_(R%E2%80%93Z)")
data1 = r1.content # Content of response
data2 = r2.content # Content of response
data3 = r3.content # Content of response
data4 = r4.content # Content of response
soup1 = BeautifulSoup(data1, "html.parser")
soup2 = BeautifulSoup(data2, "html.parser")
soup3 = BeautifulSoup(data3, "html.parser")
soup4 = BeautifulSoup(data4, "html.parser")

def FromHTMLtoA(soup):
    tab = []
    a_loop = soup.find_all('li')
    for i in a_loop:
        a = i.find('a', href=True)
        if a : tab.append(a['href'])
    return tab

def CleaningA(tab):
    index_limit = tab.index('/wiki/The_Cambridge_Dictionary_of_Philosophy')
    tab = tab[5:index_limit]
    for i in range(0, len(tab)):
        tab[i]='https://en.wikipedia.org'+tab[i]
    return tab

a1 = CleaningA(FromHTMLtoA(soup1))
a2 = CleaningA(FromHTMLtoA(soup2))
a3 = CleaningA(FromHTMLtoA(soup3))
a4 = CleaningA(FromHTMLtoA(soup4))

l_word_selection = ['theory', 'political', 'philosophy', 'view', 'religious', 'philosophical', 'career as a scientist', 'philosopher', 'theorie', 'idea', 'belief', 'thought', 'religion','theology','ideology','formalism','analysis','buddhism', 'influence']

a_final = a1+a2+a3+a4

def SelectionPhilosophers(tab, word_selection):
    philosopher_section = []
    result = []
    for i in range(0, len(tab)):
        r = requests.get(tab[i])
        data = r.content
        soup = BeautifulSoup(data, "html.parser")
        title_tab = soup.select("li.toclevel-1 > a > span.toctext")
        cp = title_tab
        title_tab = [x.contents for x in title_tab]
        title_tab = [item for sublist in title_tab for item in sublist]
        tot=[]
        for j in range(0, len(word_selection)):
            inter_tab = []
            k=0
            match=False
            while (k<len(title_tab)):
                #print(title_tab[k], k)
                match = re.findall(word_selection[j], str(title_tab[k]).lower())
                if (match) :
                    add_sub_section = cp[k].parent.parent.select("span.toctext")
                    add_sub_section = [x.contents for x in add_sub_section]
                    add_sub_section = [item for sublist in add_sub_section for item in sublist]
                    for g in range(0, len(add_sub_section)):
                        if(isinstance(add_sub_section[g], Tag)):
                            add_sub_section[g] = add_sub_section[g].text
                    if(add_sub_section not in inter_tab):
                        inter_tab += add_sub_section
                k+=1
            if (k==len(title_tab) and inter_tab):
                tot+=inter_tab                
        
        if(j==len(word_selection)-1 and tot):
            philosopher_section.append([tab[i]]+tot)
        
    return philosopher_section

def RemoveDuplicate(tab):
    # [[link_philo, section, section...], [link_philo, section, section ...] ...]
    philosopher_section = []
    for i in range(0, len(tab)):
        clean_sub_tab = []
        for g in tab[i]:
            if (g not in clean_sub_tab):
                clean_sub_tab.append(g)
        philosopher_section.append(clean_sub_tab)

    return philosopher_section

my_selection = RemoveDuplicate(SelectionPhilosophers(a_final,l_word_selection))

print(my_selection)
print(np.array(my_selection).shape)

def GetDataH(tab):
    
    final_text_idea = [] # output [[[idea_title, text_idea],[idea_title, text_idea]],..., [idea_title, text_idea]]]
    for i in range(0, len(tab)):
        all_text_idea = []
        r = requests.get(tab[i][0])
        data = r.content
        soup = BeautifulSoup(data, "html.parser")
        for j in range(1, len(tab[i])):
            start = soup.find("span",class_='mw-headline',text=tab[i][j])
            res=0
            detect_i = 0
            if (start==None):
                start = soup.find_all("span",class_='mw-headline')
                for find_this_i in start:
                    start_temp = find_this_i.find('i',text=tab[i][j])
                    if(start_temp!=None):
                        start = start_temp
                        res=1
                        detect_i = 0
                        break
                    detect_i=1
            
            if(detect_i==1 and res==0 ):
                res=2

            if (start!=None and res==0):
                text_content = []
                for elem in start.parent.next_siblings: # parent (bcz : h > span)
                    if (elem.name == 'h1' or elem.name == 'h2' or elem.name == 'h3' or elem.name == 'h4' or elem.name == 'h5' or elem.name == 'h6' or elem.name == 'h7'):
                        break
                    if(elem.name == 'p' or elem.name == 'ol' or elem.name == 'ul' or elem.name == 'blockquote'):
                        text_content.append(elem.text)
                    if (elem.name != 'p' or elem.name != 'ol' or elem.name != 'ul' or elem.name != 'blockquote'):
                        continue
                
                text_content = [tab[i][j]]+text_content # [idea_title, text_idea]
                all_text_idea.append(text_content)

            if (start!=None and res==1):
                text_content = []
                for elem in start.parent.parent.next_siblings: # parent.parent (bcz : h > span > i)
                    if (elem.name == 'h1' or elem.name == 'h2' or elem.name == 'h3' or elem.name == 'h4' or elem.name == 'h5' or elem.name == 'h6' or elem.name == 'h7'):
                        break
                    if(elem.name == 'p' or elem.name == 'ol' or elem.name == 'ul' or elem.name == 'blockquote'):
                        text_content.append(elem.text)
                    if (elem.name != 'p' or elem.name != 'ol' or elem.name != 'ul' or elem.name != 'blockquote'):
                        continue
            
                text_content = [tab[i][j]]+text_content # [idea_title, text_idea]
                all_text_idea.append(text_content)

        final_text_idea.append(all_text_idea)
    
    return final_text_idea

idea_title = GetDataH(my_selection)

def ConcatTextIdea(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])):
            if(len(tab[i][j])>2):
                for v in range(2,len(tab[i][j])):
                    tab[i][j][1] = tab[i][j][1] + tab[i][j][v]
                tab[i][j] = tab[i][j][:2]
            if(len(tab[i][j])==1):
                tab[i][j] = None
    return tab

Result_before_clean = ConcatTextIdea(idea_title)

print(Result_before_clean) # [[[title, text],[title, text]], ... ,[[title, text],[title, text]]]
print(len(Result_before_clean))

# Create a pandas dataframe

def AddValue(tab1, tab2):
    df = pd.DataFrame(columns=['Philosopher', 'Title', 'Idea'])
    for i in range(0,len(tab1)):
        for j in range(0, len(tab1[i])):
            if(tab1[i][j]!=None):
                df = df.append({'Philosopher': tab2[i][0], 'Title': tab1[i][j][0], 'Idea': tab1[i][j][1]}, ignore_index=True)
    
    return df

df = AddValue(Result_before_clean, my_selection)

df.head()

df.to_csv('/content/drive/My Drive/machine_learning/philo.csv', index = False)