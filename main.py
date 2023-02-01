from ketirobotsdk.sdk import *
from time import *
import threading

Pose1=[-0.707,0,0,0.85,0,0.707,0,0.245,0,0,-1,0.7,0,0,0,1]
Pose2=[1,0,0,-0.56,0,0,1,0.15,0,-1,0,0.60,0,0,0,1]

jnt1=[1,2,3,4,5,6]
#### Thread example
#### Get Robot Information 
def thread():
    while(1):
        Data=RobotInfo()
        print("Mat")
        print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[0],Data.Mat[1],Data.Mat[2],Data.Mat[3]))
        print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[4],Data.Mat[5],Data.Mat[6],Data.Mat[7]))
        print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[8],Data.Mat[9],Data.Mat[10],Data.Mat[11]))
        print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[12],Data.Mat[13],Data.Mat[14],Data.Mat[15]))
        
        sleep(0.1)
    
sub=threading.Thread(target=thread)
#### Thread Example end


### Example used sdk###
if __name__=='__main__':
   
     ##start Thread ##
    #sub.daemon=True
    #sub.start()
    #################
    
    SetRobotConf(RB10,'192.168.47.7',1024)
    RobotConnect()
    while(1):    
    #   SetVelocity(50)
      # movel(0,Pose1)
      ControlBoxDigitalOut(65535)
      input=ControlBoxDigitalIn()
      print("%.3f"%(input))
      sleep(2)
      movel(0,Pose1)
      sleep(2)
      movej(jnt1)
      sleep(2)
    # SetVelocity(50)
    # movel(Base,Pose2)
    # sleep(2)
   

    # SetVelocity(20)
    # movel(Base,Pose1)
    # sleep(5)

    # RobotDisconnect()
   