#!/usr/bin/python3

import argparse
import time
import os

data = []

def showProgress(i,maximum):
    barlength = 50
    done = int((i/maximum)*barlength)
    rem = barlength - done
    print("[",end="")
    for i in range(done):
        print("=",end="")
    for i in range(rem):
        print(" ",end="")
    print("]")

def init():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r","--runtime",default=10)
    args = ap.parse_args()
    return args

def run(args):
    for i in range(args.runtime):
        time.sleep(1)
        data.append(i)
        os.system('clear')
        showProgress(i,args.runtime-1)

def windup():
    f = open("data/test.txt","w")
    for d in data:
        f.write(str(d))


if __name__ == "__main__":
    print("starting..")
    args = init()
    try:
        run(args)
    except KeyboardInterrupt:
        print("keyboard interrupt recieved.. cancelling run")
    windup()
    print("ending")
