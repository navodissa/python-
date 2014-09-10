import urllib2
import urllib
import httplib
import sys
from xml.etree import ElementTree as etree
import smtplib


class wolfram(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent': None}

    
    def _get_xml(self, ip):
        url_params = {'input': ip, 'appid': self.appid}
        data = urllib.urlencode(url_params)
        req = urllib2.Request(self.base_url, data, self.headers)
        xml = urllib2.urlopen(req).read()
        return xml

    
    def _xmlparser(self, xml):
        data_dics = {}
        tree = etree.fromstring(xml)
        # retrieving every tag with label 'plaintext'
        for e in tree.findall('pod'):
            for item in [ef for ef in list(e) if ef.tag == 'subpod']:
                for it in [i for i in list(item) if i.tag == 'plaintext']:
                    if it.tag == 'plaintext':
                        data_dics[e.get('title')] = it.text
        return data_dics

    
    def search(self, ip):
        xml = self._get_xml(ip)
        result_dics = self._xmlparser(xml)

        #print 'Available Titles' , '\n'
        titles = result_dics.keys()
        #for ele in titles :
        Res = result_dics['Result']
        Res_Split = Res.split('.')
        arg_1 = Res_Split[0]
        revenue = arg_1[1:]
        try:
            if int(revenue) >= 300:
                self.send_mails()
            else:
                print "Google has not reached it's revenue to $300b yet."
        except:
            print "Erorr in output."

   
    def send_mails(self):
        gmail_user = "navomails@gmail.com"
        gmail_pwd = "zacdxs@123"
        FROM = 'navomails@gmail.com'
        TO = ['navomails@gmail.com, navodissa@yahoo.com'] #must be a list
        SUBJECT = "Google has reached it's revenue to $300b"
        TEXT = "Hi,\n\nThis is to inform you that Google has reached it's revenue to $300b.\n \nRegards,\nAutomatic Mail Sender."

         # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            #server = smtplib.SMTP(SERVER) 
            server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
                #server.quit()
            server.close()
            print 'Google has reached their revenue to $300b.\nSuccessfully sent the mail'
        except:
            print "failed to send mail"


if __name__ == "__main__":
    schedule = "0 0 * * *"
    appid = 'T8WRWQ-7X2GVQ6Y3V'
    query = sys.argv[1]
    w = wolfram(appid)
    w.search(query)
    

# http://community.wolfram.com/groups/-/m/t/228183
