from sqlalchemy import Column, Integer, Float, DateTime, String
from Share import *
import numpy as np


Base = declarative_base()

'''
    某只股票的持仓详情
    从买入到全部卖出，包括加仓、减仓等操作
'''
class HoldShare:

    __tablename__ = 'hold_share'

    id = Column(Integer, primary_key=True)
    user = Column(String)           # 所属账户
    stock = Column(String)          # 证券编码
    StockName = Column(String)      # 证券名称
    basePrice = Column(Float)       # 基线价格
    nowPrice = Column(Float)        # 当前价格
    shareCnt = Column(Integer)      # 持仓（A股：手）  当为0时代表此股已全部卖出，当从新买入时会产生新的一条记录
    buyCost = Column(Integer)       # 买入价格 当前持仓（不包含已经卖出的）的股票对应的买入价格的总和
    holdCost = Column(Integer)      # 持有价格 当买入时(买入价格*数量)，当卖出时(卖出价格*数量)
    profit = Column(Float)          # 利润
    fisrtBuyTime = Column(DateTime)     # 建仓时间
    lastBuyTime = Column(DateTime)      # 平仓时间
    simulationTrading = Column(Integer)  # 默认是模拟交易


    def __init__(self, stock, stockName, basePrice, shareCnt, user = 'default'):
        self.user = user                #所属账户
        self.stock = stock              #证券编码
        self.StockName = stockName      #证券名称
        self.basePrice = basePrice      #基线价格
        self.shareCnt = shareCnt        #持仓（A股：手）
        self.buyCost = 0
        self.holdCost = 0
        self.profit = 0                 #利润
        self.shareRate = 0              #仓位占比，不保存数据库，用于算法参数传递
        self.fisrtBuyTime = None        #建仓时间
        self.lastBuyTime = None         #平仓时间
        self.simulationTrading = True   #默认是模拟交易
        self.shares = []                #详细持仓 保存在数据库中


