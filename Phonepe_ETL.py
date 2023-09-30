########## Import Libraries  #################

import requests
import subprocess
import pandas as pd
import os
import json
import sqlite3 as sq
import sqlalchemy
from sqlalchemy import create_engine

##------ Data processing----------#
#Aggregate data
path_1="E:/Capstone2/Phonepe_Data_Visualization/data/aggregated/transaction/country/india/state/"
Agg_trans_state_list=os.listdir(path_1)
Agg_trans={'State':[],'Year':[],'Quarter': [],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}

for i in Agg_trans_state_list:
    p_i=path_1+i+'/'
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+'/'
        Agg_yr_list=os.listdir(p_j)

        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            A=json.load(Data)

            for l in A['data']['transactionData']:
                Name = l['name']
                count = l['paymentInstruments'][0]['count']
                amount = l['paymentInstruments'][0]['amount']
                Agg_trans['State'].append(i)
                Agg_trans['Year'].append(j)
                Agg_trans['Quarter'].append(int(k.strip('.json')))
                Agg_trans['Transaction_type'].append(Name)
                Agg_trans['Transaction_count'].append(count)
                Agg_trans['Transaction_amount'].append(amount)
df_aggregated_transaction=pd.DataFrame(Agg_trans)


# AGGREGATED DATA -> USER

path_2 = "E:/Capstone2/Phonepe_Data_Visualization/data/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(path_2)

Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'User_Percentage': []}

for i in Agg_user_state_list:
    p_i = path_2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            B = json.load(Data)

            try:
                for l in B["data"]["usersByDevice"]:
                    brand_name = l["brand"]
                    count_ = l["count"]
                    ALL_percentage = l["percentage"]
                    Agg_user["State"].append(i)
                    Agg_user["Year"].append(j)
                    Agg_user["Quarter"].append(int(k.strip('.json')))
                    Agg_user["Brands"].append(brand_name)
                    Agg_user["User_Count"].append(count_)
                    Agg_user["User_Percentage"].append(ALL_percentage * 100)
            except:
                pass

df_aggregated_user = pd.DataFrame(Agg_user)

# MAP DATA --> TRANSACTION

path_3 = "E:/Capstone2/Phonepe_Data_Visualization/data/map/transaction/hover/country/india/state/"
map_trans_state_list = os.listdir(path_3)

map_trans = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_Count': [], 'Transaction_Amount': []}

for i in map_trans_state_list:
    p_i = path_3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            C = json.load(Data)

            for l in C["data"]["hoverDataList"]:
                District = l["name"]
                count = l["metric"][0]["count"]
                amount = l["metric"][0]["amount"]
                map_trans['State'].append(i)
                map_trans['Year'].append(j)
                map_trans['Quarter'].append(int(k.strip('.json')))
                map_trans["District"].append(District)
                map_trans["Transaction_Count"].append(count)
                map_trans["Transaction_Amount"].append(amount)

df_map_transaction = pd.DataFrame(map_trans)

# MAP DATA --> USER

path_4 = "E:/Capstone2/Phonepe_Data_Visualization/data/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(path_4)

map_user = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": []}

for i in map_user_state_list:
    p_i = path_4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for l in D["data"]["hoverData"].items():
                district = l[0]
                registereduser = l[1]["registeredUsers"]
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))
                map_user["District"].append(district)
                map_user["Registered_User"].append(registereduser)

df_map_user = pd.DataFrame(map_user)

# TOP DATA --> TRANSACTION

path_5 = "E:/Capstone2/Phonepe_Data_Visualization/data/top/transaction/country/india/state/"
top_trans_state_list = os.listdir(path_5)

top_trans = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [],
             'Transaction_amount': []}

for i in top_trans_state_list:
    p_i = path_5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            E = json.load(Data)

            for l in E['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                top_trans['State'].append(i)
                top_trans['Year'].append(j)
                top_trans['Quarter'].append(int(k.strip('.json')))
                top_trans['District_Pincode'].append(Name)
                top_trans['Transaction_count'].append(count)
                top_trans['Transaction_amount'].append(amount)

df_top_transaction = pd.DataFrame(top_trans)

# TOP DATA --> USER

path_6 = "E:/Capstone2/Phonepe_Data_Visualization/data/top/user/country/india/state/"
top_user_state_list = os.listdir(path_6)

top_user = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}

for i in top_user_state_list:
    p_i = path_6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            F = json.load(Data)

            for l in F['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))
                top_user['District_Pincode'].append(Name)
                top_user['Registered_User'].append(registeredUser)

df_top_user = pd.DataFrame(top_user)



#### Create SQL Engine

engine=create_engine('sqlite:///Phone_pay.db')
#sqlite3
mydb=sq.connect(database='Phone_pay.db')
my_cursor=mydb.cursor()


#creating tables
df_aggregated_transaction.to_sql(name='aggregated_transaction',con=engine,if_exists='append',index=False,schema=None)
df_aggregated_user.to_sql(name='aggregated_user',con=engine,if_exists='append',index=False,schema=None)
df_map_transaction.to_sql(name='map_transaction',con=engine,if_exists='append',index=False,schema=None)
df_map_user.to_sql(name='map_user',con=engine,if_exists='append',index=False,schema=None)
df_top_transaction.to_sql(name='top_transaction',con=engine,if_exists='append',index=False,schema=None)
df_top_user.to_sql(name='top_user',con=engine,if_exists='append',index=False,schema=None)

