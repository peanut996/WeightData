# * coding=utf-8 *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime 

DataFrame=pd.read_csv('WeightData.csv')
DataFrame.columns=["Date","Weight"]
Date=DataFrame["Date"]
Weight=DataFrame["Weight"]
Date=np.array(Date)
Date=[datetime.strptime(i, '%Y.%m.%d') for i in Date]
Weight=np.array(Weight)
#A Figure
figure=plt.figure("Weight Data",figsize=(12,6))
plt.xlabel("Days")
plt.ylabel("Weight")
plt.title("Weight Data")
#plt.yticks([i for i in range(0,80,10)])
plt.plot(Date,Weight,marker=".",color="r",linestyle="-",linewidth=1.0,label="Weight")
plt.legend(loc='upper left')
figure.autofmt_xdate()
#plt.grid(color="k", linestyle=":")
plt.savefig("WeightData.png")
plt.show()