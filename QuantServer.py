# -*- coding: utf-8 -*-
import os
import shutil
import zipfile
import time
import re
import sqlite3
import urllib
import Algorithmlib as alg
import Sharedefine as sd
import pandas as pd

def cal():
    array1= [7,1,5,3,6,4]
    ret1=alg.getMaxProfit(array1)
    ret2=alg.get_mdd(array1)
    array2=[100, 101, 102, 105, 103, 101, 102, 107, 106,104]
    ret3 = alg.getMaxProfit(array2)
    ret4 = alg.get_mdd(array2)
    pass

def trace(inURL):
    pass

'''
Input: a raw dataframe downloaded from datavendor
Return: a dataframe with data only in market open time
'''
def Init(df):
    if df is None:
        return None
    df.rename(inplace=True,columns=sd.option_ch2en)
    return

def raw2tick(df, symbol='IH'):
    if df is None:
        return None
    df.drop(df[(df.LastModifyTime<u'09:00:00')].index,inplace=True)
    df.drop(df[(df.LastModifyTime >= u'10:15:00') & (df.LastModifyTime < u'10:30:00')].index, inplace=True)
    df.drop(df[(df.LastModifyTime >= u'11:30:00') & (df.LastModifyTime < u'13:30:00')].index, inplace=True)
    df.drop(df[(df.LastModifyTime > u'15:00:00')].index, inplace=True)
    pass

def get_trade_time():
    pass

def tick2min():
    pass

if __name__ == "__main__":
    csv = pd.read_csv('./rawdata/rb2005_20200228.csv',encoding='gb2312')
    Init(csv)
    raw2tick(csv,'I')
    #trace('http://www.baidu.com/')
    cal()
    pass