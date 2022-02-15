# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
from IFindAccess import *



def realTimeQuotesTest():
    ifindAccess = IFindAccess()
    result = ifindAccess.realtimeQuotes("600004.SH", REALTIME_QUOTES_OPEN + REALTIME_QUOTES_HIGH)
    print(result)

def highFreqSequenceTest():
    ifindAccess = IFindAccess()
    result = ifindAccess.highFreqSequence("600004.SH",
                                        REALTIME_QUOTES_OPEN + REALTIME_QUOTES_HIGH + REALTIME_QUOTES_LATEST,
                                        ifindAccess.highFreqGetFreq(1),
                                        "2021-07-04 09:30:00",
                                        "2021-07-09 15:30:00")
    print(result)
    print(result.data['time'])
    # print(result.data.iloc[1:5, :])
    print(result.data['time'].iloc[1])
    print(result.data['time'].loc[2])
    print(result.data.iat[0, 0])
    print(result.data.iloc[1][0])
    print(result.data.loc[1]['time'])
    print(result.data.shape)
    print(result.data.shape[0], result.data.shape[1])

    for index, row in result.data.iterrows() :
        print("index:%d, open:%f", index, row['high'])


def strategy():
    ifindAccess = IFindAccess()

    ifindAccess.highFreqSequence("600004.SH",
                                REALTIME_QUOTES_OPEN + REALTIME_QUOTES_HIGH + HIGH_FREQ_CLOSE,
                                ifindAccess.highFreqGetFreq(1),
                                "2021-07-04 09:30:00",
                                "2021-07-09 15:30:00")



if __name__ == '__main__':
    highFreqSequenceTest()