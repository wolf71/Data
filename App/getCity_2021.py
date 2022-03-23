#
# 获取 中国省-城市-乡镇-街道 信息
# 国家统计局信息源: http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/index.html
#

import requests
import re, time 

r_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/'

ha = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


# 获取地址的 目录部分，例如 123/123.html -? 123/
def gurl(url):
  r = '/'.join(url.split('/')[:-1])
  if len(r) > 1:
    r += '/'
  return r

def getinfo(url):
  # 如果连接超时出错，重试 
  # raise ConnectionError(e, request=request)  requests.exceptions.ConnectionError:
  while True:
    # 缓冲延时，避免服务器拒绝
    time.sleep(0.3)
    try:
      r = requests.get(url, timeout = 30, headers=ha)
      if r.status_code == 200:
        break
      else:
        # 返回结果不为 200 , 继续重试
        print('# Err:',r.status_code, url )
    except:
      # 重试
      print('# !! Block, waitting 66s,and then retry.', time.asctime( time.localtime(time.time()) ))
      time.sleep(66)

  # 返回结果(将 回车换行去掉)
  r.encoding = 'UTF-8'
  return r.text.replace('\r','').replace('\n','').replace('\t','')

#
# 数据抓取 (解析首页 1-省份)
#
r = getinfo(r_url + 'index.html')
if r:
  plist = re.findall('<a href="(.+?)">(.+?)<br /></a>', r)

for i in plist:
  city = []
  print('#',i[1], time.asctime( time.localtime(time.time()) ) )
  city.append( (i[0][:2], i[1], 1) )
  r = getinfo(r_url + i[0])

  # 解析 2-市
  if r:
    # 找寻类似 ID,  name这类没有下级链接的数据（例如：市辖区）
    plist0 = re.findall('<td>(\d+?)</td>.*?<td>(.+?)</td>', r)
    if plist0: print('# 2 Found <id><name> record', len(plist0))
    for z in plist0:
      city.append( (z[0], z[1], 2))
      # 找寻 下级数据 ref, ID, name     
    plist2 = re.findall('<a href="(.+?)">(.+?)</a></td>.+?d><a href=".+?">(.+?)</a>', r)
    if not plist2: print('# 2 Not found info in :', r_url + i[0])

    for j in plist2:
      city.append( (j[1], j[2], 2) )
      r = getinfo(r_url + gurl(i[0]) + j[0])
      # 解析 3-区/县
      if r:
        # 找寻类似 ID,  name这类没有下级链接的数据（例如：市辖区）
        plist0 = re.findall('<td>(\d+?)</td>.*?<td>(.+?)</td>', r)
        if plist0: print('# 3 Found <id><name> record', len(plist0))
        for z in plist0:
          city.append( (z[0], z[1], 3))
        # 找寻 下级数据 ref, ID, name 
        plist3 = re.findall('<a href="(.+?)">(.+?)</a></td>.+?d><a href=".+?">(.+?)</a>', r)
        if not plist3: print('# 3 Not found info in :', r_url + gurl(i[0]) + j[0])

      for k in plist3:
        city.append( (k[1], k[2], 3) )        
        r = getinfo(r_url + gurl(i[0]) + gurl(j[0]) + k[0])
        # 解析 4-街道/乡镇
        if r:
          # 某些地方可能这一级就直接到村了（例如海南-儋州市-那大镇-西干社区居委会)
          if len( ((k[0]).split('/')[-1]).split('.')[0] ) == 9:
            print('# 直接到村:', r_url + gurl(i[0]) + gurl(j[0]) + k[0])
            plist5 = re.findall('<td>(\d+?)</td>.+?d>(.+?)</td>.+?d>(.+?)</td>', r)              
            if not plist5: 
              print('# 5 Not found info in :', r_url + gurl(i[0]) + gurl(j[0]) + gurl(k[0]) + l[0])
              print(r)
            for m in plist5:
              city.append( (m[0],m[2],m[1]) )
          else:
            # 找寻类似 ID,  name这类没有下级链接的数据（例如：市辖区）
            plist0 = re.findall('<td>(\d+?)</td>.*?<td>(.+?)</td>', r)
            if plist0: print('# 4 Found <id><name> record', len(plist0))
            for z in plist0:
              city.append( (z[0], z[1], 4))
              # 找寻 下级数据 ref, ID, name           
            plist4 = re.findall('<a href="(.+?)">(.+?)</a></td>.+?d><a href=".+?">(.+?)</a>', r)
            if not plist4: print('# 4 Not found info in :', r_url + gurl(i[0]) + gurl(j[0]) + k[0])

            for l in plist4:
              city.append( (l[1], l[2], 4) )
              r = getinfo(r_url + gurl(i[0]) + gurl(j[0]) + gurl(k[0]) + l[0])
              # 解析 5-社区/村
              if r:
                plist5 = re.findall('<td>(\d+?)</td>.+?d>(.+?)</td>.+?d>(.+?)</td>', r)              
                if not plist5: 
                  print('# 5 Not found info in :', r_url + gurl(i[0]) + gurl(j[0]) + gurl(k[0]) + l[0])
                  print(r)
                for m in plist5:
                  city.append( (m[0],m[2],m[1]) )

  # 每个省 数据保存到 csv 文件
  with open('City.csv', 'ab') as f:
    for i in city:
      f.write( ('%s,%s,%s\n'%i).encode("UTF-8") )
