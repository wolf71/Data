'''
  利用 pandas, 通过网页抓取 上市公司 某个年度财务信息 保存到 csv 文件

'''

import pandas as pd

gtime = '2020-12-31'
fname = 'corp202012.csv'
pages = 237

# gtime = '2018-12-31'
# fname = 'corp201812.csv'
# pages = 237

# gtime = '2019-12-31'
# fname = 'corp201912.csv'
# pages = 237


# 爬取全部页 最后页数 + 1 !!
for i in range(1, pages):
    # 显示进度信息      
    if i % 10 == 1: print('Load Page %d ...'%i)
    # 构造获取地址, 获取数据
    tb = pd.read_html( 'http://s.askci.com/stock/a/?reportTime=%s&pageNum=%s' % (gtime, str(i)) )[3]
    if i== 1:
      # 第一页写入表头信息, 其它不需要
      tb.to_csv(fname, mode='a', encoding='utf_8_sig', header=1, index=0)
    else:
      tb.to_csv(fname, mode='a', encoding='utf_8_sig', header=0, index=0)


'''
# 数据处理

## 1. 用文本编辑器修改表头信息
- id,stockid,sname,name,prov,city,revenue,netprofit,employee,listingdate,f1,f2,industry,producttype,mainbusiness 
- 因为 招股书,公司财报数据字段为空 因此用 f1,f2 代替, 后续过滤掉
- 原表头:
  - 序号,股票代码,股票简称,公司名称,省份,城市,主营业务收入(202012),净利润(202012),员工人数,上市日期,招股书,公司财报,行业分类,产品类型,主营业务


## 2. 执行 Qsqlite 脚本
- Qsqlite getCorp.txt 
- 完成处理后, 将会输出 output.csv 最终文件

'''