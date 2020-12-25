# -*- coding: utf-8 -*-

#左闭右开
option_opentime=[(u'09:00:00',u'10:15:00'),
                 (u'10:30:00',u'11:30:00'),
                 (u'13:30:00',u'15:00:00')
                 ]

#左闭右开
option_closetime=[(u'00:00:00',u'09:00:00'),
                  (u'10:15:00',u'10:30:00'),
                  (u'11:30:00',u'13:30:00'),
                  (u'15:00:00',u'24:00:00')
                  ]

option_ch2en=\
{
    u'交易日':'TradingDate',
    u'合约代码':'ContractCode',
    u'交易所代码':'ExchangeCode',
    u'合约在交易所的代码':'ExchangeCodeOfContract',
    u'最新价':'NewestPrice',
    u'上次结算价':'LastClearPrice',
    u'昨收盘':'LastClosePrice',
    u'昨持仓量':'yesterdayPositionVolume',
    u'今开盘':'OpeningPrice',
    u'最高价':'HighPrice',
    u'最低价':'LowPrice',
    u'数量':'TradeVolume',
    u'成交金额':'TradeAmount',
    u'持仓量':'PositionVolume',
    u'今收盘':'ClosePrice',
    u'本次结算价':'ClearPrice',
    u'涨停板价':'UpLimitedPrice',
    u'跌停板价':'DownLimitedPrice',
    u'昨虚实度':'PreDelta ',
    u'今虚实度':'CurrDelta',
    u'最后修改时间':'LastModifyTime',
    u'最后修改毫秒':'LastModifyMS',
    u'申买价一':'BuyPrice1',
    u'申买量一':'BuyVolume1',
    u'申卖价一':'SellPrice1',
    u'申卖量一':'SellVolume1',
    u'申买价二':'BuyPrice2',
    u'申买量二':'BuyVolume2',
    u'申卖价二':'SellPrice2',
    u'申卖量二':'SellVolume2',
    u'申买价三':'BuyPrice3',
    u'申买量三':'BuyVolume3',
    u'申卖价三':'SellPrice3',
    u'申卖量三':'SellVolume3',
    u'申买价四':'BuyPrice4',
    u'申买量四':'BuyVolume4',
    u'申卖价四':'SellPrice4',
    u'申卖量四':'SellVolume4',
    u'申买价五':'BuyPrice5',
    u'申买量五':'BuyVolume5',
    u'申卖价五':'SellPrice5',
    u'申卖量五':'SellVolume5',
    u'当日均价':'IntradayAveragePrice',
    u'业务日期':'BusinessDate'
}

