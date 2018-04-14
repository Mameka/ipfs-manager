#!/usr/bin/env python3
# Manager for IPFS (Interplanetary Fils System)
#---------------------------------------------------------------------------
# Autor: Marco Menne
# E-Mail: marco.menne17@gmail.com
#---------------------------------------------------------------------------

import os
import time

#read local time
localtime = time.asctime( time.localtime(time.time()) )

#define Functions
def banner():
    os.system("clear")
    print(52 * "-")
    print("|" + (50 * " ") + "|")
    print("|" + (20 * " ") + "IPFS Manager" + (18 * " ") + "|")
    print("|" + (50 * " ") + "|")
    print("|" + (50 * " ") + "|")
    print(52 * "-")

def start():
    print(" <1> File/Folder upload")
    print(" <2> File/Folder download")
    print(" <3> List all uploaded hashes with names")
    print(" <4> Search for hashes or names")
    print(" <Enter> or other key to Quit")
    wahl = input("Please choose: \n")
    if wahl == "1":
        data_upload()
    elif wahl == "2":
        data_download()
    elif wahl == "3":
        data_list()
    elif wahl == "4":
        data_search()
    else:
        print("Program quit...")

def data_upload():
    banner()
    print(" ")
    print("File/Folder upload")
    data = input("Please input the absolut path of the file or folder: \n")
    #upload
    #Write timestamp into ipfs-hashes.csv
    with open("ipfs-hashes.csv", "a") as fin:
        fin.write(" " + localtime)
    #Write file/foldername into ipfs-hashes.csv
    command = "ipfs add -r " + data + " >> ipfs-hashes.csv"
    os.system(command)
    print("The data was uploades to IPFS. The hash and the file/foldername")
    print("are printed to the end of 'ipfs-hashes.csv'")
    banner()
    start()

def data_download():
    banner()
    print(" ")
    print("Download file/folder")
    data = input("Please put in the hash of your data: \n")
    #download
    command = "ipfs get " + data
    os.system(command)
    print("The data with the hash")
    print(data)
    print("was downloaded.")
    banner()
    start()

def data_list():
    banner()
    print("")
    print("Overall view of timestamps, hashes and names:")
    print (" ")
    fin = open("ipfs-hashes.csv","r")
    for line in fin:
        print(line.rstrip())
    fin.close()
    print(" ")
    input("Please use a key from keybord to go to the menu...")
    banner()
    start()

def data_search():
    banner()
    print("")
    print("Search for a file/foldername or hash. A fragment of the")
    print("desired data is enough. Placeholder does not work.")
    data = input("Please input hash or name: \n")
    print(" ")
    fin = open("ipfs-hashes.csv")
    for line in fin:
        if data in line:
            print(line.rstrip())
    fin.close()
    print(" ")
    input("Please use a key from keybord to go to the menu...")
    banner()
    start()

banner()
start()
