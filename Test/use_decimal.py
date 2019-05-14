"""
展示了小数点模块decimal的基本用法，保留小数精度（四舍五入）
Date：2019.5.14
"""
import decimal
decimal.getcontext().prec=3 #全局设置
print(decimal.Decimal(2)/decimal.Decimal(3)) #局部设置
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal(2)/decimal.Decimal(3))
