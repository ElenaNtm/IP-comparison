# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:07:27 2023

@author: Eleni
Melt all the dataframes of hourly data into one
"""
"""
Libraries
"""
import pandas as pd

"""
Load data
"""
path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/hourly_gas.xlsx"
df_gas = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/hourly_res.xlsx"
df_res = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/hourly_hydro.xlsx"
df_hydro = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/hourly_lignite.xlsx"
df_lignite = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/hourly_load.xlsx"
df_load = pd.read_excel(path)
df_load.info()

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/dam_2020_2022.xlsx"
df_dam = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/lida1_2020_2022.xlsx"
df_lida1 = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/lida2_2020_2022.xlsx"
df_lida2 = pd.read_excel(path)

path = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data/lida3_2020_2022.xlsx"
df_lida3 = pd.read_excel(path)
"""
Melt the data to one column and then to a new dataframe
"""

#NET LOAD
melted_df = pd.melt(df_load, id_vars=['Unnamed: 0'], var_name='Hour', value_name='system load')
melted_df['Hour'] = pd.to_numeric(melted_df['Hour'])
melted_df['Unnamed: 0'] = melted_df['Unnamed: 0'].astype(str)
# Combine the 'Unnamed: 0' and 'Hour' columns to create a new 'datetime' column
melted_df['datetime'] = melted_df['Unnamed: 0'] + ' ' + melted_df['Hour'].astype(str).str.zfill(2) + ':00:00'
# Convert the 'datetime' column to datetime format with the correct format
melted_df['datetime'] = pd.to_datetime(melted_df['datetime'], format='%Y%m%d %H:%M:%S')
# Drop unnecessary columns
new_df = melted_df[['datetime', 'system load']]
# Set 'datetime' as the index
new_df.set_index('datetime', inplace=True)
# Sort the index if it's not sorted
new_df.sort_index(inplace=True)
#Overwrite the new dataframe on the old one to save space
df_load = new_df.copy()

#GAS
melted_df = pd.melt(df_gas, id_vars=['Unnamed: 0'], var_name='Hour', value_name='gas')
melted_df['Hour'] = pd.to_numeric(melted_df['Hour'])
melted_df['Unnamed: 0'] = melted_df['Unnamed: 0'].astype(str)
# Combine the 'Unnamed: 0' and 'Hour' columns to create a new 'datetime' column
melted_df['datetime'] = melted_df['Unnamed: 0'] + ' ' + melted_df['Hour'].astype(str).str.zfill(2) + ':00:00'
# Convert the 'datetime' column to datetime format with the correct format
melted_df['datetime'] = pd.to_datetime(melted_df['datetime'], format='%Y%m%d %H:%M:%S')
# Drop unnecessary columns
new_df = melted_df[['datetime', 'gas']]
# Set 'datetime' as the index
new_df.set_index('datetime', inplace=True)
# Sort the index if it's not sorted
new_df.sort_index(inplace=True)
#Overwrite the new dataframe on the old one to save space
df_gas = new_df.copy()
df_gas.head()
#RES
melted_df = pd.melt(df_res, id_vars=['Unnamed: 0'], var_name='Hour', value_name='res')
melted_df['Hour'] = pd.to_numeric(melted_df['Hour'])
melted_df['Unnamed: 0'] = melted_df['Unnamed: 0'].astype(str)
# Combine the 'Unnamed: 0' and 'Hour' columns to create a new 'datetime' column
melted_df['datetime'] = melted_df['Unnamed: 0'] + ' ' + melted_df['Hour'].astype(str).str.zfill(2) + ':00:00'
# Convert the 'datetime' column to datetime format with the correct format
melted_df['datetime'] = pd.to_datetime(melted_df['datetime'], format='%Y%m%d %H:%M:%S')
# Drop unnecessary columns
new_df = melted_df[['datetime', 'res']]
# Set 'datetime' as the index
new_df.set_index('datetime', inplace=True)
# Sort the index if it's not sorted
new_df.sort_index(inplace=True)
#Overwrite the new dataframe on the old one to save space
df_res = new_df.copy()
df_res.head()
#HYDRO
melted_df = pd.melt(df_hydro, id_vars=['Unnamed: 0'], var_name='Hour', value_name='hydro')
melted_df['Hour'] = pd.to_numeric(melted_df['Hour'])
melted_df['Unnamed: 0'] = melted_df['Unnamed: 0'].astype(str)
# Combine the 'Unnamed: 0' and 'Hour' columns to create a new 'datetime' column
melted_df['datetime'] = melted_df['Unnamed: 0'] + ' ' + melted_df['Hour'].astype(str).str.zfill(2) + ':00:00'
# Convert the 'datetime' column to datetime format with the correct format
melted_df['datetime'] = pd.to_datetime(melted_df['datetime'], format='%Y%m%d %H:%M:%S')
# Drop unnecessary columns
new_df = melted_df[['datetime', 'hydro']]
# Set 'datetime' as the index
new_df.set_index('datetime', inplace=True)
# Sort the index if it's not sorted
new_df.sort_index(inplace=True)
#Overwrite the new dataframe on the old one to save space
df_hydro = new_df.copy()
df_hydro.head()
#LIGNITE
melted_df = pd.melt(df_lignite, id_vars=['Unnamed: 0'], var_name='Hour', value_name='lignite')
melted_df['Hour'] = pd.to_numeric(melted_df['Hour'])
melted_df['Unnamed: 0'] = melted_df['Unnamed: 0'].astype(str)
# Combine the 'Unnamed: 0' and 'Hour' columns to create a new 'datetime' column
melted_df['datetime'] = melted_df['Unnamed: 0'] + ' ' + melted_df['Hour'].astype(str).str.zfill(2) + ':00:00'
# Convert the 'datetime' column to datetime format with the correct format
melted_df['datetime'] = pd.to_datetime(melted_df['datetime'], format='%Y%m%d %H:%M:%S')
# Drop unnecessary columns
new_df = melted_df[['datetime', 'lignite']]
# Set 'datetime' as the index
new_df.set_index('datetime', inplace=True)
# Sort the index if it's not sorted
new_df.sort_index(inplace=True)
#Overwrite the new dataframe on the old one to save space
df_lignite = new_df.copy()

"""
Merge all the dataframes into one
"""
result = pd.concat([df_gas, df_lignite], axis =1, join = 'inner')
result = pd.concat([result, df_res], axis =1, join = 'inner')
result = pd.concat([result, df_hydro], axis =1, join = 'inner')
result = pd.concat([result, df_load], axis =1, join = 'inner')

result.tail()


"""
Save again to an excel
"""
# Define the directory and filename
output_directory = "C:/Users/Eleni/OneDrive - Hellenic Association for Energy Economics (1)/ENPOWER/Market Prices Data/code and final outputs/output data"

output_filename = 'hourly_data.xlsx'  # Your specific filename
# Create the full file path
output_file_path = f"{output_directory}/{output_filename}"
result.to_excel(output_file_path, index=False)
