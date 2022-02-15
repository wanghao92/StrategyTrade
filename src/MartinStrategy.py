import numpy as np
from model.HoldShare import *

BASE_PRICE_LADDER = 100  #向下价格截图数。最大价格阶梯数为该值两倍
MONEY_PER_TRANSACTION = 10000
YIELD_RATE = 0.01
class MartinStrategy:
    def __init__(self, maxAccount, usedMoney, yieldRate):
        self.yieldRate = yieldRate
        #个人仓位[股票代码，汉语名称，基准价格，当前价格，当前手数， 盈利， 建仓时间, 模拟交易]
        self.holdShares = []


    '''
        马丁策略：判断当前是否卖出
    '''
    def sellTransaction(self, nowPrice, holdShare):
        # 判断是否需要卖出
        for share in holdShare.shares:
            if share.sellPrice == 0:
                continue
            if nowPrice > share.buyPrice * self.yieldRate:
                return

    def buyTransaction(self, nowPrice, holdShare, account):
        priceLadder = self.calPriceLadder(holdShare.basePrice)
        buyPrice = 0
        for i in range(BASE_PRICE_LADDER, 1):
            if nowPrice < priceLadder[i]:
                buyPrice = priceLadder[i]
                break
        for share in holdShare:
            if share.sellPrice == 0:
                continue
            if share.buyPrice == buyPrice:
                return
        return 

    '''
        产生价格梯度
    '''
    def calPriceLadder(self, basePrice):
        priceLadder = np.zeros(BASE_PRICE_LADDER * 2)
        priceLadder[BASE_PRICE_LADDER] = basePrice
        for i in range(1, BASE_PRICE_LADDER):
            priceLadder[BASE_PRICE_LADDER + i] = priceLadder[BASE_PRICE_LADDER + i - 1] * 1.01
            priceLadder[BASE_PRICE_LADDER - i] = priceLadder[BASE_PRICE_LADDER - i + 1] * 0.99
        return priceLadder

    def getBuyShareCnt(self, price):
        if price > MONEY_PER_TRANSACTION :
            return 1
        else :
            return (int)((MONEY_PER_TRANSACTION / price) + 1)

if __name__ == '__main__':
    position = HoldShare('ccc', 'zxcvb', 15.5)
    print(position.priceLadder)