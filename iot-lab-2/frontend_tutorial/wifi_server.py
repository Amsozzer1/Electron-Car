import socket
import os
import sys  # Ensure this is imported
import picar_4wd as fc
import sys
import tty
import termios
import asyncio
from picamera2 import Picamera2,Preview

speed= 50
# Correct the path if it's meant to be absolute
sys.path.insert(1, "/home/amsozzer/Car-self_driving-correct")

# Now import the desired function from follow.py within the examples package
from examples.keyboard_control import * 
HOST = "192.168.0.191" # IP address of your Raspberry PI
PORT = 65433          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    s.listen()

    try:
		
        while 1:
            client, clientInfo = s.accept()
            client.sendall(("If you want to quit.Please press q").encode())
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)     
                ANGLE = getSpeed()
                ANGLE_bytes = str(power_val).encode() 
                DATA = data.decode().strip().split(" ")
                if DATA[0] == "stop":
                    fc.stop()
                elif (DATA[0] == "left"):
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.turn_left(sp)
                    else:
                        fc.turn_left(speed)
                elif (DATA[0] == "right"):
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.turn_right(sp)
                    else:
                        fc.turn_right(speed)
                elif (DATA[0] == "Action"):
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.stop()
                    else:
                        fc.stop()
                elif (DATA[0] == "up"):
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.forward(sp)
                    else:
                        fc.forward(speed)
                elif (DATA[0] == "reverse"):
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.backward(sp)
                    else:
                        fc.backward(speed)
                else:
                    print(DATA[0])
                #client.sendall(ANGLE_bytes) # Echo back to client
        
    except Exception as e: 
        print(f"Closing socket because: {e}")
        
        client.close()
        s.close()    

