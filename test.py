TV = P - SV(期权的时间价值=期权价格-空间价值） 
from vnpy.trader.utility import load_json
from vnpy_scripttrader import init_cli_trading
from vnpy_ctp import CtpGateway

# 连接到服务器
setting = {
    '用户名': '202108',
    '密码': 'joonchan00',
    '经纪商代码': '9999',
    '交易服务器': '180.168.146.187:10212',
    '行情服务器': '180.168.146.187:10212',
    '产品名称': 'simnow client test',
    '授权编码': '0000000000000000',
    '产品信息': ''

}
engine = init_cli_trading([CtpGateway])
engine.connect_gateway(setting, "CTP")

# 查询所有合约
engine.get_all_contracts(use_df=True)

# 订阅行情
strike_prices = list(range(3300,3800,50)
vt_symbols = ['IF2312.CFFEX']

# 生成合约代码
for strike_price in strike_prices:
    vt_symbol = f'IO2312-C-{strike_price}.CFFEX'
    vt_symbols.append(vt_symbol)
engine.subscibe(vt_symbols)

# 查询行情
underlying_price = engine.get_tick('IF2312.CFFEX').last_price

for strike_price in strike_prices:
    vt_symbol = f'IO2312-C-{strike_price}.CFFEX'
    tick = engine.get_tick(vt_symbol)
    if tick:
        space_value = max(underlying_price - strike_price, 0 )
        time_value = tick.last_price - space_value
        print('--------------------')
        print('期权代码‘，tick.symbol)
        print('最新价‘，tick.last_price)
        print('标的价格‘，underlying_price)
        print('空间价值‘，space_value)
        print('时间价值', time_vlaue)
        print('当前时间‘，tick.datetime)
















  
