# 数据资源

## 城市数据资源 (/City)

### 世界城市数据
- **world_city_l3_xy.csv**
  - 209,579个城市数据, 包含: 城市ID, 城市名, 洲/省, 国家, 经纬度坐标

### 中国城市 与 大学
- **cn_city_l5_2021.csv**
  - 中国 截止2021年10月31日 省-市-区/县-街道/乡/镇-社区/村 五级数据
  - 包括: 31省, 342市, 3343 区/县, 41278 街道/乡镇, 618133 社区/村
  - 包含: 编码, 名称, 类别
  - 更详细描述, 见: cn_city_l5_README.md 文档
- **cn_city_l5_2019.csv** 为 2019年10月31日 数据, 格式同上, 可用于分析城市变迁
- **cn_city_l5_2016.csv** 为 2016年07月31日 数据, 格式同上, 可用于分析城市变迁

- **cn_city_l2_xyp.csv**
  - 中国 330 个市 带经纬度, 人口 数据
  - 包含: 城市编码, 省+城市名, 城市名称, 人口数(万人), 经纬度

- **cn_city_l3_xy.csv**
  - 中国 3198 个市/县 带经纬度 数据
  - 包含: 城市编码, 名称, 经纬度

- **cn_University.csv**
  - 中国 2688 所大学数据
  - 包含: 学校代码, 学校名称, 主管部门, 所在城市, 办学层次(本科/专科), 类别(公办/民办), 层次(985/211/..)

### 美国城市
- **us_city_l3_xyp.csv**
  - 美国 3227 市县带经纬度, 人口数据
  - 包含: 城市编码, 城市名, 洲, 经纬度, 人口数


## 数据处理程序 （/Qscript)
- 请使用 [Qsqlite](https://github.com/wolf71/Qsqlite) 程序运行这些脚本 
- **qMap.txt** 使用城市数据, 绘制对应的地图, 运行后的页面见: [city_map.html](Qsqlite/city_map.html)
  - 将 qMap.txt 复制到 数据库文件/csv文件 同一个目录
  - 用 Qsqlite qMap.txt 运行, 而后检查生成的 city_map.html 文件
- **dP2021.txt** 对 cn_city_l5_2021.csv 数据进行加工, 增加一个 ptxt 地址前缀字段, 便于快速地址完整显示
  - 将 dP2021.txt 复制到 数据库文件/csv文件 同一个目录
  - 用 Qsqlite dP2021.txt 运行, 而后会自动生成一个 new_2021.csv 文件
- **qCity_cn.txt** 对 cn_city_l5_2021.csv 数据进行统计 和 比较 2019 年数据,生成 cn_city.html 报表
  - 将 qCity_cn.txt 复制到 数据库文件/csv文件 同一个目录
  - 用 Qsqlite qCity_cn.txt 运行, 而后会自动生成一个 cn_city.html 文件

## 数据抓取程序 (/App)
### 中国 2021 省-市-区/县-街道/乡/镇-社区/村 五级数据 抓取程序
- **getCity_2021.py**
  - 直接 python3 getCity_2021.py 运行即可



