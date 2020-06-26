# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:10:57 2020

@author: Abhijith
"""
import VeinTest as vt
import Send_Mail as sm
import awsSetup as aws
import reportGen as re
import json
import os
import glob
import time
import subprocess
from bluetooth import *

def receiver():
    subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
    server_sock=BluetoothSocket(RFCOMM)
    port = 1
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)
    ports = server_sock.getsockname()[1]
    uuid = "6fd729af-5af3-4238-8f29-5480e0b732fe"
    advertise_service( server_sock, "VDHRM",    service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ])
    user_data=""
    while True:          
        print ("Waiting to receive Patient's data")
        client_sock, client_info = server_sock.accept()
        #print("Accepted data from "+str(client_info))
        try:
            data = client_sock.recv(1024)
            if len(data) == 0:
                user_data="nil"
                break
            #print(str(data))
            
            my_json = data.decode('utf8')
            datas = json.loads(my_json)
            user_data=datas
            print(datas)
            break
        except IOError:
            pass
        except KeyboardInterrupt:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print ("all done")
            break
    return user_data

#Main program
if __name__ == "__main__":
    Flag=True
    while(Flag):#receiver
        Flag=False
        Udata = receiver()
        if(vt.veinDetect()):
            print("Test Complete!")
        if(Udata != "nil"):
            reportFlag=re.convertHtmlToPdf(Udata)
            if(reportFlag==0):
                print("Report Generation Complete")
                if(aws.upload_file(Udata['FilePath'],Udata['phone']) ==True):
                    sm.Send_Email_On_Test(Udata)
                    print("Report is generated and uploaded to the Cloud and an Email is sent to the user's registered Email ID.")
                    Flag=True
                else:
                    print("couldnot upload report")
                    Flag=True
            else:
                print("couldnot create report")
                Flag=True
        else:
            print("No data received from the App. Try again.")
            Flag=True
