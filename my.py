from datetime import datetime
from time import sleep

import pandas as pd
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BarData
from vnpy.trader.utility import ArrayManager


data = pd.read_csv(r"C:\Users\admin\Downloads\IF888_CFFEX.csv",encoding="utf8",nrows=1000)
print(data.columns)

for index, i in data.iterrows():
    bar = BarData(
        symbol="IF888",
        exchange=Exchange.CFFEX,
        interval=Interval.MINUTE,
        datetime=i['datetime'],
        gateway_name="CTP",
        open_price=float(i["open"]),
        high_price=float(i["high"]),
        low_price=float(i["low"]),
        close_price=float(i["close"]),
        volume=float(i["volume"]),
        turnover=float(i["turnover"]),
    )
    am = ArrayManager()
    am.update_bar(bar)
    sleep(1)




