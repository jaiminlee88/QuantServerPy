# -*- coding: utf-8 -*-
import pandas
import numpy as nu

def getMaxProfit(inArray):
    mlen=len(inArray)
    if mlen<=1:
        return 0
    minPrice=inArray[0]
    outMax=0
    outMin=0
    maxProfit=0
    for i in inArray:
        if i < minPrice:
            minPrice = i
        elif i-minPrice > maxProfit:
            maxProfit = i - minPrice
            outMax = i
            outMin=minPrice
    return [outMin,outMax,maxProfit]

def getMaxLoss(inArray):
    mlen = len(inArray)
    if mlen <= 1:
        return 0
    maxPrice = inArray[0]
    outMax=0
    outMin=0
    maxLoss = 0
    for i in inArray:
        if i>maxPrice:
            maxPrice=i
        elif maxPrice-i>maxLoss:
            maxLoss=maxPrice-i
            outMin=i
            outMax=maxPrice
    return [outMax,outMin,maxLoss]

"""
 A maximum drawdown (MDD) is the
 maximum observed loss from a peak to a trough of a
 portfolio, before a new peak is attained.
"""
def get_mdd(inArray):
    return getMaxLoss(inArray)


class KLine:
    def __init__(self):
        self.rawIn=""

    def get_KLineByType(self,type):

        pass



if __name__ == "__main__":
    pass
