''' PIT Reader met MODBUS  & REST API'''
from PITreaderREST import *
from PITreaderMODBUS import *


def main():
    
    PIT2 = PITreaderREST()
    PIT2.SetUserToken("GerritAPIAdmin")
    #PIT2.Fetch('api/config/blocklist')
    PIT2.RequestEndPoint('api/config/permissionList')
    PIT2.ExecuteMethod()
    PIT2.ParseMethodResponse()
    return
    
    PIT1 = PITReaderMODBUS()
 
    PIT1.OverrideLedStatus(1,0,0)


    PIT1.ReadInputRegs()
    PIT1.PitReaderSerial()
    PIT1.PitReaderOrderNr()
    PIT1.AuthStatus()
    PIT1.Permission()
    PIT1.TransponderOrderNr()
    PIT1.GetTransponderSerial()


    PIT1.getLedFlashmode()
    PIT1.getLedColor()
    PIT1.GetTransponderDataLength()
    PIT1.GetTransponderUID()
    PIT1.GetStartDate()
    PIT1.GetEndDate()
    
#    PIT1.IsAuthenticated()

#    PIT1.OverwriteActivate(23,1)
    
    

#print(__name__)

if __name__ == '__main__' :
    main()
