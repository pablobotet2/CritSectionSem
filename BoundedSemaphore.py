#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:53:50 2022

@author: Pablo Martínez Botet
"""

from multiprocessing import Process, Lock, BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array

"El N sería el número de procesos"
N=8
k=1

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
    l=BoundedSemaphore(k)
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