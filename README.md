***
### Robot & Command Develop DB
https://stingy-lemming-c04.notion.site/SDK-DB-865ae97a0938402582f9138f96384663

### Environment

#### UpdataDatae : 
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
from ketirobotsdk.sdk  import * 를 추가하고 setLibPath('ketirobotsdk/librobotsdk.so')로 라이브러리 경로를 지정
Robot 클래스 객체를 만들어 제공되는 명령어를 사용 (rob=Robot(); rob.SetRobotConf(...))
모듈 함수(SetRobotConf(), RobotConnect() 등)는 현재 librobotsdk.so와 호환되지 않으므로 Robot 클래스를 사용
```

### 3. Example
``` python
from ketirobotsdk.sdk import *
from time import *
import threading

# 예제의 joint/pose 값은 참고용입니다. 실행 전 사용하는 로봇의 작업 공간에 맞게 다시 티칭하세요.
Pose1=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.178,0,0,0,1]
Pose2=[-1,0,0,0.735,0,1,0,-0.172,0,0,-1,0.328,0,0,0,1]

setLibPath('ketirobotsdk/librobotsdk.so')
rob=Robot()

#### Thread example
#### Get Robot Information 
def thread():
    while(1):
        Data=rob.RobotInfo()
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
   
    # 사용하는 로봇에 맞게 설정 (2026 challenge: rob.SetRobotConf(RB10,'192.168.137.50',5000))
    rob.SetRobotConf(UR10,'192.168.0.77',30003)
    rob.RobotConnect()

    ##start Thread ##
    sub.daemon=True
    sub.start()
    #################
    
    
    rob.SetVelocity(80)
    rob.movej([0,-1.57,-1.57,-1.57,1.57,0])
    sleep(5)

    rob.SetVelocity(50)
    rob.movel(Base,Pose2)
    sleep(2)
   

    rob.SetVelocity(20)
    rob.movel(Base,Pose1)
    sleep(5)

    rob.RobotDisconnect()
   
```

### 4. Commands Description

#### SetRobotConf(Rsys, IP, PORT)
```
사용할 로봇과 TCP 통신 IP, PORT 할당

Rsys : 로봇 종류 (RB10, Indy7, UR10, M1013)
IP : TCP IP Address
PORT : TCP Port (RB10: 5000, M1013: 12345, UR10: 30003)
ex) 
SetRobotConf(RB10, '192.168.137.50', 5000)
SetRobotConf(UR10, '192.168.0.77', 30003)
```

#### RobotConnect()/RobotDisconnect()
```
TCP 통신에 연결/연결 해제
```
#### [Jnt[6],Mat[16],State]=RobotInfo()
``` python
Jnt : joint position
Mat : Robot Position 4 by 4 matrix
State : Robot state(2:Moving , 1: Idle, 0: else)

ex) 

#### 4by4 Matrix 
Data=RobotInfo()

print("Matrix")
print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[0],Data.Mat[1],Data.Mat[2],Data.Mat[3]))
print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[4],Data.Mat[5],Data.Mat[6],Data.Mat[7]))
print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[8],Data.Mat[9],Data.Mat[10],Data.Mat[11]))
print("%.3f\t%.3f\t%.3f\t%.3f"%(Data.Mat[12],Data.Mat[13],Data.Mat[14],Data.Mat[15]))
        

print("Joint")
print("%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f"%(Data.Jnt[0],Data.Jnt[1],Data.Jnt[2],Data.Jnt[3],Data.Jnt[4],Data.Jnt[5]))

print("State")
print("%.3f"%(Data.State))

```

#### SetTCP(TCPOffset) - 현재 sdk.py 미지원
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
movel(Base, pose1)
```

#### moveb(type, r, nPnt, Pose1, Pose2, ... , Pose5)
```
type : Reference Coordinate , (Base or TCP)
r : Blend Radius [m]
nPnt : number of via point
Pose(n) : target position & rotation, (4by4 matrix)
ex)
pose1= [0, 1, 0, 0.3, 0, 0, 1, 0.2, 1, 0, 0, 0.25, 0, 0, 0, 1]
pose2= [0, 1, 0, 0.2, 0, 0, 1, 0.3, 1, 0, 0, 0.25, 0, 0, 0, 1]
pose3= [0, 1, 0, 0.3, 0, 0, 1, 0.3, 1, 0, 0, 0.25, 0, 0, 0, 1]
moveb(Base, 0.05, 3, pose1, pose2, pose3)
```

#### movec(type, Pose1, Pose2)
```
type : Reference Coordinate , (Base or TCP)
Pose(n) : target position & rotation, (4by4 matrix)
ex)
pose1= [0, 1, 0, 0.3, 0, 0, 1, 0.2, 1, 0, 0, 0.25, 0, 0, 0, 1]
pose2= [0, 1, 0, 0.2, 0, 0, 1, 0.3, 1, 0, 0, 0.25, 0, 0, 0, 1]
movec(Base, pose1, pose2)
```

#### Stop()
```
Robot stop immediately
```

#### ControlBoxDigitalOut(PortNum)
```
PortNum : The Number of output with Bit Control. 0 is False,1 is True

ex) OutputPort 0,2 Set True
ControlBoxDigitalOut(5)

```
#### PortNum=ControlBoxDigitalIn()
```
PortNum : The Number of Input with Bit Control.

ex) If Input Port is 14, InputPort 1,2,3 is True
 Input=ControlBoxDigitalIn()
```

### 힘 제어(Force control) & 순응 제어(Compliance Control)
```
힘 제어 및 순응 제어는 M1013에서만 지원됨
RB10 등 다른 로봇에서는 호출해도 아무 동작을 하지 않으며 RobotGetToolForce()는 0을 반환함

힘 제어를 사용하는 경우 순응 제어와 함께 사용해야 함
RobotComplianceCtrlOn() -> RobotSetToolForce(fd, dir)
 -> move linear command -> RobotReleaseForce() -> RobotComplianceCtrlOff()

힘제어를 사용하지 않고 순응제어만 사용 할 경우
RobotComplianceCtrlOn() -> move linear command -> RobotComplianceCtrlOff

힘 제어 및 순응 제어는 반드시 cartesian space 내 움직임에 대해서만 적용해야 함.
joint space 에서는 작동하지 않고 오류가 발생함

ex)
RobotComplianceCtrlOn()

fd = [0, 0, -50, 0, 0, 10] # 힘 제어에 사용할 기준 힘 값 [px, py, pz, mx, my, mz]
dir = [0, 0, 1, 0, 0, 1] # 힘 제어 적용 할 축 방향, 양의 방향만 가능
RobotSetToolForce(fd, dir)

movel(0, pose)

RobotReleaseForce()
RobotComplianceCtrlOff()
```


