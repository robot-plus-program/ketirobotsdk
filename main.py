from cmath import pi
from ketirobotsdk.sdk import *
from time import *
import threading

# Pose1=[0,0,-1,-0.500,-1,0,0,0.158,0,1,0,0.334,0,0,0,1]
# Pose2=[0,0,-1,-0.500,-1,0,0,0.316,0,1,0,0.492,0,0,0,1]
# Pose3=[0,0,-1,-0.500,-1,0,0,0.158,0,1,0,0.630,0,0,0,1]
# Pose4=[0,0,-1,-0.500,-1,0,0,0.000,0,1,0,0.492,0,0,0,1]
# Pose5=[0,0,-1,-0.500,-1,0,0,0.158,0,1,0,0.334,0,0,0,1]
# Jnt1=[-pi,-24*pi/180,pi/2+24*pi/180,0,pi/2,0]

Pose1=[-1,0,0,-0.394,0,0,1,-0.688,0,1,0,0.510546,0,0,0,1]
Pose2=[-1,0,0,-0.394,0,0,1,-0.688,0,1,0,0.330724,0,0,0,1]
Pose3=[0,1,0,-0.691,1,0,0,-0.176,0,0,-1,0.745,0,0,0,1]
Pose4=[0,1,0,-0.691,1,0,0,-0.352,0,0,-1,0.579,0,0,0,1]
Pose5=[0,1,0,-0.691,1,0,0,-0.176,0,0,-1,0.403,0,0,0,1]
Jnt1=[0,-90*pi/180,90*pi/180,-90*pi/180,-90*pi/180,0]
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
    
    # SetRobotConf(RB10,'192.168.47.7',5000)
    # RobotConnect()
  
  
    SetRobotConf(RB10,'192.168.0.7',5000)
    RobotConnect()
    SetVelocity(80)

    # while(True):
    #     sleep(1)
    # print("MoveJ")
    # movej(Jnt1)
    # sleep(5)
    
    # SetVelocity(30)
    
    # print("MoveL")
    # movel(Base,Pose1)
    # sleep(5)
    
    print("MoveB")
    moveb(Base,0.05,2,Pose1,Pose2)
    sleep(10)
    
    # print("MoveC")
    # movec(Base,Pose4,Pose5)
    # sleep(10)

    RobotDisconnect()
   