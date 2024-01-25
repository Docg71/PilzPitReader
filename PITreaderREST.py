''' PIT Reader REST API'''

from PITreaderBASE import *
import pycurl       
import certifi
from io import BytesIO
import json
             
            
        
'''
============================================================================================
PIT Reader REST API
============================================================================================
'''
''' Make sure you have added users in the PIT Reader under User -> Device user '''        

API_Roles =  ( ( 10 , "Guest") , 
              ( 200 , "Transponder") ,
              ( 400 , "Device") ,
              ( 500 , "Administrator")
            )

'''These are fictious users in a test environment'''

API_Users = (   { "n" : "GerritAPI" , "l" : 10, "t" : "FdgQrWY7K1AmQjZL1+Kw7Q==" },
                { "n" : "GerritAPITransponder" , "l" : 200 , "t" : "mm/bRecaPGL/jgqzIpUH8Q==" } ,              
                { "n" : "GerritAPIDevice" , "l" : 400 , "t" : "RKJaGBSa96BqgJlLHTQ3Dg==" } ,
                { "n" : "GerritAPIAdmin" , "l" : 500 , "t" : "mJm6Xf2E+6/X6rKZjVBy0w==" }
            )




class PITreaderREST(PITreaderBase):
    ''' PIT Reader met REST API'''

    AuthUser  = { "n" : "" , "l" : 0 , "t" : "" }

    def __init__(self):
        super().__init__()
        self.Port = 443
        
    def GetUserToken(self, User):
        for x in API_Users:
            if x['n'] == User:
                #print (x)
                return x['t']
        return ''
        
         
    def SetUserToken(self, User):
        for x in API_Users:
            if x['n'] == User:
                self.AuthUser = x
                return True
        return False

    def Get(self,EndPoint):
        print (f"GET https://{self.IP}/{EndPoint}")
    
        return  f"https://{self.IP}/{EndPoint}"
    
    def Post(self,EndPoint):
        return  f"POST https://{self.IP}:443/{EndPoint}"
    
    def Fetch(self, cmd = 'api/status'):

        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.VERBOSE, True)
        
        #c.setopt(c.URL, 'https://duckduckgo.com/')
        c.setopt(c.URL, self.Get( cmd ))
        
        if self.AuthUser['t'] != '':
            print ("--Auth User Found : set Headers")
            header = [ f"Authorization: Bearer {self.AuthUser['t']}" ]  # Case sensitive  !
            c.setopt(c.HTTPHEADER, header)
        
        c.setopt(pycurl.SSL_VERIFYPEER, 0)   
        c.setopt(pycurl.SSL_VERIFYHOST, 0)

        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        c.perform()
        c.close()

        body = buffer.getvalue()
        # Body is a byte string.
        # We have to know the encoding in order to print it to a text file
        # such as standard output.
        print(body.decode('iso-8859-1'))    
    
    
    