#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading

class MyThread(threading.Thread):

    def __init__(self,func,args,name = ''):

        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):

        self.func(*self.args)

def scrape(htmlbase,start,length):

    print('start:',start)

    try:

        with open('test'+str(start),'a') as f:

            for i in range(start,start+length):

                try:

                    html    = htmlbase + str(i) + '/?from=showing'
                    bsObj   = BeautifulSoup(urlopen(html).read(),'html.parser')
                    namelist= bsObj.findAll("span",{"property":"v:itemreviewed"})
                    taglist = bsObj.findAll("span",{"property":"v:genre"})
                    print('writein')

                    for name in namelist:

                        f.write(name.get_text()+': ')

                    for tag in taglist:

                        f.write(tag.get_text()+'/')

                    f.write('\n')

                except:

                    pass

    except IOError :

        print('IOError')

    print('end:',start+300)

def main():

    print('start....')

    threads     = []
    htmlbase    = "https://movie.douban.com/subject/"
    start       = 26672098
    length      = 300
    end         = start + length*4

    for i in range(start,end,length):

        t   = MyThread(scrape,(htmlbase,i,length),scrape.__name__)
        threads.append(t)

    for i in range(len(threads)):

        threads[i].start()

    for i in range(len(threads)):

        threads[i].join()


    print('all done....')

if __name__ == '__main__':

    main()
