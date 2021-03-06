#coding:utf-8



"""
抽取列表后的第一层过滤
"""
MAX_SAMEITEM_COUNT = 20
MIN_DISCOUNT_PRICE = 20
MIN_DISCOUNT = 0.8

"""
抽取相同列表后的第一层过滤
"""
MIN_SAME_RATESUM = 1




"""
比价时进入比价的最低信用值
"""
CP_MIN_CREDIT = 1
"""
比价时与均值差价的最小范围
"""
CP_DIFF_MIN = 5
CP_DIFF_MIN_RATE = 0.09
"""
同疑似好产品的最大差价范围
"""
X_MAX_DIFF_RATE = 0.05
X_MAX_DIFF = 100
"""
疑似好产品的信用
"""
CP_CREDIT_GOOD = 3

"""
样本最大偏离度
"""
MAX_SAMPLE_DIFF_RATE = 3



"""
进入formal的条件
"""
OUT_GOOD_CHANGERANK = 0
OUT_GOOD_CPRANK = -1
OUT_GOOD_ITEMRANK = 0.2
IN_GOOD_CPRANK = 1
IN_GOOD_ITEMRANK = 0.6
IN_GOOD_CHANGERANK = 0.2
INTER_GOOD_ITEMRANK = 0.3
INTER_GOOD_CHANGERANK = 0.05


pagetocrawl = {
        "nvzhuang":range(1,11),
        "nvxie":range(1,11),
        "wenxiong":range(1,11),
        "shuiyi":range(1,11),
        "sushen":range(1,11),
        "danjianbao":range(1,11),
        "shoutibao":range(1,11),
        "xiekuabao":range(1,11),
        "qianbao":range(1,11),
        "shounabao":range(1,11),
        "tongzhuang":range(1,11),
        "chuangshang":range(1,11),
        "jiajushipin":range(1,11),
        "peishi":range(1,11),
        "maorongwanju":range(1,11),
}


other_dict = {
        "nvzhuang":
            {"fl":"Shangpml"},
        "nvxie":
            {"fl":"nx_shangpml"},
        "wenxiong":
            {"fl":"1625","mSelect":"false"},
        "shuiyi":
            {"fl":"1625","msp":1,"mSelect":"false"},
        "danjianbao":
            {"fl":"danjianx","mSelect":"false"},
        "shoutibao":
            {"fl":"xiekuabaox","mSelect":"false"},
        "xiekuabao":
            {"fl":"xiekuabaox","mSelect":"false"},
        "qianbao":
            {"fl":"qianbaox","mSelect":"false"},
        "shounabao":
            {"fl":"shounabaox","mSelect":"false"},
        "tongzhuang":
            {"gobaby":1,"spercent":95,"mSelect":"false"},
        "chuangshang":
            {"sd":0},
        "jiajushipin":
            {"sd":0},
        "maorongwanju":
            {"sort":"coefp"}
}
