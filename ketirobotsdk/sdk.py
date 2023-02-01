
from operator import mod
import os
import ctypes
# from psutil import cpu_times_percent
TestDummy= 0
RB10    =1
UR10    =2
M1013   =3
Indy7   =4

Base=0
TCP=1
file_path= f'{os.getcwd()}/ketirobotsdk/librobotsdkv2.so'

module=ctypes.cdll.LoadLibrary(file_path)
connect_state=0



class RxDataInfo(ctypes.Structure):
    _fields_=[("Jnt",ctypes.c_double*7),
             ("Mat",ctypes.c_double*16),
             ("State",ctypes.c_double)]
    
class TCPoff(ctypes.Structure):
    _fields_=[('x',ctypes.c_double),
              ('y',ctypes.c_double),
              ('z',ctypes.c_double),
              ('rot1',ctypes.c_double),
              ('rot2',ctypes.c_double),
              ('rot3',ctypes.c_double)]      

class DIInput(ctypes.Structure):
    _fields_=[('DI',ctypes.c_bool*16)]      


def RobotInfo():
    module.RobotInfo.restype=RxDataInfo

    return module.RobotInfo()

# def SetTCP(args):
   
#     module.SetTCPCord(TCP(args[0],args[1],args[2],args[3],args[4],args[5]))

def movel(*args):
    module.movel.argtypes=[ctypes.c_double,ctypes.POINTER(ctypes.c_double)]
    if len(args[1])!=16: 
        print("input arguments must 16")
    
    arg_arr=[args[0],(ctypes.c_double*len(args[1]))(*args[1])]
    
   
    module.movel(*arg_arr)
    
    
def movej(args):
    module.movej.argtypes=[ctypes.POINTER(ctypes.c_double)]
    if len(args)!=6: 
        print("input arguments must 6")
    
    arg_arr=(ctypes.c_double*len(args))(*args)
    module.movej(arg_arr)
                 

def moveb(*args):
    err=0
    args_arr=[args[0],args[1],len(args)-3]
    module.moveb.argtypes=[ctypes.c_double,ctypes.c_double,ctypes.c_double]
    print(len(args))
    
    for i in range(3,len(args)):
        print(i,len(args[i]))
        if(len(args[i])==16) :
            args_arr.append((ctypes.c_double*len(args[i]))(*args[i]))
            module.moveb.argtypes.append(ctypes.POINTER(ctypes.c_double))
            
        else:
            err=i 
            break
        
    if err!=0 :
        print('CMD Input',err,'Length Not match')
    else : 
        module.moveb(*args_arr)
    
    
def SetRobotConf(*args):
    args_arr=[args[0],args[1].encode('utf-8'),args[2]]
    module.SetRobotConf.argtypes=[ctypes.c_int,ctypes.c_char_p,ctypes.c_int]
    module.SetRobotConf(*args_arr)
    
def RobotConnect():
    module.RobotConnect()
    
    
def RobotDisconnect():
    module.RobotDisconnect()
    
def SetVelocity(args):
    module.SetVelocity.argtypes=[ctypes.c_double]
    module.SetVelocity(args)
    
def Stop():
    module.Stop()
    

def ControlBoxDigitalOut(args):
    module.ControlBoxDigitalOut.argtypes=[ctypes.c_int]
    module.ControlBoxDigitalOut(args)
    
def ControlBoxDigitalIn():
    # module.ControlBoxDigitalIn.restype=DIInput
    module.ControlBoxDigitalIn.restype=ctypes.c_double
    return module.ControlBoxDigitalIn()
   