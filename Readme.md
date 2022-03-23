# Data Resources

## City Data Resources (/City)

### World City Data
- **world_city_l3_xy.csv**
  - 209,579 city data, including: city ID, city name, continent/province, country, latitude and longitude coordinates

### Chinese cities and universities
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

