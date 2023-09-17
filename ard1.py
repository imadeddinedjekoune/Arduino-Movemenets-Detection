import numpy as np
import serial
import time
import _thread

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

ser = serial.Serial('COM14', 9600)
rl = ReadLine(ser)

ser2 = serial.Serial('COM7', 9600)
rl2 = ReadLine(ser2)

def readFile():
    while True:
        f = open("ard1.txt", "a")
        val1 = f.read()
        f = open("ard2.txt", "a")
        val2 = f.read()

        #print(val1,val2)
        


def f1():
    while True:
        
        p = float(str(rl.readline())[19:25])
        f = float(str(rl.readline())[18:24])
        c = float(str(rl.readline())[22:28])
        str(rl.readline())
        moveD = np.argmax([p,f,c])
        #print([p,f,c])
        f = open("ard1.txt","w")
        
        f.write(str(moveD))
        f.close()
        

        
def f2():
    while True:
        p = float(str(rl2.readline())[19:25])
        f = float(str(rl2.readline())[18:24])
        c = float(str(rl2.readline())[22:28])
        str(rl2.readline())
        moveD = np.argmax([p,f,c])

        time.sleep(0.3)

        try:
            fich = open("ard1.txt","r")
           # print([p,f,c])
            

            
            try:
                ard1 = int(fich.read())
            except:
                ard1 = -1 
            ard2 = moveD

            
            if (ard1==0 ):
                print("le geste effectuer est : ")
                if(ard2 == 0):
                    print("pousser")
                if(ard2 == 1 ):
                    print("Box Gauche")
                if(ard2 == 2 ):
                    print("Box Cercler Gauche")
            if (ard1==1 ):
                print("le geste effectuer est : ")
                if(ard2 == 0):
                    print("Box Droite")
                if(ard2 == 1 ):
                    print("Tirer")
                if(ard2 == 2 ):
                    print("Reculer Droite")
                    
            if (ard1==2 ):
                print("le geste effectuer est : ")
                if(ard2 == 0):
                    print("Box Cercler Droite")
                if(ard2 == 1 ):
                    print("Reculer Gauche")
                if(ard2 == 2 ):
                    print("Geste Cerculaire")
                

            fich = open("ard1.txt","w")
            fich.close()
            
        except:
            a = 1

        
        
        


# Create two threads as follows
try:
   _thread.start_new_thread( f1, ( ) )
   _thread.start_new_thread( f2, ( ) )
   #_thread.start_new_thread( readFile, ( ) )
   
except:
   print("Error: unable to start thread")

while 1:
   pass
