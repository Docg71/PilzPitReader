'''
============================================================================================
PIT Reader MODBUS
============================================================================================
'''
    
import modbus.client as mbc
#import struct as s
import datetime as dt
    
    
class PITReaderMODBUS(PITReaderBase):
    ''' PIT Reader with MODBUS'''

    
    def __init__(self):
        super().__init__()
        self.Conn = mbc.client(host=self.IP)
        self.Port = 502


    def _read(self, FC=4,ADR=0, LEN = 2):
       
        return self.Conn.read(FC=FC,ADR=ADR, LEN = LEN)
        
        
    def ReadInputRegs(self):
        
        self.InputRegs = self._read(FC=4,ADR=0, LEN =58)
   #     print ( self.InputRegs )
 
 
    def GetReg(self , Reg = 1 , Len = 1 ):
        #print(f"Reg={Reg},Len={Len}:BeginElement={Reg - 1},EndElement={Reg - 1 + Len}-(not included)")
                
        return self.InputRegs[ Reg - 1 : Reg - 1 + Len ]
        
       
    def To32b(self, Regs):
        #print(len(Regs))
        return (Regs[0] << 16 ) + Regs[1]        
        
    def To16b(self,Regs):
        return Regs[0]
            
            
    def  PitReaderOrderNr(self):
        # 3x00001 & 3x00002
        result = self.To32b(self.GetReg( Reg = 1 , Len = 2) )
        print(f"PIT Reader OrderNr : {result}")
        return result    
            
            
    def  PitReaderSerial(self):
        # 3x00003 & 3x00004
        result = self.To32b(self.GetReg( Reg = 3 , Len = 2) )
        print(f"PIT Reader Serial : {result}")
        return result

    def Permission(self):
        # 3x00033
        result = self.To16b(self.GetReg(33))
        print(f"PIT Permission : {result}")
        return result

    def AuthStatus(self):
        # 3x00034
        result = self.To16b(self.GetReg(34))
        print(f"PIT Auth status: {result}")
        return result
    
        
    def getLedColor(self):
        # 3x0009
        result = self.To16b(self.GetReg(9))
        print(f"PIT Get Color: {result}")
        return result

       

    def getLedFlashmode(self):    
        # 3x0010
        result = self.To16b( self.GetReg(10))
        print(f"PIT Flash: {result}")
        return result
        

    def TransponderOrderNr(self):
        result = self.To32b( self.GetReg(Reg=35,Len=2)) 
        print(f"TransponderOrderNr : {result}")
        return result
        
    def GetTransponderSerial(self):
        # 3x0037  and 38
        result = self.To32b( self.GetReg(Reg=37,Len=2)) 
        print(f"TransponderSerial : {result}")
        return result

    def GetTransponderDataLength(self):
        # 3x0048
        result = self.To16b( self.GetReg(48))
        print(f"Transponder Data UID Length: {result}")
        return result
       
    def GetTransponderUID(self):
        result = self.GetReg(Reg=43,Len=5)
        print(f"TransponderUID : {result}")
        return result
    
    
    
    def OverrideLedStatus(self , color, flash , active = 0):           
        self.Conn.write(color, flash , active , FC=16 , ADR=6000)
        print("Led Overwritten")
        
 
    def GetStartDate(self):
        result = self.To32b(self.GetReg(Reg=55,Len=2))
        print (f"StartDate secs since  01-01-2000 - 00:00: {result}")
        print (f"Real Start Date {self.dt_delta(result)}")
        return result

    def GetEndDate(self):
        result = self.To32b(self.GetReg(Reg=57,Len=2))
        print (f"EndDate secs since  01-01-2000 - 00:00: {result}")
        print (f"Real End Date {self.dt_delta(result)}")
        return result
 
    def dt_delta(self, secs):
        start = dt.datetime(2000,1,1)
        return start + dt.timedelta(seconds=secs)
        
        
        
        
