import datetime

from model.HoldShare import *
from model.Transaction import *
from model.Share import *


MONEY_PER_TRANSACTION = 10000

class Customer:
    def __init__(self, totalAccount, usedMoney, name = 'default'):
        self.name = name
        self.oriAccount = totalAccount
        self.totalAccount = totalAccount
        self.usedMoney = usedMoney
        #个人仓位[股票代码，汉语名称，基准价格，当前价格，当前手数， 盈利， 建仓时间, 模拟交易]
        self.holdShares = []

    def addHoldShare(self, stock, stockName, basePrice, shares = 0):
        holdShare = HoldShare(stock, stockName, basePrice, shares, self.name)
        self.holdShares.append(holdShare)

    '''
        交易执行，由策略产生相应的交易，根据交易刷新数据
    '''
    def transactionStock(self, transaction):
        holdShare = HoldShare()     #todo select from holdShares by transation.holdShareId
        #买入
        if transaction.transactionType:
            share = Share(holdShare.id, transaction.price, transaction.shareCnt)
            #todo insert
            holdShare.shares.append(share)
            holdShare.shareCnt += share.shareCnt
            holdShare.holdCost += share.buyPrice * share.shareCnt
            if holdShare.fisrtBuyTime == None :
                holdShare.fisrtBuyTime = datetime.datetime.now()
            #TODO update holdShare
            self.usedMoney -= share.buyPrice * share.shareCnt
        #卖出
        else:
            if holdShare.shareCnt < transaction.shareCnt :
                raise Exception
            share = Share()     #todo select from Share by transaction.shareId
            share.sellTime = datetime.datetime.now()
            share.sellPrice = transaction.price
            share.profit = (share.sellPrice - share.buyPrice) * share.shareCnt
            share.holdPeriod = (share.sellTime - share.buyTime).days

            #todo insert share
            holdShare.shares -= share.shareCnt
            holdShare.profit += share.profit
            holdShare.holdCost -= share.sellPrice * share.shareCnt
            if holdShare.shareCnt == 0 :
                holdShare.lastBuyTime = datetime.datetime.now()
            #todo update holdShare
            self.usedMoney += share.sellPrice * share.shareCnt

    '''
        计算单只股票的仓位, 当前价格 * 数量 / 总数
        @return [股票仓位，占总资产的仓位]
    '''
    def getShareRate(self, holdShareId):
        holdShares = []  #todo select by user
        total = 0
        sharePrice = 0
        for holdShare in holdShares :
            total += holdShare.nowPrice * holdShare.shareCnt
            if holdShare.id == holdShareId :
                sharePrice = holdShare.nowPrice * holdShare.shareCnt

        return [sharePrice / total,  sharePrice / self.totalAccount]





