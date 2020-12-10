# -*- coding: utf-8 -*-
import os
import shutil
import zipfile
import time
import re
import sqlite3
import urllib
import urllib3
import Algorithmlib as alg
import Sharedefine as sd

def cal():
    array1= [7,1,5,3,6,4]
    ret1=alg.getMaxProfit(array1)
    ret2=alg.get_mdd(array1)
    array2=[100, 101, 102, 105, 103, 101, 102, 107, 106,104]
    ret3 = alg.getMaxProfit(array2)
    ret4 = alg.get_mdd(array2)
    pass

def trace(inURL):
    if inURL=="":
        return
    http = urllib3.PoolManager()
    r = http.request('GET',inURL,preload_content=False)
    for i in r.stream(32):
        print(i)
    r.release_conn()
    pass


def raw2tick():
    pass

def get_trade_time():
    pass

def tick2min():
    pass

if __name__ == "__main__":
    #trace('http://www.baidu.com/')
    cal()
    pass