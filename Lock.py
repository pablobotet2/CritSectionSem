#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:23:22 2022

@author: alumno
"""

from multiprocessing import Process, Lock
from multiprocessing import current_process
from multiprocessing import Value, Array

"El N sería el número de procesos"
N=8

def task(common,tid,l):
    a=0
    for i in range (100):
        print (f'{tid}-{i}:Non-critical Section')
        a+=1
        print (f'{tid}-{i}:End of non-critical Section')
        l.acquire()
        try:
            print ("Start of critical section")
            v = common.value+1
            print(f'{tid}-{i}:Inside critical section')
            common.value=v
            print(f'{tid}-{i}:End of critical section')
        finally:
            l.release()
           

        
def main():
    lp=[]
    common = Value('i',0)
    l=Lock()
    for tid in range(N):
        lp.append (Process(target=task, args=(common,tid,l)))
    print (f"Valor inicial del contador {common.value}")
    
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
        
    print (f"Valor final del contador{common.value}")
    print ("fin")
    
if __name__=="__main__":
    main()