#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape(htmlbase,start):

    print('start:',start)

    try:

        with open('top250','a') as f:

            try:

                html    = htmlbase
                bsObj   = BeautifulSoup(urlopen(html).read(),'html.parser')
                namelist= bsObj.findAll("span",{"property":"v:average"})
                for name in namelist:

                    f.write(name.get_text()+': ')

                f.write('\n')

            except:

                pass

    except IOError :

        print('IOError')

    print('end')

def main():

    htmlbase    = "https://movie.douban.com/top250?start=25&filter="
    start       = 25
    length      = 25
    end         = 166
    scrape(htmlbase,start)

if __name__ == '__main__':

    main()
