***

### Environment

#### Linux Version : Ubuntu 20.04
#### Python version : 3.8.10

***

### 1. Download Project
~~~
git clone https://github.com/robot-plus-program/ketirobotsdk.git
~~~

### 2. How to use
``` python
사용하려는 *.py 파일과 같은 경로에 패키지( ketirobotsdk 폴더) 설치
from ketirobotsdk.sd  import * 를 추가하여 제공되는 명령어를 사용
```

### 3. Example
``` python

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
```

### 4. Commands Discription

#### SetRobotConf(Rsys, IP, PORT)
```
사용할 로봇과 TCP 통신 IP, PORT 할당

Rsys : 로봇 종류 (RB10, INDY7, UR10, M1013)
IP : TCP IP Address
PORT : TCP Port
ex) 
SetRobotConf(UR10, '168.137.0.77', 30003)
```

#### RobotConnet()/RobotDisconnect()
```
TCP 통신에 연결/연결 해제
```

#### movej(q)
```
q : joint position
ex)  
q0 : 0°, q1 : 0°, q2 90°, q3 : -90°, q4 : 0°, q5 : 0° -> q = [0, 0, 1.5707, -1.5707, 0, 0]
movej(q)
```

#### movel(type, pose)
```
type : Reference Coordinate, (Base or TCP)
Pose : target position, (4by4 matrix)
ex) 
case RB10 -> x:300mm, y:200mm, z=250mm , rx :90°, ry:0°, rz:90° (RPY)
case M1013 -> x:300mm, y:200mm, z=250mm, A:0°, B:90°, C:90° (ZXZ)
pose1 = [0, 1, 0, 0.3, 0, 0, 1, 0.2, 1, 0, 0, 0.25, 0, 0, 0, 1]
movel(base,pose1)
```

#### moveb(type, r, nPnt, Pose1, Pose2, ... , Pose5)
```
type : Reference Coordinate , (Base or TCP)
r : Blend Radius [m]
nPnt : number of via point
Pose(n) : target position & rotation, (4by4 matrix)
ex)
pose1= [0, 1, 0 0.3, 0, 0, 1, 0.2, 1, 0, 0, 0.25, 0, 0, 0, 1]
pose2= [0, 1, 0 0.2, 0, 0, 1, 0.3, 1, 0, 0, 0.25, 0, 0, 0, 1]
pose3= [0, 1, 0 0.3, 0, 0, 1, 0.3, 1, 0, 0, 0.25, 0, 0, 0, 1]
moveb(base,0.05, 3, pose1, pose2, pose3)
```
#### Stop()
```
Robot stop immediately
```

#### [Jnt[6],Mat[16],State]=RobotInfo()
```
Jnt : joint position
Mat : Robot Position 4 by 4 matrix
State : Robot state(2:Moving , 1: Idel, 0: else)

ex) 

#### 4by4 Matrix 
 Data=RobotInfo()

print(Data.Mat[0],Data.Mat[1],Data.Mat[2],Data.Mat[3])
print(Data.Mat[4],Data.Mat[5],Data.Mat[6],Data.Mat[7])
print(Data.Mat[8],Data.Mat[9],Data.Mat[10],Data.Mat[11])
print(Data.Mat[12],Data.Mat[13],Data.Mat[14],Data.Mat[15])


```

#### SetTCP(TCPOffset)
```
TCPOffset : TCP offset position & rotation (4by4 matrix)
ex)
TCPOffset = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0.01, 0, 0, 0, 1]
```

#### SetVelocity(v)
```
Setting Robot Velocity  0 ~ 100 %

v: Robot Velocity(%) default 50%

```
