# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:49:35 2021

@author: Gebruiker
"""

#%% Getting all KM for INIT and all 

import requests

init_id = 1900696668
rorq_id = 28352
year = 2021
month = 9
month_text = 'september'

root_url = f'https://zkillboard.com/api'
year_modifier = f'/year/{year}'
month_modifier = f'/month/{month}/'
fetch_type_init = f'/kills'
fetch_type_all = f'/losses'
fetch_modifier_alliance = f'/allianceID/{init_id}'
fetch_modifier_ship = f'/shipTypeID/{rorq_id}'

request_url_init = root_url + fetch_type_init + fetch_modifier_alliance + fetch_modifier_ship + year_modifier + month_modifier
request_url_all = root_url + fetch_type_all + fetch_modifier_ship + year_modifier + month_modifier

r_init = requests.get(request_url_init)
r_all = requests.get(request_url_all)

init_json = r_init.json()
all_json = r_all.json()

print(f'This {month_text}, init killed {round((len(init_json) / len(all_json) ) * 100,0)}% of all dead rorquals in Eve.')

char_id = f'/characterID/2114500834/'

request_url_char = root_url + fetch_type_init + char_id

r_char = requests.get(request_url_char)

char_kill = len(r_char.json())


#%% Getting all Rorq Killed per month

import requests
import pandas as pd

rorq_id = 28352

df_year = pd.DataFrame({'year': range(2017,2022),'key': 0})
df_months = pd.DataFrame({'month': range(1,13),'key': 0})

l_year = []
l_month = []
l_kills = []

df_month_range = df_year.merge(df_months, how='outer').drop(columns=['key'])

root_url = f'https://zkillboard.com/api'
fetch_type_all = f'/losses'
fetch_modifier_ship = f'/shipTypeID/{rorq_id}'

for index, row in df_month_range.iterrows():
    year = row['year']
    month = row['month']
    year_modifier = f'/year/{year}'
    month_modifier = f'/month/{month}/'
    request_url_all = root_url + fetch_type_all + fetch_modifier_ship + year_modifier + month_modifier
    r_all_json = requests.get(request_url_all).json()
    l_year.append(year)
    l_month.append(month)
    l_kills.append(len(r_all_json))

df_results = pd.DataFrame()
df_results['year'] = l_year
df_results['month'] = l_month
df_results['kills'] = l_kills

