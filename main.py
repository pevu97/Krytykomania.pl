from urllib.request import urlopen
import html
import json
import re


def convert(lst):
    return ' '.join(lst)

def finding_url(verse):
    string2 = 'class="sc-fTFjTM iSPZmI"><a href="'
    string3 = '" class="sc-cmaqmh '
    while (True):
        if string2 in verse:
            verse = verse.replace(string2,'')
    
        if string3 in verse:
            verse = verse.replace(string3,'')
        else:
            break
        
    return verse

def finding_verse(file):
    for line in file:
        verse = line.rstrip()
        if ('<div class="filmRating__rate"><span class="filmRating__rateValue">' in verse):
            return verse
        else:
            continue
    return 'nothing'

def finding_a_rating(verse):
    sub1 = '<div class="filmRating__rate"><span class="filmRating__rateValue">'
    sub2 = '</span>'
    
    # getting index of substrings
    if (sub1 in verse):
        idx1 = verse.index(sub1)
        idx2 = verse.index(sub2)
 
        res = ''
    # getting elements in between
        res = ''.join(verse.split(sub1)[1].split(sub2)[0])
 
    # printing result
        if (',' in res):
            res = res.replace(',', '.')
            return float(res)
        
        else:
            return float(0)
    else:
        return float(0)
    

def title(line):
    if ('ript><meta property="og:title" content="' in line): 
        sub1 = 'ript><meta property="og:title" content="'
        sub2 = '| Film'
 
        # getting index of substrings
        idx1 = line.index(sub1)
        idx2 = line.index(sub2)
 
        res = ''
        # getting elements in between
        res = ''.join(line.split(sub1)[1].split(sub2)[0])
 
        # printing result
        return res
    else:
       return 1

list = []
x = 0
film = {}
counting = 0

# Operation on main file

with open("movies_website.html", 'r', encoding='utf-8') as f:
    lines = f.read()
    test = convert(lines)
    list = re.findall('http[s]?://www.filmweb.pl/film/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', lines)



            
print("There are", len(list), "movies")

# Operation on movie file
for pages in list:
    page = urlopen(pages).read().decode('ISO-8859-1')
    if (title(page) != 1):
        film.update({title(page): 0})
    else:
        pass
    
    with open('movie_file.txt', 'w', encoding='UTF-8') as file:
        file.write(page)
            
        
    with open('movie_file.txt', 'r', encoding='UTF-8') as file:
        verse = finding_verse(file)
        film.update({title(page):finding_a_rating(verse)})
        counting += 1
        print("Adding..", counting)
        
            
        
 
    
with open('movie_file.txt', 'a', encoding='UTF-8') as file:
    file.write(json.dumps((film)))
    print('End')
    exit()

    
    
