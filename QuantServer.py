# -*- coding: utf-8 -*-
import os
import shutil
import zipfile
import time
import re
import sqlite3
import urllib
import Algorithmlib as ALG
import Sharedefine as SD
import pandas as pd

def cal():
    array1= [7,1,5,3,6,4]
    ret1=ALG.getMaxProfit(array1)
    ret2=ALG.get_mdd(array1)
    array2=[100, 101, 102, 105, 103, 101, 102, 107, 106,104]
    ret3 = ALG.getMaxProfit(array2)
    ret4 = ALG.get_mdd(array2)
    pass

def trace(inURL):
    pass

"""
name:
desc:单纯初始化
@params: a raw dataframe downloaded from datavendor
@return: a dataframe with data only in market open time
"""
def Init(df):
    if df is None:
        return None
    df.rename(inplace=True,columns=SD.option_ch2en)
    return

"""
name:
desc:删除无效时间区间的数据
@params: a raw dataframe , 规则
@return: a dataframe with data only in market open time
"""
def raw2tick(df, Inplace=False):
    if df is None:
        return None
    if(Inplace==True):
        for cond in SD.option_closetime:
            df.drop(df[(df.LastModifyTime >= cond[0]) & (df.LastModifyTime < cond[1])].index, inplace=True)
    else:
        ret=df
        for cond in SD.option_closetime:
            ret.drop(df[(df.LastModifyTime >= cond[0]) & (df.LastModifyTime < cond[1])].index, inplace=False)
        return ret

"""
name:
desc:抽样
@params: a raw dataframe, 规则
@return: a dataframe with data only in market open time
"""
def sampleTick(df,interval=2,type='sec'):
    if df is None:
        return None
    ret=df[0::interval]
    return ret

"""
name:
desc:抽样
@params: a raw dataframe
@return: trade datetime includes night/day open, close datetime
        if no break in morning, morning break start/end datetime 
        would be set as morning_trade_end_time
"""
def get_trade_time():
    pass

"""
name:
desc:只抽三个维度的
@params: a raw dataframe of market tick data
@return: a dataframe with Open High Low Close price sampled by 1 minus
"""
def tick2min(df):
    TargetCol=[ 'OpeningPrice','HighPrice','LowPrice','ClosePrice']
    for i in TargetCol:
        if i not in df.columns:
            return
    return df[]
    pass

if __name__ == "__main__":
    csv = pd.read_csv('./rawdata/rb2005_20200228.csv',encoding='gb2312')
    Init(csv)
    raw2tick(csv,'I')
    sampledcsv=sampleTick(csv,interval=60)
    #trace('http://www.baidu.com/')
    cal()
    pass