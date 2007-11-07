#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Sets the encoding to utf-8 to avoid problems with æøå

import random
import os,re
from urlextracter import *
from sgmllib import *

class Crawler:
    current = ""
    urls = []
    crawled = []
    
    def crawl(self,url):
        self.current = url
        print "Crawling " + url
        try:
            ue = URLextracter(url)
        except SGMLParseError:
            print "This URL contains error that can't be handled by this app.\nSorry!"
            print "=" * 30
            print "Trying new random URL"
            self.crawl(self.urls[random.randint(1,len(self.urls))])
            return
        
        urlparts = url.replace("http://", "").replace("/",".").split(".")
        filename = ""
        for part in urlparts:
            if not str(part).__contains__("www"):
                filename += part + "."
        filename += "txt"
        
        print "Stored as: " + filename
        urls = ""
        try:
            f = open("/home/thomas/mined2/no/%s" % filename, 'wb')
            content = str(ue.output())         
            #content = re.sub(r"\W+", " ", content)
            #content = re.sub(r"[0-9]", " ", content)
            content = re.sub(r"[^a-zA-ZæøåÆØÅ]", " ", content)
            content = content.strip()
#            for c in self.special_chars:    # Remove special characters
#                content.replace(str(c), " ")
#                print content
#                raw_input("enter")
            
#            lines = content.replace("\t", " ").replace("\r"," ").splitlines()
#            content = []
#            for line in lines:
#                temp = line.strip()
#                if temp == "" or temp == " ":
#                    lines.remove(line)
#                else:
#                    if len(line.strip().split(" ")) > 5:        # Minimum 5 words
#                        content.append(line.strip() + "\n")
            if len(content) > 5:
                try:
                    textToWrite = unicode("".join(content))
                except UnicodeDecodeError:
                    textToWrite = str("".join(content))
                f.write(textToWrite)
                f.close()
            else:
                os.remove("/home/thomas/mined2/no/%s" % filename)
            urls = ue.linklist
            print "" + url + " mined!"
        except IOError:
            print "Mined, but failed to store as file.\nSkipping this, going on to next!"
            urls = self.urls
        ok_urls = []
        for i in urls:
            url = i
            if str(url).__contains__("javascript"):
                urls.remove(url)
            elif str(url).__contains__("http://"):
                ok_urls.append(url)
            elif str(url).__contains__("https://"):
                ok_urls.append(url)
            else:
                urls.remove(url)
        if len(ok_urls) < 2:
            ok_urls = self.crawled
            unique = True            # Fake true
            print str(len(ok_urls))
        else:
            unique = False
        
        next = random.randint(1,len(ok_urls)-1)
        print next
        new_url = ok_urls[next]
        while not unique:
            next = random.randint(1,len(ok_urls)-1)
            new_url = ok_urls[next]
            if not new_url in self.crawled:
                unique = True
            elif len(ok_urls) < 2:                    # with this few left we fake it
                ok_urls = self.crawled
                next = random.randint(1,len(ok_urls)-1)
                new_url = ok_urls[next]
                unique = True
            else:
                print "Already crawled " + new_url
                ok_urls.remove(new_url)
                if len(ok_urls) < 2:
                    ok_urls = self.crawled
                    next = random.randint(1,len(ok_urls)-1)
                    new_url = ok_urls[next]
                    unique = True
                
        self.urls = ok_urls
        self.crawled.append(self.current)
        self.crawl(new_url)



if __name__=="__main__":
    url = "http://www.vg.no"
    c = Crawler()
    c.crawl(url)