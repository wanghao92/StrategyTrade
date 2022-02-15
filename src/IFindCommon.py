
from iFinDPy import *

#返回码定义
IFIND_CODE_OK = 0   #登录成功
IFIND_CODE_LOGIN_ERROR = -2     #账号或密码错误
IFIND_CODE_HAS_LOGIN = -5       #该账户已经被其他人使用
IFIND_CODE_ACCOUNT_LOCKED = -9  #账户被锁定
IFIND_CODE_REPEAT_LOGIN = -201  #重复登录

IFIND_CODE_NO_LOGIN = -208 #未登录
IFIND_CODE_PARAMS_INVALID = -209  #请求参数不正确

'''实时交易数据指标  --begin-- '''
REALTIME_QUOTES_TRADE_DATA = "tradeDate;"   #交易日期
REALTIME_QUOTES_TRADE_TIME = "tradeTime;"   #交易时间
REALTIME_QUOTES_PRE_CLOASE = "preClose;"    #前收盘价
REALTIME_QUOTES_OPEN = "open;"              #开盘价
REALTIME_QUOTES_HIGH = "high;"              #最高价
REALTIME_QUOTES_LOW = "low;"                #最低价
REALTIME_QUOTES_LATEST = "latest;"          #最新价
REALTIME_QUOTES_LATEEST_AMOUNT = "latestAmount;"    #现额
REALTIME_QUOTES_LATEST_VOLUME = "latestVolume;"     #现量
REALTIME_QUOTES_AVG_PRICE = "latestVolume;"         #均价
REALTIME_QUOTES_CHANGE = "change;"                  #涨跌
REALTIME_QUOTES_CHANGE_RATIO = "changeRatio;"       #涨跌幅
REALTIME_QUOTES_UPPER_LIMIT = "upperLimit;"         #涨停价
REALTIME_QUOTES_DOWN_LIMIT = "downLimit;"           #跌停价
REALTIME_QUOTES_AMOUNT = "amount;"                  #成交额
REALTIME_QUOTES_VOLUME = "volume;"                  #成交量
REALTIME_QUOTES_TURN_OVER_RATIO = "turnoverRatio;"  #换手率
REALTIME_QUOTES_SELL_VOLUME = "sellVolume;"         #内盘
REALTIME_QUOTES_BUY_VOLUME = "buyVolume;"           #外盘
REALTIME_QUOTES_TOTAL_BIDVOL = "totalBidVol;"       #委买十档总量
REALTIME_QUOTES_TOTAL_ASK_VOL = "totalAskVol;"      #委卖十档总量
REALTIME_QUOTES_TOTAL_SHARES = "totalShares;"       #总股本
REALTIME_QUOTES_TOTASL_CAPITAL = "totalCapital;"    #总市值
REALTIME_QUOTES_PB = "pb;"                          #市净率
REALTIME_QUOTES_RISE_DAY_COUNT = "riseDayCount;"    #连涨天数
REALTIME_QUOTES_SUSPENSION_FLAG = "suspensionFlag;" #停牌标志
REALTIME_QUOTES_TRADE_STATUS = "tradeStatus;"       #交易状态
REALTIME_QUOTES_CHG_1MIN = "chg_1min;"              #一分钟涨跌幅
REALTIME_QUOTES_CHG_3MIN = "chg_3min;"              #3分钟涨跌幅
REALTIME_QUOTES_CHG_5MIN = "chg_5min;"              #5分钟涨跌幅
'''实时交易数据指标  --end-- '''

'''高频历史数据指标  --begin-- '''
HIGH_FREQ_OPEN = "open;"        #开盘价
HIGH_FREQ_HIGH = "high;"        #最高价
HIGH_FREQ_LOW = "low;"        #最低价
HIGH_FREQ_CLOSE = "close;"        #收盘价
HIGH_FREQ_AVG_PRICE = "avgPrice;"        #均价
HIGH_FREQ_VOLUME = "volume;"        #成交量
HIGH_FREQ_AMOUNT = "amount;"        #成交额
HIGH_FREQ_CHANGE = "change;"        #涨跌
HIGH_FREQ_CHANGE_RATIO = "changeRatio;"        #涨跌幅
HIGH_FREQ_TURN_OVER_RATIO = "turnoverRatio;"        #换手率
HIGH_FREQ_SELL_VOLUME = "sellVolume;"        #内盘
HIGH_FREQ_BUY_VOLUME = "buyVolume;"        #外盘
'''高频历史数据指标  --end-- '''