# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:16:55 2024

@author: Eleni
"""

"""
for DAM prices
"""

import pandas as pd 

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\DAM 2023-2024 CET.xlsx"

df = pd.read_excel(path, sheet_name = "JAN23")
df.set_index('Unnamed: 0', inplace= True)
df.head()

new_df = pd.DataFrame()
# Step 1: Create a new DataFrame with columns for quarter-hour intervals.
new_columns = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)]
new_df = pd.DataFrame(index=df.index, columns=new_columns)

# Step 2: Populate the new DataFrame by duplicating the values from the old DataFrame.
for hour in range(24):
    for minute in range(0, 60, 15):
        new_df[f"{hour:02d}:{minute:02d}"] = df[hour].values

new_df.head()

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\DAM duplicated 2023-2024 CET.xlsx"

new_df.to_excel(path, index = True)
final = new_df


path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\DAM 2023-2024 CET.xlsx"

df = pd.read_excel(path, sheet_name = "AUG24")
df.set_index('Unnamed: 0', inplace= True)
df.head()


# Step 1: Create a new DataFrame with columns for quarter-hour intervals.
new_columns = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)]
new_df = pd.DataFrame(index=df.index, columns=new_columns)

# Step 2: Populate the new DataFrame by duplicating the values from the old DataFrame.
for hour in range(24):
    for minute in range(0, 60, 15):
        new_df[f"{hour:02d}:{minute:02d}"] = df[hour].values

final = pd.concat([final,new_df], axis = 0)

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\DAM duplicated 2023-2024 CET.xlsx"

final.to_excel(path, index = True)



"""
for net load and res production by IPTO
"""
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\RES 2023-2024 CET +1.xlsx"
df = pd.read_excel(path, sheet_name = 'JAN23')
df.set_index('Date', inplace = True)
df.head()
# Step 1: Create a new DataFrame with columns for quarter-hour intervals.
new_columns = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)]
new_df = pd.DataFrame(index=df.index, columns=new_columns)

# Step 2: Populate the new DataFrame by dividing each value by 4 and assigning it to the corresponding quarter-hour intervals.
for hour in range(24):
    value_per_quarter = df[hour].values / 4  # Divide the hourly value by 4
    for minute in range(0, 60, 15):
        new_df[f"{hour:02d}:{minute:02d}"] = value_per_quarter

# Display the new DataFrame
final = new_df
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\RES split 2023-2024 CET +1.xlsx"
final.to_excel(path, index = True)


path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\RES 2023-2024 CET +1.xlsx"
df = pd.read_excel(path, sheet_name = 'AUG24')
df.set_index('Date', inplace = True)
#df.head()
# Step 1: Create a new DataFrame with columns for quarter-hour intervals.
new_columns = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)]
new_df = pd.DataFrame(index=df.index, columns=new_columns)

# Step 2: Populate the new DataFrame by dividing each value by 4 and assigning it to the corresponding quarter-hour intervals.
for hour in range(24):
    value_per_quarter = df[hour].values / 4  # Divide the hourly value by 4
    for minute in range(0, 60, 15):
        new_df[f"{hour:02d}:{minute:02d}"] = value_per_quarter

# Display the new DataFrame
final = pd.concat([final, new_df], axis = 0 )
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\IP & DAM\IPTO DATA\RES split 2023-2024 CET +1.xlsx"

final.to_excel(path, index = True)
