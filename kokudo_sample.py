import pandas as pd
import xml.etree.ElementTree as ET

tree=ET.parse('S12-18.xml')
root=tree.getroot()

mylist=[]
ns={'place':'http://nlftp.mlit.go.jp/ksj/schemas/ksj-app'}

for i in root.findall('place:TheNumberofTheStationPassengersGettingonandoff',ns):
  station=i.find('place:stationName',ns).text
  passenger2011=i.find('place:passengers2011',ns).text
  passenger2012=i.find('place:passengers2012',ns).text
  passenger2013=i.find('place:passengers2013',ns).text
  passenger2014=i.find('place:passengers2014',ns).text
  passenger2015=i.find('place:passengers2015',ns).text
  passenger2016=i.find('place:passengers2016',ns).text
  passenger2017=i.find('place:passengers2017',ns).text
  
  sublist=[]
  sublist.extend([station , passenger2011 , passenger2012 , passenger2013 , passenger2014 , passenger2015 , passenger2016 , passenger2017])

  mylist.append(sublist)


features=["駅名" , "2011年" , "2012年" , "2013年" , "2014年" , "2015年" , "2016年" , "2017年"]


#データは一日の乗客人数
df=pd.DataFrame(mylist , columns=features)
df.index=df.index + 1
#print(df)

df.to_csv("kokudo_sample.csv" , encoding="shift-jis")

