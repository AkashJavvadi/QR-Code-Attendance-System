import pyqrcode
import png
from pyqrcode import QRCode
import cv2
import webbrowser
import datetime
print("Hi-----------------------------------------------------------------------------------------------------------------")
print("0)To generate a QR for New Student")
print("1)To scan a QR from the Student")
print("-----------------------------------------------------------------------------------------------------------------")
userinput=input("Select a Number: ")

if(userinput=="0"):
  no_of_students=int(input("Enter No.of Students : "))
  for i in range(no_of_students):
    RollNumber=input("Enter Student RollNumber : ").upper()
    url = pyqrcode.create(RollNumber)
    url.png(RollNumber+".png", scale = 6)
    break
elif(userinput=="1"):
  f=open("D:\\EH_Tools\\LIST.csv")
  f.readline()
  students=f.readlines()
  f.close()

  f=open("D:\\EH_Tools\\LIST.csv")
  f.readline()
  students2=f.readlines()
  f.close()

  for i in range(len(students)):
    students[i]=students[i].replace("\n","").upper()
  for i in range(len(students2)):
    students2[i]=students2[i].replace("\n","").upper()
  cap=cv2.VideoCapture(0)
  detector=cv2.QRCodeDetector()
  f=open("D:\\EH_Tools\\Student.csv","a")
  f.write("\n")
  f.write("---------------------------------------------------------------------------------------------------------")
  f.write("\n\n")
  f.close()
  while True:
    _,img=cap.read()
    
    data,one, _=detector.detectAndDecode(img)
    if(len(data)>1):
        if data in students:
          print(data+"-present")
          now=datetime.datetime.now()
          s=now.strftime("-Present    date: %d-%m-%y    time: %H:%M:%S " )
          f=open("D:\\EH_Tools\\Student.csv","a")
          f.write( data+s)
          f.write("\n")
          f.close()
          students.remove(data)
        elif data in students2:
          print(data+"-Already Present")
        else:
          print("Student is Invalid")
    
    cv2.imshow('show your qr',img)
    if cv2.waitKey(500)==ord('q'):
      break
  print("No.of Students Present: ",len(students2)-len(students))
  print("No.of Students Absent: ",len(students))
  print(students)
  for i in students:
    now=datetime.datetime.now()
    s1=now.strftime("-Absent     date: %d-%m-%y    time: %H:%M:%S " )
    f=open("D:\\EH_Tools\\Student.csv","a")
    f.write(i+s1)
    f.write("\n")
    f.close()


else:
  print("select valid number")
  
  
cv2.destroyAllWindows()