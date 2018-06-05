import subprocess
import serial
import time
import os
#ser = serial.Serial('COM3', 9600)
# time.sleep(2)
os.chdir(r'F:\darknet-master_dropbox\build\darknet\x64')
cmd = "darknet.exe.exe detector demo cfg/obj_pipe_one_class.data cfg/yolo-pipe_one_class.cfg backup_pipe1/yolo-pipe_one_class_2200.weights -c 1"

p = subprocess.Popen(cmd, stderr=subprocess.PIPE, bufsize=0)
for line in p.stderr:
    print(line.decode())
    if line[-7:] == b'Done!\r\n':
        break


temp = []
for line in p.stderr:
    if(line[:6] == b'Object'):
        print(temp)
        temp = []
    else:
        temp.append(line.decode().replace("\r", "").replace("\n", "").split(","))
    # if(line[:6] == b'mouse:' ):
    # print(line)
     #   ser.write(b'k')
