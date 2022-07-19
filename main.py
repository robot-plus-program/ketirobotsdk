
from ketirobotsdk.sdk import *
from time import *

Pose1=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.178,0,0,0,1]
Pose2=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.328,0,0,0,1]


if __name__=='__main__':
    ###MoveJ Example used sdk###
    SetRobotConf(UR10,'192.168.0.77',30003)
    RobotConnect()
    SetVelocity(80)
    movej([0,-1.57,-1.57,-1.57,1.57,0])
    sleep(5)

    SetVelocity(50)
    movel(Base,Pose2)
    sleep(2)
    a=RobotInfo()
    print("Mat")
    print(a.Mat[0],"\t",a.Mat[1],"\t",a.Mat[2],"\t",a.Pos[0])
    print(a.Mat[3],"\t",a.Mat[4],"\t",a.Mat[5],"\t",a.Pos[1])
    print(a.Mat[6],"\t",a.Mat[7],"\t",a.Mat[8],"\t",a.Pos[2])
    print(0,"\t",0,"\t",0,"\t",1)

    SetVelocity(20)
    movel(Base,Pose1)
    sleep(5)
    a=RobotInfo()
    print("Mat")
    print(a.Mat[0],"\t",a.Mat[1],"\t",a.Mat[2],"\t",a.Pos[0])
    print(a.Mat[3],"\t",a.Mat[4],"\t",a.Mat[5],"\t",a.Pos[1])
    print(a.Mat[6],"\t",a.Mat[7],"\t",a.Mat[8],"\t",a.Pos[2])
    print(0,"\t",0,"\t",0,"\t",1)
        
    RobotDisconnect()