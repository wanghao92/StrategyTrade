

from IFindCommon import *

class IFindAccess:
    def __init__(self):

        self.loginIFind()


    def realtimeQuotes(self, stockCode, quota):
        return THS_RQ(stockCode, quota)

#
#   高频交易信息获取接口列表  -----begin-------
#   该命令用来获取证券的分钟K线数据，包括历史日期和当前日期。
#   分钟线的周期可以自己选定，目前可选的周期有1分钟、3分钟、5分钟、10分钟、15分钟、30分钟和60分钟。
#   通过高频序列函数还可以获取证券的逐笔成交数据以及一些技术指标数据
#
    '''
        @description：获取历史交易数据分钟k线图
        @param:
            stockCode：股票代码
            indicate：获取参数
            freq：数据采样频率
            startTime：开始时间，格式"2021-1-1 09:30:30"
            endTime：结束时间，格式"2021-1-1 09:30:30"
    '''
    def highFreqSequence(self, stockCode, indicate, freq, startTime, endTime):
        return THS_HF(stockCode, indicate, freq, startTime, endTime)

    '''
        @description：设置高频序列周期
        @param:
            interval 时间间隔，单位分钟，可取值（1/3/5/10/15/30/60）
            startOnDay: 每天的起始时间，格式"09:30:00"
            endOnDay：每天结束时间，格式"15:30:00"
            fill：非交易时间数据填充，可取值：Previous(沿用之前数据)、Black(空置)、具体数值(自定义数值)、Original(缺省)[默认]
    '''
    def highFreqGetFreq(self, interval, startOnDay = "09:30:00", endOnDay = "15:00:00", fill = "Original"):
        if interval < 1 or interval > 60 :
            raise Exception("interval format error! interval must be [1, 60]")

        return "interval:" + str(interval) \
               + ",startTime:" + startOnDay \
               + ",endTime:" + endOnDay \
               + ", fill:" + fill
#
#   高频交易信息获取接口列表  -----end-------
#


    def loginIFind(self):
        result = THS_iFinDLogin("cqjc001", "zzzt2021")
        if (result == IFIND_CODE_OK):
            print("login ifind success...")
        elif result == IFIND_CODE_LOGIN_ERROR:
            print("account or password is error!")
            raise Exception("ifind login in error")
        elif result == IFIND_CODE_REPEAT_LOGIN:
            print("repeat login in, this account is logined!")
            raise Exception("ifind login in error")
        else:
            print("unknow error, errorCode is %d", result)
            raise Exception("ifind login in error")
        return result