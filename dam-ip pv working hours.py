# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:43:32 2024

@author: Eleni
"""
"""
Libraries
"""
import pandas as pd
from datetime import datetime, timedelta
from sklearn import preprocessing
import numpy as np
from matplotlib import pyplot

"""
Import DAM data and bring them to the same format as IP
"""

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\working dam.xlsx"
dam = pd.read_excel(path)
dam["DELIVERY_MTU"] = pd.to_datetime(dam['DELIVERY_MTU'])
dam = dam.rename({"DELIVERY_MTU":'DateTime'},axis=1)
dam = dam.set_index('DateTime')
#Drop duplicates
dam = dam[~dam.index.duplicated()]

new_index = pd.date_range(start=dam.index.min(), end=dam.index.max(), freq='15T')
dam = dam.sort_index()
dam = dam.reindex(new_index, method='ffill')
for i in range(1, 4):
    new_index = dam.index[-1] + timedelta(minutes=15)
    dam.loc[new_index] = dam['MCP'].iloc[-1]
dam.sort_index(inplace=True)    
"""
Import IP data and concat them to a new dataframe
"""
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\ip2022-2024.xlsx"
ip = pd.read_excel(path)
ip = ip.rename({'UTC+1 at the end of the interval ':'DateTime'},axis=1)
ip['DateTime'] = pd.to_datetime(ip['DateTime'])
ip['DateTime']

# Initialize new column with the first datetime object
ip['new datetime'] = ip['DateTime'].iloc[0]

# Add 15 minutes to each subsequent row
for i in range(1, len(ip)):
    ip['new datetime'].iloc[i] = ip['new datetime'].iloc[i - 1] + timedelta(minutes=15)
ip.drop('DateTime', axis = 1, inplace = True)
ip = ip.rename({"new datetime":"DateTime"}, axis = 1)
ip = ip.set_index('DateTime')
ip = ip[~ip.index.duplicated()]
ip = ip.sort_index()


new = pd.DataFrame()
new['IP'] = ip['HENEX-Imbalance Price']
new = pd.concat([new, dam], axis = 1)
new.index = pd.to_datetime(new.index)

#new.tail()

#normalize the data in the new dataframe


#df_max_scaled = new.copy()
#Scale the data
for column in new.columns: 
    new[column] = new[column]  / new[column].abs().max() 
#df_max_scaled.head()      
new['hour'] = new.index.hour
new['month'] = new.index.month
new['year'] = new.index.year

new = new[new['year']>=2023]
new = new[new['year']<2024]
#Find NaN values in the dataframe
nan_df = new.isna()
print(nan_df)
"""
Add the remaining data for MCP and/or IP
"""
#Split into months to find seasonality that way
jan = new[new['month']==1]

feb = new[new['month']==2]

mar = new[new['month']==3]

apr = new[new['month']==4]

may = new[new['month']==5]

jun = new[new['month']==6]

jul = new[new['month']==7]

aug = new[new['month']==8]

sep = new[new['month']==9]

octo = new[new['month']==10]

nov = new[new['month']==11]

dec = new[new['month']==12]

#Keep only the PV workining hours
jan = jan[(jan['hour'] >= 8) & (jan['hour'] <= 17)]
feb = feb[(feb['hour'] >= 8) & (feb['hour'] <= 17)]
mar = mar[(mar['hour'] >= 8) & (mar['hour'] <= 18)]
apr = apr[(apr['hour'] >= 8) & (apr['hour'] <= 19)]
may = may[(may['hour'] >= 7) & (may['hour'] <= 19)]
jun = jun[(jun['hour'] >= 6) & (jun['hour'] <= 20)]
jul = jul[(jul['hour'] >= 6) & (jul['hour'] <= 20)]
aug = aug[(aug['hour'] >= 7) & (aug['hour'] <= 19)]
sep = sep[(sep['hour'] >= 8) & (sep['hour'] <= 19)]
octo = octo[(octo['hour'] >= 8) & (octo['hour'] <= 18)]
nov = nov[(nov['hour'] >= 8) & (nov['hour'] <= 17)]
dec = dec[(dec['hour'] >= 8) & (dec['hour'] <= 17)]

new1 = pd.DataFrame()
new1 = pd.concat([jan,feb,mar, apr, may, jun, jul, aug, sep, octo, nov, dec], axis = 0)

"""
df = pd.DataFrame()
df = pd.concat([jan, feb],axis = 0)
df = pd.concat([df,mar], axis = 0)
df = pd.concat([df,apr], axis = 0)
df = pd.concat([df,may], axis = 0)
df = pd.concat([df,jun], axis = 0)
df = pd.concat([df,jul], axis = 0)
df = pd.concat([df,aug], axis = 0)
df = pd.concat([df,sep], axis = 0)
df = pd.concat([df,octo], axis = 0)
df = pd.concat([df,nov], axis = 0)
df = pd.concat([df,dec], axis = 0)
df.info()
df = df.drop('hour', axis = 1)
df = df.drop('month', axis = 1)
"""
jan = jan[jan['year'] == 2023]
feb = feb[feb['year'] == 2023]
mar = mar[mar['year'] == 2023]
apr = apr[apr['year'] == 2023]
may = may[may['year'] == 2023]
jun = jun[jun['year'] == 2023]
jul = jul[jul['year'] == 2023]
aug = aug[aug['year'] == 2023]
sep = sep[sep['year'] == 2023]
octo = octo[octo['year'] == 2023]
nov = nov[nov['year'] == 2023]
dec = dec[dec['year'] == 2023]


jan[['IP','MCP']].plot()
pyplot.show()

feb[['IP','MCP']].plot()
pyplot.show()

mar[['IP','MCP']].plot()
pyplot.show()

apr[['IP','MCP']].plot()
pyplot.show()

may[['IP','MCP']].plot()
pyplot.show()

jun[['IP','MCP']].plot()
pyplot.show()

jul[['IP','MCP']].plot()
pyplot.show()

aug[['IP','MCP']].plot()
pyplot.show()

sep[['IP','MCP']].plot()
pyplot.show()

octo[['IP','MCP']].plot()
pyplot.show()

nov[['IP','MCP']].plot()
pyplot.show()

dec[['IP','MCP']].plot()
pyplot.show()

#Create a point system 
jan['IP POINT'] = 1 * (jan['IP'] < jan['MCP']) + 2 * (jan['IP'] > jan['MCP'])
feb['IP POINT'] = 1 * (feb['IP'] < feb['MCP']) + 2 * (feb['IP'] > feb['MCP'])
mar['IP POINT'] = 1 * (mar['IP'] < mar['MCP']) + 2 * (mar['IP'] > mar['MCP'])
apr['IP POINT'] = 1 * (apr['IP'] < apr['MCP']) + 2 * (apr['IP'] > apr['MCP'])
may['IP POINT'] = 1 * (may['IP'] < may['MCP']) + 2 * (may['IP'] > may['MCP'])
jun['IP POINT'] = 1 * (jun['IP'] < jun['MCP']) + 2 * (jun['IP'] > jun['MCP'])
jul['IP POINT'] = 1 * (jul['IP'] < jul['MCP']) + 2 * (jul['IP'] > jul['MCP'])
aug['IP POINT'] = 1 * (aug['IP'] < aug['MCP']) + 2 * (aug['IP'] > aug['MCP'])
sep['IP POINT'] = 1 * (sep['IP'] < sep['MCP']) + 2 * (sep['IP'] > sep['MCP'])
octo['IP POINT'] = 1 * (octo['IP'] < octo['MCP']) + 2 * (octo['IP'] > octo['MCP'])
nov['IP POINT'] = 1 * (nov['IP'] < nov['MCP']) + 2 * (nov['IP'] > nov['MCP'])
dec['IP POINT'] = 1 * (dec['IP'] < dec['MCP']) + 2 * (dec['IP'] > dec['MCP'])

jan['DAM POINT'] = 1 * (jan['IP'] > jan['MCP']) + 2 * (jan['IP'] < jan['MCP'])
feb['DAM POINT'] = 1 * (feb['IP'] > feb['MCP']) + 2 * (feb['IP'] < feb['MCP'])
mar['DAM POINT'] = 1 * (mar['IP'] > mar['MCP']) + 2 * (mar['IP'] < mar['MCP'])
apr['DAM POINT'] = 1 * (apr['IP'] > apr['MCP']) + 2 * (apr['IP'] < apr['MCP'])
may['DAM POINT'] = 1 * (may['IP'] > may['MCP']) + 2 * (may['IP'] < may['MCP'])
jun['DAM POINT'] = 1 * (jun['IP'] > jun['MCP']) + 2 * (jun['IP'] < jun['MCP'])
jul['DAM POINT'] = 1 * (jul['IP'] > jul['MCP']) + 2 * (jul['IP'] < jul['MCP'])
aug['DAM POINT'] = 1 * (aug['IP'] > aug['MCP']) + 2 * (aug['IP'] < aug['MCP'])
sep['DAM POINT'] = 1 * (sep['IP'] > sep['MCP']) + 2 * (sep['IP'] < sep['MCP'])
octo['DAM POINT'] = 1 * (octo['IP'] > octo['MCP']) + 2 * (octo['IP'] < octo['MCP'])
nov['DAM POINT'] = 1 * (nov['IP'] > nov['MCP']) + 2 * (nov['IP'] < nov['MCP'])
dec['DAM POINT'] = 1 * (dec['IP'] > dec['MCP']) + 2 * (dec['IP'] < dec['MCP'])

names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'octo', 'nov', 'dec']
lst = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
for df in lst:
    df.drop(['year', 'month'], axis = 1, inplace = True)
    
for df in lst:
    df['DAM - IP'] = df['MCP'] - df['IP']
    df['|DAM - IP|'] = df['DAM - IP'].abs()
    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\months ip dam pv hours.xlsx"


with pd.ExcelWriter(path) as writer:
    for df, sheet_name in zip(lst, names):
        df.to_excel(writer, sheet_name=sheet_name, index=True)
        
        
jan['DAM - IP'].plot() 
feb['DAM - IP'].plot()  
mar['DAM - IP'].plot()  
apr['DAM - IP'].plot()  
may['DAM - IP'].plot()  
jun['DAM - IP'].plot()  
jul['DAM - IP'].plot()  
aug['DAM - IP'].plot()  
sep['DAM - IP'].plot()  
octo['DAM - IP'].plot()  
nov['DAM - IP'].plot()  
dec['DAM - IP'].plot()  

       
import matplotlib.pyplot as plt
#Autocorellation lag=1

#from statsmodels.tsa.seasonal import STL
from statsmodels.graphics.tsaplots import plot_acf
# Autocorrelation plot
plt.figure(figsize=(10, 6))
plot_acf(jan['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Week Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Jan')
plt.show()    

plt.figure(figsize=(10, 6))
plot_acf(feb['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Feb')
plt.show()     

plt.figure(figsize=(10, 6))
plot_acf(mar['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Mar')
plt.show()     

plt.figure(figsize=(10, 6))
plot_acf(apr['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Apr')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(may['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot May')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(jun['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Jun')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(jul['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Jul')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(aug['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Aug')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(sep['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Sep')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(octo['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Octo')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(nov['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Nov')
plt.show() 

plt.figure(figsize=(10, 6))
plot_acf(dec['DAM - IP'], lags=1)  # Adjust the number of lags according to your data frequency
plt.xlabel('Day Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot Dec')
plt.show() 

#Check the whole dataset
plt.figure(figsize=(10, 6))
plot_acf(new['IP'], lags=7)  # Adjust the number of lags according to your data frequency
plt.xlabel('Week Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot IP')
plt.show()  

plt.figure(figsize=(10, 6))
plot_acf(new['MCP'], lags=30)  # Adjust the number of lags according to your data frequency
plt.xlabel('Month Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot DAM')
plt.show()

new['DAM - IP'] = new['MCP'] - new['IP']
plt.figure(figsize=(10, 6))
plot_acf(new['DAM - IP'], lags=7)  # Adjust the number of lags according to your data frequency
plt.xlabel('Week Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot DEV')
plt.show()
"""
Perform the same analysis as above, but for each hour of the day instead of each month
"""
new.info()
#Split into months to find seasonality that way
df0 = new[new['hour']==0]
df1 = new[new['hour']==1]
df2 = new[new['hour']==2]
df3 = new[new['hour']==3]
df4 = new[new['hour']==4]
df5 = new[new['hour']==5]
df6 = new[new['hour']==6]
df7 = new[new['hour']==7]
df8 = new[new['hour']==8]
df9 = new[new['hour']==9]
df10 = new[new['hour']==10]
df11 = new[new['hour']==11]
df12 = new[new['hour']==12]
df13 = new[new['hour']==13]
df14 = new[new['hour']==14]
df15 = new[new['hour']==15]
df16 = new[new['hour']==16]
df17 = new[new['hour']==17]
df18 = new[new['hour']==18]
df19 = new[new['hour']==19]
df20 = new[new['hour']==20]
df21 = new[new['hour']==21]
df22 = new[new['hour']==22]
df23 = new[new['hour']==23]


hours= [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23]

for df in hours:
    #df['DAM - IP'] = df['MCP'] - df['IP']
    plt.figure(figsize=(10, 6))
    plot_acf(df['MCP'], lags=7)  # Adjust the number of lags according to your data frequency
    plt.xlabel('Week Lag')
    plt.ylabel('Autocorrelation')
    plt.title('Autocorrelation Plot DAM')
    plt.show()

"""
The only possible autocorrelation and pattern is for data within a specific month for the PV working hours - we have data for the 2023 in this case
"""
#find pottential outliers
#from scipy import stats
from scipy.stats import zscore
score = jan.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = feb.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = mar.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = apr.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = may.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = jun.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = jul.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = jul.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = aug.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = sep.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = octo.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = nov.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

score = dec.apply(zscore, axis = 1)
score.head()
score['|DAM - IP|'].plot()

#we do not have outliers

"""
Apply DTW to find simmilar patterns between the months
That involves normalization in the preprosessing, outlier detection-we do not have any
#pip install dtw-python
from dtw import dtw

#resample time series to have the same frequency
#jan_resampled = jan.resample('1D').mean().interpolate()
#feb_resampled = feb.resample('1D').mean().interpolate()
#mar_resampled = mar.resample('1D').mean().interpolate()

# Compute DTW distance between each pair of time series
#distance_jan_feb, _ = dtw(jan['DAM - IP'], feb_resampled['DAM - IP'])
distance_jan_mar, _ = dtw(jan['DAM - IP'], mar['DAM - IP'])
#distance_feb_mar, _ = dtw(feb_resampled['DAM - IP'], mar_resampled['DAM - IP'])

#print("DTW distance between jan and feb:", distance_jan_feb)
print("DTW distance between jan and mar:", distance_jan_mar)
#print("DTW distance between feb and mar:", distance_feb_mar)




jan.info()
feb_resampled.info()
mar.info()
"""


"""
Detect seasonality using Seasonal Decomposition

Seasonal decomposition is a method used to separate a time series into its components, such as trend, seasonality, 
and residual (or noise).

Trend: This component represents the long-term progression of the time series. Think of the trend as the long-term path
your data is pursuing. If you imagine your data as a twisted road, the direction of the road is the trend. It helps you 
observe if the data is naturally decreasing, increasing, or holding steady and ignoring the short-term ups and downs. It is 
like comprehending the whole journey of the data.

Seasonal: The seasonal feature apprehends repeating patterns or seasonality within the time series. These patterns may occur 
at specified intervals, like daily, weekly, monthly, quarterly, or annually.

Residual: The residual element contains irregular or random fluctuations, not accounted for by the trend and seasonality. 
It depicts noise in your data.
"""
from statsmodels.tsa.seasonal import seasonal_decompose
# convert passenger column values to int
jan.info()
# perform seasonal decomposition
result = seasonal_decompose(jan['IP'], model='additive', period=1)

# plot the original data
plt.figure(figsize=(30, 8))
plt.subplot(411)
plt.plot(jan['IP'], label='Original')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot trend in data
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot seasonality in data
plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot residual components
plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# show plot
plt.tight_layout()
plt.show()


#try for the year 2023
new.info()
new['DAM - IP'] = new['MCP'] - new['IP']
result = seasonal_decompose(new['DAM - IP'], model='additive', period=92)

# plot the original data
plt.figure(figsize=(30, 8))
plt.subplot(411)
plt.plot(jan['DAM - IP'], label='Original')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot trend in data
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot seasonality in data
plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot residual components
plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# show plot
plt.tight_layout()
plt.show()


new1['DAM - IP'] = new1['MCP'] - new1['IP']
result = seasonal_decompose(new1['DAM - IP'], model='additive', period=2)

# plot the original data
plt.figure(figsize=(30, 8))
plt.subplot(411)
plt.plot(jan['DAM - IP'], label='Original')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot trend in data
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot seasonality in data
plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot residual components
plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# show plot
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plot_acf(dam['MCP'], lags=365)  # Adjust the number of lags according to your data frequency
plt.xlabel('week Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Plot 2023')
plt.show()   


result = seasonal_decompose(dam['MCP'], model='additive', period=92)

# plot the original data
plt.figure(figsize=(30, 8))
plt.subplot(411)
plt.plot(dam['MCP'], label='Original')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot trend in data
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot seasonality in data
plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# plot residual components
plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='best')
plt.xticks(rotation = 45)

# show plot
plt.tight_layout()
plt.show()

ip.info()
ip = ip.drop(['Unnamed: 2','ppc_i','PPCMA_{24 hours}','Unnamed: 5','Unnamed: 6','DATE', 'IP AVERAGE'],axis = 1)
ip['HENEX-Imbalance Price'] = ip['HENEX-Imbalance Price'].astype(float)
ip['IP'] = ip['HENEX-Imbalance Price']
ip['IP'].plot()
ip.info()




new1.info()
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\dam-ip.xlsx"
new1.to_excel(path, index = True)


#LSTM prediction
X = jan.values
train, test = X[0:-12], X[-12:]


history = [x for x in train]
predictions = list()
for i in range(len(test)):

