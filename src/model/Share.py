import datetime

from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Share(Base):
    __tablename__ = 'share'

    id = Column(Integer, primary_key=True)

    holdShareId = Column(Integer)                       #持仓id

    buyPrice = Column(Integer)                          # 买入价格(单位：分)

    buyTime = Column(DateTime)                              # 买入时间

    shareCnt = Column(Integer)                          # 交易笔数(A股：手)

    sellPrice = Column(Integer)                         # 卖出价格

    sellTime = Column(DateTime)                             # 卖出时间

    profit = Column(Integer)                            #此次交易利润

    holdPeriod = Column(Integer)                        #持股天数

    def __init__(self, holdSharedId, buyPrice, shareCnt):
        self.holdShareId = holdSharedId
        self.buyPrice = buyPrice
        self.shareCnt = shareCnt
        self.buyTime = datetime.datetime.now()


