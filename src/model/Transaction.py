from sqlalchemy import Column, Integer, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)

    holdShareId = Column(Integer)

    shareId = Column(Integer)

    price = Column(Float)                           # 交易价格

    time = Column(DateTime)                             # 交易时间

    shareCnt = Column(Integer)                      # 交易笔数(A股：手)

    transactionType = Column(Boolean)                  # 买入true or 卖出false

    def __init__(self, holdShareId, shareId, price, time, shareCnt):
        self.id = None
        self.holdShareId = holdShareId
        self.shareId = shareId
        self.price = price                      #交易价格
        self.time = time                        #交易时间
        self.shareCnt = shareCnt                #交易笔数(A股：手)
        self.transactionType = True                    #买入 or 卖出
