#!/usr/bin/env python3

import os
import netifaces
import pyexcel

from netmiko import ConnectHandler

def act_inac():
     print(netifaces.interfaces())
     for i in netifaces.interfaces():
         print('\n****** details of interface - ' + i + ' ******')
         try:
             print('MAC: ', end='')
             print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
             print('IP: ', end='')
             print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
         except:          # This is a new line
             print('Could not collect adapter information')



def retv_excel(par):
    d = {}
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        d.update( { record['IP'] : record['MAC'] } )
    return d
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)
    
    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def main():
    act_inac()
    input("Press Enter to Continue")
    file_location = str(input("\nWhere is the file location? "))
    entry = retv_excel(file_location)
    print("\n***** BEGIN ICMP CHECKING *****")
    for x in entry.keys():
        if ping_router(x):
            print("\n\t**IP: - " + x + " - responding to ICMP\n")
        else:            print("\n\t**IP: - " + x + " - NOT responding to ICMP\n")

main()



