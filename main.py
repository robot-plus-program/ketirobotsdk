from ketirobotsdk.sdk import *
from time import *
import threading

Pose1=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.178,0,0,0,1]
Pose2=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.328,0,0,0,1]

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
    sub.daemon=True
    sub.start()
    #################
    
    
    SetRobotConf(UR10,'192.168.0.77',30003)
    RobotConnect()
    SetVelocity(80)
    movej([0,-1.57,-1.57,-1.57,1.57,0])
    sleep(5)

    SetVelocity(50)
    movel(Base,Pose2)
    sleep(2)
   

    SetVelocity(20)
    movel(Base,Pose1)
    sleep(5)

    RobotDisconnect()
   