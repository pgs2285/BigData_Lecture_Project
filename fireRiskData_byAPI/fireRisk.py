from urllib import request
from urllib.parse import unquote
import requests
import xml.etree.ElementTree as elemTree
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy

localKeys = {
    11:"서울특별시",
    26:"부산광역시",
    27:"대구광역시",
    28:"인천광역시",
    29:"광주광역시",
    30:"대전광역시",
    31:"울산광역시",
    36:"세종특별자치시",
    41:"경기도",
    42:"강원도",
    43:"충청북도",
    44:"충청남도",
    45:"전라북도",
    46:"전라남도",
    47:"경상북도",
    48:"경상남도",
    50:"제주특별자치도"
}
url = 'http://know.nifos.go.kr/openapi/forestPoint/forestPointListSearch.do?'
serviceKey = 'gQ0Jw5e69TaJDIEIzPbEFDoiXYk9RQ2GkPYhMQuhxYI%3D' #api key
rc('font', family='AppleGothic') #폰트바꾸기
plt.rcParams['axes.unicode_minus'] = False
plt.ylim(0,100) # y값 범위 지정
plt.xlabel("날짜")
plt.ylabel("화제 위험도(%)")
for i in localKeys.keys():
    params=[('keyValue',unquote(serviceKey)), # api
    ('version', '1.1'),# 버전
    ('gubun', 'sido'), # 구분
    ('localArea', str(i)), # 지역 - dictionary에 저장되어 있음
    ('excludeForecast','0') # 예측 사용여부 0-사용 1-제외
    ]
    response = requests.get(url,params=params)

    status = response.status_code #응답코드
    result = response.text # xml내용
    tree = elemTree.fromstring(result) # 문자열 xml파싱
    baseRoot = tree.find('outputData').findall('items')
    
    date = [x.findtext('analdate') for x in baseRoot]
    fireRisk = [x.findtext('meanavg') for x in baseRoot]
    print(date, fireRisk)
    print(localKeys[i])
    floatRisk = []
    for j in fireRisk: # 정렬을 위해 float로 바꾸어줌
        floatRisk.append(float(j))
    plt.plot(date,floatRisk,label=localKeys[i],c=numpy.random.rand(3,),marker='d')

plt.legend()    
plt.show()    


#후에 해당 지역 산불을 미리 방지, 피해를 최소화 하는것과 연관을 지을수 있지 않을까... 이 데이터를 누적 쌓다보면 예측도 가능?