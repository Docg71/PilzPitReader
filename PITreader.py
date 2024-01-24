
''' PIT Reader met MODBUS  & REST API'''

#import os,re
import modbus.client as mbc
#import struct as s
import datetime as dt
             
class PITReaderBase:


    AccessKey = { "Ordernr" : "402260" ,
                  "SerialNR" : "000503314" ,
                  "SecurityID" : "056C918936F749B8"
                }


    LedColors = ( ( 0 , "Off") , 
                  ( 1 , "blue") ,
                  ( 2 , "yellow") ,
                  ( 3 , "red") ,
                  ( 4 , "green") ,
                )
             
    LedMode = ( ( 0 , "cont" ),
                 ( 1 , "slow" )
               )

    def __init__(self):
        self.Reader = "123456789"
        self.KeySerial = ""
        self.IsAuth = False   
        
        self.IP = "192.168.178.21" 
        self.Port = 80
        
        
        

class PITreaderREST_API(PITReaderBase):
    ''' PIT Reader met REST API'''
    pass
    



    
    
    
class PITReader(PITReaderBase):
    ''' PIT Reader met MODBUS'''

    
    def __init__(self):
        super().__init__()
        self.Conn = mbc.client(host=self.IP)
        self.Port = 502

 #   def IsAuthenticated(self):
 #3       print("isauth")
 #       result = self._read(FC=2,ADR=4001, LEN = 1)
 #       print(result)
 #       self.IsAuth = True




#    def _write(self):
#        print("adkfjsdkfjkds0a")

    def _read(self, FC=4,ADR=0, LEN = 2):
        
        result = self.Conn.read(FC=FC,ADR=ADR, LEN = LEN)
        
        return result
        
    def ReadInputRegs(self):
        
        self.InputRegs = self._read(FC=4,ADR=0, LEN =58)
   #     print ( self.InputRegs )
 
 
    def GetReg(self , Reg = 1 , Len = 1 ):
        #print(f"Reg={Reg},Len={Len}:BeginElement={Reg - 1},EndElement={Reg - 1 + Len}-(not included)")
        
#        print( self.InputRegs[ Reg - 1  ] )
        
#        print( self.InputRegs[ Reg - 1 : Reg  + Len ] )
        
        result = self.InputRegs[ Reg - 1 : Reg - 1 + Len ]
        #print (result)
        return result
       
    def To32b(self, Regs):
        #print(len(Regs))
        return (Regs[0] << 16 ) + Regs[1]        
        
    def To16b(self,Regs):
        return Regs[0]
            
            
    def  PitReaderOrderNr(self):
        # 3x00001 & 3x00002
        result = self.To32b(self.GetReg( Reg = 1 , Len = 2) )
        print(f"PIT Reader OrderNr : {result}")
            
            
            
    def  PitReaderSerial(self):
        # 3x00003 & 3x00004
        result = self.To32b(self.GetReg( Reg = 3 , Len = 2) )
        print(f"PIT Reader Serial : {result}")
        

    def Permission(self):
        # 3x00033
        result = self.To16b(self.GetReg(33))
        print(f"PIT Permission : {result}")


    def AuthStatus(self):
        # 3x00034
        result = self.To16b(self.GetReg(34))
        print(f"PIT Auth status: {result}")

    
        
    def getColor(self):
        # 3x0009
        result = self.To16b(self.GetReg(9))
        print(f"PIT Get Color: {result}")
       

#    def setColor(self, color):
#        print("setcolor")
        
#        result = self.Conn.write(
#        print(result)
#        print(f"PIT Set Color: {result}")
       

    def getFlashmode(self):    
        # 3x0010
        result = self.To16b( self.GetReg(10))
        print(f"PIT Flash: {result}")
       
        
  # def setFlashmode(self, mode):
  #      print("setflash")

    def TransponderOrderNr(self):
        result = self.To32b( self.GetReg(Reg=35,Len=2)) 
       # print(result)
        print(f"TransponderOrderNr : {result}")

        
    def GetTransponderSerial(self):
        # 3x0037  and 38
        result = self.To32b( self.GetReg(Reg=37,Len=2)) 
       # print(result)
        print(f"TransponderSerial : {result}")

    def GetTransponderDataLength(self):
        # 3x0048
        result = self.To16b( self.GetReg(48))
        print(f"Transponder Data UID Length: {result}")
       
    def GetTransponderUID(self):
        result = self.GetReg(Reg=43,Len=5)
        print(f"TransponderUID : {result}")

    def OverwriteActivate(self , color, flash , active = 0):           
        result = self.Conn.write(color, flash , active , FC=16 , ADR=6000)
        print("Led Overwritten")
        
 
    def GetStartDate(self):
        result = self.To32b(self.GetReg(Reg=55,Len=2))
        print (f"StartDate secs since  01-01-2000 - 00:00: {result}")
        print (f"Real Start Date {self.dt_delta(result)}")


    def GetEndDate(self):
        result = self.To32b(self.GetReg(Reg=57,Len=2))
        print (f"EndDate secs since  01-01-2000 - 00:00: {result}")
        print (f"Real End Date {self.dt_delta(result)}")

 
    def dt_delta(self, secs):
        start = dt.datetime(2000,1,1)
        return start + dt.timedelta(seconds=secs)
        #print (end)
        
        
        
        


def main():
    
    PIT1 = PITReader()
 
    PIT1.OverwriteActivate(1,0,0)


    PIT1.ReadInputRegs()
    PIT1.PitReaderSerial()
    PIT1.PitReaderOrderNr()
    PIT1.AuthStatus()
    PIT1.Permission()
    PIT1.TransponderOrderNr()
    PIT1.GetTransponderSerial()
#    PIT1.GetKeySerial()

    PIT1.getFlashmode()
    PIT1.getColor()
    PIT1.GetTransponderDataLength()
    PIT1.GetTransponderUID()
    PIT1.GetStartDate()
    PIT1.GetEndDate()
    
#    PIT1.IsAuthenticated()

#    PIT1.OverwriteActivate(23,1)
    
    



if __name__ == '__main__' :
    main()
