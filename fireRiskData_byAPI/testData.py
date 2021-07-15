import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic') #폰트바꾸기
plt.rcParams['axes.unicode_minus'] = False

jbDate = ['2021-07-13 23','2021-07-14 03','2021-07-14 06','2021-07-14 09','2021-07-14 12','2021-07-14 17', '2021-07-15 03', '2021-07-15 06', '2021-07-15 09', '2021-07-15 12', '2021-07-16 03', '2021-07-16 06', '2021-07-16 09', '2021-07-16 12']
jbRisk = [18.47,22.34,27.26,27.45,25.54,25.39, 21.05, 27.06, 27, 23.42, 18.56, 24, 24.04, 21.54]
jbTemperature = [28,26,26,29,31,31.0,25.0,25.0,29.0,31.0,25.0,25.0,28.0,31.0]

plt.plot(jbDate,jbRisk,label = '전라북도 화제위험도',c='r',marker='d')
plt.plot(jbDate,jbTemperature,label = '전라북도 기온',c='b',marker='d')

plt.legend()    
plt.show()    
