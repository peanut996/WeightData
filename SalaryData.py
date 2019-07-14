# * coding=utf-8 *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime 

DataFrame=pd.read_csv('SalaryData.csv')
DataFrame.columns=["Date","GetMoney","Cost"]
Date=DataFrame["Date"]
GetMoney=DataFrame["GetMoney"]
Cost=DataFrame["Cost"]
Date=np.array(Date)
Date=[datetime.strptime(i, '%Y.%m.%d') for i in Date]
GetMoney=np.array(GetMoney)
Cost=np.array(Cost)
RealGain=[GetMoney[i]-Cost[i] for i in range(len(Date))]
#A Figure
figure=plt.figure("Salary Data",figsize=(12,6))
plt.xlabel("Days")
plt.ylabel("Money")
plt.title("Salary Data")
plt.yticks([i for i in range(00,180,10)])
plt.bar(Date,RealGain,color="c",linestyle="-",linewidth=1.0,label="RealGain")
plt.plot(Date,GetMoney,marker=".",color="k",linestyle="-",linewidth=1.0,label="GetMoney")
plt.plot(Date,Cost,marker=".",color="r",linestyle="-",linewidth=1.0,label="Cost")
plt.legend(loc='upper left')
figure.autofmt_xdate()
#plt.grid(color="k", linestyle=":")
plt.savefig("SalaryData.png")
plt.show()