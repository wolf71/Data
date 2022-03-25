# Data Resources

## City Data Resources (/City)

### World City Data
- **world_city_l3_xy.csv**
  - 209,579 city data, including: city ID, city name, continent/province, country, latitude and longitude coordinates
- **world_country_code.csv**
  - 245 countrys code info
  - Contains: chinese country name, english name, english fullname, 2-ID, 3-ID, IDnum

### Chinese cities and Enterprise / Universities
- **cn_city_l5_2021.csv**
  - China 2021/10/31 Province - City - County - Street - Community Five-level data
  - Includes: 31 provinces, 342 cities, 3343 districts/counties, 41278 streets/towns, 618133 communities/villages
  - Contains: Code, Name, Category
  - For a more detailed description, check: cn_city_l5_README.md
- **cn_city_l5_2019.csv** for 2019/10/31, same format as above, can be used to analyze change
- **cn_city_l5_2016.csv** for 2016/07/31, same format as above, can be used to analyze change

- **cn_city_l2_xyp.csv**
  - 330 cities in China with latitude and longitude, population data
  - Contains: city code, province + city name, city name, population (10K people), latitude and longitude

- **cn_city_l3_xy.csv**
  - 3198 cities/counties in China with latitude and longitude data
  - Contains: city code, name, latitude and longitude

- **cn_University.csv**
  - Data of 2688 universities in China
  - Contains: university code, university name, department, city, level(university/college), category(public/private), level(985/211/...)

- **cn_corp202012.csv**
  - China 4716 listed companies until 2022/3
  - Contains: stock code, stock name, company name, province, city, 2018 revenue, 2018 net profit, 2019 revenue, 2019 net profit, 2020 revenue, 2020 net profit, number of employees, date of listing, industry, product type, main business description

- **cn_corp_pettm.csv**
  - China Listed Companies 2018/12, 2019/12, 2020/12, 2021/12 Monthly Average Dynamic P/E (peTTM).
  - Including: Stock Code, 2018/12 Monthly Average peTTM, 2019/12 Monthly Average peTTM, 2020/12 Monthly Average peTTM, 2021/12 Monthly Average peTTM.


### U.S. cities
- **us_city_l3_xyp.csv**
  - United States 3227 cities and counties with latitude and longitude, population data
  - Contains: city code, city name, continent, latitude, longitude, population


## Data processing program (/Qscript)
- Please use the [Qsqlite](https://github.com/wolf71/Qsqlite) program to run these scripts 
- **qMap.txt** uses the city data and draws the citys map, generate html file: [city_map.html](Qscript/city_map.html)
  - Copy qMap.txt to the same directory as the database file/csv file
  - Run it with Qsqlite qMap.txt, and then check the generated city_map.html file
- **dP2021.txt** process the cn_city_l5_2021.csv data, add a ptxt address prefix field for quick and complete address display
  - Copy dP2021.txt to the same directory as the database file/csv file
  - Run with Qsqlite dP2021.txt, and a new_2021.csv file will be generated automatically
- **qCity_cn.txt** to count and compare the cn_city_l5_2021.csv data with the 2019 data to generate the cn_city.html report
  - Copy qCity_cn.txt to the same directory as the database file/csv file
  - Run with Qsqlite qCity_cn.txt, and a cn_city.html file will be generated automatically


## Data Crawler (/App)
### China 2021/10/31 Province - City - County - Street - Community Five-level data
- **getCity_2021.py**
  - run: python3 getCity_2021.py, the csv file will generated.
### China Listed Companies Data Crawl (/App/GetCorp)
- **getCorpInfo.py**
  - Open the program, modify the parameter, and then run it.
  - After the data crawl, clean and integrate the data as described in the comments.

