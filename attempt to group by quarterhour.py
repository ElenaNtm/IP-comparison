# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:17:39 2024

@author: Eleni

Data from existing excel files get aranged as date being the index and column being the quarterhour
Initially we make that for the difference between W+6 - W+1 to find the percentage difference 
(values between 0 and 1-depicted as a probablity)
On the second step we save in the same format IP prices for W+1 and W+6
"""

import pandas as pd
import numpy as np


path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP&DAM solar\PV working hours2024.xlsx"
jan = pd.read_excel(path, sheet_name = 'Jan')
jan['DateTime'] = pd.to_datetime(jan['DateTime'])
jan.drop(['DAM Prices (PTO)', 'CRIDA 1 results', 'CRIDA 2 results','CRIDA 3 results'], axis = 1, inplace = True)

jan['IP diff %'] = np.where(
    (jan['Imbalance Prices W+1'] == 0) & (jan['Imbalance Prices W+6'] == 0), 
    0,
    np.where(
        (jan['Imbalance Prices W+6'] == 0) & (jan['Imbalance Prices W+1'] != 0),
        jan['Imbalance Prices W+1'],
        (jan['Imbalance Prices W+6'] - jan['Imbalance Prices W+1']) / jan['Imbalance Prices W+6']
    )
)
jan.set_index('DateTime', inplace=True)

#melt the data to a new form
jan['date'] = jan.index.date
jan['time'] = jan.index.time

# Pivot the DataFrame
jan_pivot = jan.pivot(index='date', columns='time', values='IP diff %')
# Rename columns for readability if desired
jan_pivot.columns = [f"{col}" for col in jan_pivot.columns]
#jan_pivot.info()

feb = pd.read_excel(path, sheet_name = 'Feb')
feb['DateTime'] = pd.to_datetime(feb['DateTime'])
feb.drop(['DAM Prices (PTO)', 'CRIDA 1 results', 'CRIDA 2 results','CRIDA 3 results'], axis = 1, inplace = True)

feb['IP diff %'] = np.where(
    (feb['Imbalance Prices W+1'] == 0) & (feb['Imbalance Prices W+6'] == 0), 
    0,
    np.where(
        (feb['Imbalance Prices W+6'] == 0) & (feb['Imbalance Prices W+1'] != 0),
        feb['Imbalance Prices W+1'],
        (feb['Imbalance Prices W+6'] - feb['Imbalance Prices W+1']) / feb['Imbalance Prices W+6']
    )
)
feb.set_index('DateTime', inplace=True)

#melt the data to a new form
feb['date'] = feb.index.date
feb['time'] = feb.index.time

# Pivot the DataFrame
feb_pivot = feb.pivot(index='date', columns='time', values='IP diff %')
# Rename columns for readability if desired
feb_pivot.columns = [f"{col}" for col in feb_pivot.columns]

mar = pd.read_excel(path, sheet_name = 'Mar')
mar['DateTime'] = pd.to_datetime(mar['DateTime'])
mar.drop(['DAM Prices (PTO)', 'CRIDA 1 results', 'CRIDA 2 results','CRIDA 3 results'], axis = 1, inplace = True)

mar['IP diff %'] = np.where(
    (mar['Imbalance Prices W+1'] == 0) & (mar['Imbalance Prices W+6'] == 0), 
    0,
    np.where(
        (mar['Imbalance Prices W+6'] == 0) & (mar['Imbalance Prices W+1'] != 0),
        mar['Imbalance Prices W+1'],
        (mar['Imbalance Prices W+6'] - mar['Imbalance Prices W+1']) / mar['Imbalance Prices W+6']
    )
)
mar.set_index('DateTime', inplace=True)

#melt the data to a new form
mar['date'] = mar.index.date
mar['time'] = mar.index.time

# Pivot the DataFrame
mar_pivot = mar.pivot(index='date', columns='time', values='IP diff %')
# Rename columns for readability if desired
mar_pivot.columns = [f"{col}" for col in mar_pivot.columns]

apr = pd.read_excel(path, sheet_name = 'Apr')
apr['DateTime'] = pd.to_datetime(apr['DateTime'])
#apr.info()
apr.drop(['DAM results', 'CRIDA 1 results', 'CRIDA 2 results','CRIDA 3 results'], axis = 1, inplace = True)

apr['IP diff %'] = np.where(
    (apr['Imbalance Prices W+1'] == 0) & (apr['Imbalance Prices W+6'] == 0), 
    0,
    np.where(
        (apr['Imbalance Prices W+6'] == 0) & (apr['Imbalance Prices W+1'] != 0),
        apr['Imbalance Prices W+1'],
        (apr['Imbalance Prices W+6'] - apr['Imbalance Prices W+1']) / apr['Imbalance Prices W+6']
    )
)
apr.set_index('DateTime', inplace=True)

#melt the data to a new form
apr['date'] = apr.index.date
apr['time'] = apr.index.time

# Pivot the DataFrame
apr_pivot = apr.pivot(index='date', columns='time', values='IP diff %')
# Rename columns for readability if desired
apr_pivot.columns = [f"{col}" for col in apr_pivot.columns]

#When you will add data of market prices you will continue the same procedure

"""
Save the data to an excel file to different sheets
"""
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP&DAM solar\PV working hours2024 MELT IP.xlsx"
with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
    jan_pivot.to_excel(writer, sheet_name='Jan')
    feb_pivot.to_excel(writer, sheet_name='Feb')
    mar_pivot.to_excel(writer, sheet_name='Mar')
    apr_pivot.to_excel(writer, sheet_name='Apr')
    
    
"""
Do the same action, this time for IP W+1 and latter W+6
but for the full 24 hours-96 quarterhours
"""
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\Market Prices 2024.xlsx"
#Jan
df = pd.read_excel(path, sheet_name = 'Jan')    
df.info()
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
jan_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+1')
# Rename columns for readability if desired
jan_pivot.columns = [f"{col}" for col in jan_pivot.columns]

#Feb
df = pd.read_excel(path, sheet_name = 'Feb')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
feb_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+1')
# Rename columns for readability if desired
feb_pivot.columns = [f"{col}" for col in feb_pivot.columns]

#Mar
df = pd.read_excel(path, sheet_name = 'Mar')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
mar_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+1')
# Rename columns for readability if desired
mar_pivot.columns = [f"{col}" for col in mar_pivot.columns]

#Apr
df = pd.read_excel(path, sheet_name = 'Apr')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
apr_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+1')
# Rename columns for readability if desired
apr_pivot.columns = [f"{col}" for col in apr_pivot.columns]

#Add more months as data is collected
new_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\Market Prices 2024 IP W+1 MELT.xlsx"
with pd.ExcelWriter(new_path, engine='xlsxwriter') as writer:
    jan_pivot.to_excel(writer, sheet_name='Jan')
    feb_pivot.to_excel(writer, sheet_name='Feb')
    mar_pivot.to_excel(writer, sheet_name='Mar')
    apr_pivot.to_excel(writer, sheet_name='Apr')

#W+6
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\Market Prices 2024.xlsx"
#Jan
df = pd.read_excel(path, sheet_name = 'Jan')    
df.info()
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
jan_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+6')
# Rename columns for readability if desired
jan_pivot.columns = [f"{col}" for col in jan_pivot.columns]

#Feb
df = pd.read_excel(path, sheet_name = 'Feb')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
feb_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+6')
# Rename columns for readability if desired
feb_pivot.columns = [f"{col}" for col in feb_pivot.columns]

#Mar
df = pd.read_excel(path, sheet_name = 'Mar')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
mar_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+6')
# Rename columns for readability if desired
mar_pivot.columns = [f"{col}" for col in mar_pivot.columns]

#Apr
df = pd.read_excel(path, sheet_name = 'Apr')    
df['DateTime'] = pd.to_datetime(df['DateTime'], format = "%d/%m/%Y %H:%M")
df.set_index('DateTime', inplace = True)
#melt the data to a new form
df['date'] = df.index.date
df['time'] = df.index.time

# Pivot the DataFrame
apr_pivot = df.pivot(index='date', columns='time', values='Imbalance Prices W+6')
# Rename columns for readability if desired
apr_pivot.columns = [f"{col}" for col in apr_pivot.columns]

#Add more months as data is collected
new_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\Market Prices 2024 IP W+6 MELT.xlsx"
with pd.ExcelWriter(new_path, engine='xlsxwriter') as writer:
    jan_pivot.to_excel(writer, sheet_name='Jan')
    feb_pivot.to_excel(writer, sheet_name='Feb')
    mar_pivot.to_excel(writer, sheet_name='Mar')
    apr_pivot.to_excel(writer, sheet_name='Apr')
