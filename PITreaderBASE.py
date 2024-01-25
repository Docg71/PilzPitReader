''' PIT Reader base'''

             

AccessKey = { "Ordernr" : "402260" ,
              "SerialNR" : "000503314" ,
              "SecurityID" : "056C918936F749B8"
            }


LedColors = ( ( 0 , "Off") , 
              ( 1 , "blue") ,
              ( 2 , "yellow") ,
              ( 3 , "red") ,
              ( 4 , "green")
            )
         
LedMode = ( ( 0 , "cont" ),
             ( 1 , "slow" )
           )
         
         



class PITreaderBase:


    def __init__(self, IP = "192.168.178.21"):   # fill  in your own pit reader ip address
#        self.Reader = "123456789"
#        self.KeySerial = ""
#        self.IsAuth = False   
        
        self.IP = IP 
#        self.Port = 80
        
        