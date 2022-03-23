def sem1():
    sem1=[]
    a=b=c=0
    print("\nCommunicative English\nEngineering Mathematics - 1\nEngineering Graphics\nEngineering physics\nEngineering Chemistry\nPython\nPython Laboratory\nPhysics and Chemistry Laboratory")
    for i in range(0,3):
        x=int(input())
        if(x>5):
            sem1.append(x*4)
            a+=1
    for i in range(3,6):
        y=int(input())
        if(y>5):
            sem1.append(y*3)
            b+=1
    for k in range(6,8):
        z=int(input())
        if(z>5):
            sem1.append(z*2)
            c+=1
    print("Semester 1 - GPA : ",sum(sem1)/((a*4)+(b*3)+(c*2)))

def sem2():
    sem2=[]
    a=b=c=0
    print("\nTechnical English\nEngineering Mathematics - 2\nCircuit Analysis\nPhysics for Electronics Engineering\nBasic Electrical and Instrumentation Engineering\nElectronic Devices\nCircuits and Devices Laboratory\nEngineering Practicles Laboratory")
    for i in range(0,3):
        x=int(input())
        if(x>5):
            sem2.append(x*4)
            a+=1
    for i in range(3,6):
        y=int(input())
        if(y>5):
            sem2.append(y*3)
            b+=1
    for k in range(6,8):
        z=int(input())
        if(z>5):
            sem2.append(z*2)
            c+=1
    print("Semester 2 - GPA : ",sum(sem2)/((a*4)+(b*3)+(c*2)))

def sem3():
    sem3=[]
    a=b=c=d=0
    print("\nLinear Algebra and Partial Differential Equations\nSignals and Systems\nFundamentals of Data Structure in C\nElectronic Circuit - 1\nDigital Electronics\nControl Systems Engineering\nFundamentals of Data Structures in C Laboratory\nAnalog and Digital Circuits Laboratory\nInterpersonal Skills/Listening & Speaking")
    for i in range(0,2):
        x=int(input())
        if(x>5):
            sem3.append(x*4)
            a+=1
    for i in range(2,6):
        y=int(input())
        if(y>5):
            sem3.append(y*3)
            b+=1
    for k in range(6,8):
        z=int(input())
        if(z>5):
            sem3.append(z*2)
            c+=1
    for l in range(8,9):
        m=int(input())
        if(m>5):
            sem3.append(m*1)
            d+=1
    print("Semester 3 - GPA : ",sum(sem3)/((a*4)+(b*3)+(c*2)+(d*1)))
    
def sem4():
    sem4=[]
    a=b=c=0
    print("\nProbability and Random Processes\nElectromagnetic Fields\nElectronic Circuits - 2\nCommunication Theory\nLinear Integrated Circuits\nEnvironmental Science and Engineering\nCircuit Design and Simulation Laboratory\nLinear Integrated Circuits Laboratory")
    for i in range(0,2):
        x=int(input())
        if(x>5):
            sem4.append(x*4)
            a+=1
    for i in range(2,6):
        y=int(input())
        if(y>5):
            sem4.append(y*3)
            b+=1
    for k in range(6,8):
        z=int(input())
        if(z>5):
            sem4.append(z*2)
            c+=1
    print("Semester 4 - GPA : ",sum(sem4)/((a*4)+(b*3)+(c*2)))
    
def sem5():
    sem5=[]
    a=b=c=0
    print("\nDiscrete-Time Signal Processing\nDigital Communication\nComputer Architecture and Organization\nCommunication Networks\nProfessional Elective - 1\nOpen Elective - 1\nDigital Signal Processing Laboratory\nCommunication Systems Laboratory\nCommunication Networks Laboratory")
    for i in range(0,1):
        x=int(input())
        if(x>5):
            sem5.append(x*4)
            a+=1
    for i in range(1,6):
        y=int(input())
        if(y>5):
            sem5.append(y*3)
            b+=1
    for k in range(6,9):
        z=int(input())
        if(z>5):
            sem5.append(z*2)
            c+=1
    print("Semester 5 - GPA : ",sum(sem5)/((a*4)+(b*3)+(c*2)))

def sem6():
    sem6=[]
    a=b=c=0
    print("\nMicroprocessors and Microcontrollers\nVLSI Design\nWireless Communication\nPrinciples of Management\nTransmission Lines and RF Systems\nProfessional Elective - 2\nMicroprocessors and Microcontrollers Laboratory\nVLSI Design Laboratory\nTechnical Seminar")
    for i in range(0,6):
        x=int(input())
        if(x>5):
            sem6.append(x*3)
            a+=1
    for i in range(6,8):
        y=int(input())
        if(y>5):
            sem6.append(y*2)
            b+=1
    for k in range(8,9):
        z=int(input())
        if(z>5):
            sem6.append(z*1)
            c+=1
    print("Semester 6 - GPA : ",sum(sem6)/((a*3)+(b*2)+(c*1)))
    
def sem7():
    sem7=[]
    a=b=0
    print("\nAntennas and Microwave Engineering\nOptical Communication\nEmbedded and Real Time Systems\nAd hoc and Wireless Sensor Networks\nProfessional Elective - 3\nOpen Elective - 2\nEmbedded Laboratory\nAdvanced Communication Laboratory")
    for i in range(0,6):
        x=int(input())
        if(x>5):
            sem7.append(x*3)
            a+=1
    for i in range(6,8):
        y=int(input())
        if(y>5):
            sem7.append(y*2)
            b+=1
    print("Semester 7 - GPA : ",sum(sem7)/((a*3)+(b*2)))

def sem8():
    sem8=[]
    a=b=0
    print("\nProfessional Elective - 4\nProfessional Elective - 5\nProject Work")
    for i in range(0,2):
        x=int(input())
        if(x>5):
            sem8.append(x*3)
            a+=1
    for j in range(2,3):
        y=int(input())
        if(y>5):
            sem8.append(y*10)
            b+=1
    print("Semester 8 - GPA : ",sum(sem8)/((a*3)+(b*10)))

print("Welcome to CGPA calculator")

print("Semester1 - 1\nSemester2 - 2\nSemester3 - 3\nSemester4 - 4\nSemester5 - 5\nSemester6 - 6\nSemester7 - 7\nSemester8 - 8\nTotal CGPA - CGPA")
ch=input()
if(ch=='1'):
    sem1()
elif(ch=='2'):
    sem2()
elif(ch=='3'):
    sem3()
elif(ch=='4'):
    sem4()
elif(ch=='5'):
    sem5()
elif(ch=='6'):
    sem6()
elif(ch=='7'):
    sem7()
elif(ch=='8'):
    sem8()
else:
    CGPA=((sem1()+sem2()+sem3()+sem4()+sem5()+sem6()+sem7()+sem8())/8)
    print("CGPA : ",CGPA)