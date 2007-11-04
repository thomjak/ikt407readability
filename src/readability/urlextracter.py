import urllib
import htmlentitydefs
from sgmllib import *

class URLextracter(SGMLParser):
    
    style = False
    script = False
    hyperlink = False
    
    linklist = []
    
    def __init__(self, url='http://python.org'):
        self.reset()
        try:
            self.sock = urllib.urlopen(url)
            self.feed(self.sock.read())
            self.sock.close()
            self.close()
        except IOError:
            raise SGMLParseError
        
    def start_style(self,attr):
        self.style = True
    
    def end_style(self):
        self.style = False
        
    def start_script(self,attr):
        self.script = True
    
    def do_script(self,attr):
        pass
    
    def end_script(self):
        self.script = False
        
    def start_a(self,attr):
        self.hyperlink = True
        href = [v for k, v in attr if k=='href']
        if href:
            self.linklist.extend(href)
    
    def end_a(self):
        self.hyperlink = False
   
    def reset(self):
        self.pieces = []
        SGMLParser.reset(self)
        
    def handle_data(self, text):
        tags_to_skip = [self.style, self.script, self.hyperlink]
        if True in tags_to_skip:
            pass
        else:
            self.pieces.append(text)
    
    def handle_declaration(self,decl):
        pass
    
    def report_unbalanced(self,tag):
        pass
    
    def unknown_starttag(self, tag, attrs):
        pass

    def unknown_endtag(self, tag):         
        pass
    
    def unknown_charref(self,tag):
        pass

        
    def output(self):
        return "" . join(self.pieces)
        
if __name__=="__main__":
    url = "http://www.db.no"
    try:
        ue = URLextracter(url)
    except SGMLParseError:
        print "This URL contains error that can't be handled by this app.\nSorry!"
        import sys
        sys.exit()
    
    urlparts = url.replace("http://", "").replace("/",".").split(".")
    filename = ""
    for part in urlparts:
        if not str(part).__contains__("www"):
            filename += part + "."
    filename += "txt"
    print filename
    
    f = open("/home/thomas/mined/%s" % filename, 'wb')
    content = str(ue.output())
    lines = content.replace("\t", " ").replace("\r"," ").splitlines()
    content = []
    for line in lines:
        temp = line.strip()
        if temp == "" or temp == " ":
            lines.remove(line)
        else:
            if len(line.strip().split(" ")) > 2:
                content.append(line.strip() + "\n")
    print content
    f.write("".join(content))
    f.close()
    print "" + url + " mined!"
    urls = ue.linklist
    print urls
#===============================================================================
#    for i in urls:
#        url = i
#        if not str(url).__contains__("javascript"):
#            ue = URLextracter(url)
#            print "" + url + " mined!"
#            urlparts = url.replace("http://", "").replace("/",".").split(".")
#            filename = ""
#            for part in urlparts:
#                if not str(part).__contains__("www"):
#                    filename += part + "."
#            filename += "txt"
#            print filename
#            
#            f = open("/home/thomas/mined/%s" % filename, 'wb')
#            content = str(ue.output())
#            f.write(content.strip("\n\t"))
#            f.close()
#            print "" + url + " mined!"
#            urls = ue.linklist
#===============================================================================