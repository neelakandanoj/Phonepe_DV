# Phonepe_DV
Application link: https://phonepedv-jaaier3adeate9dqvfypn5.streamlit.app/


Phonepe Pulse Data Visualization
Introduction
PhonePe has become one of the most popular digital payment platforms in India, with millions of users relying on it for their day-to-day transactions. The app is known for its simplicity, user-friendly interface, and fast and secure payment processing. It has also won several awards and accolades for its innovative features and contributions to the digital payments industry.

We create a web app to analyse the Phonepe transaction and users depending on various Years, Quarters, States, and Types of transaction and give a Geographical and Geo visualization output based on given requirements.

" Disclaimer:-This data between 2018 to 2022 in INDIA only "
Intro GUI

Developer Guide
1. Tools install
virtual code.
Jupyter notebook.
Python 3.11.0 or higher.
MySQL
Git
2. Requirement Libraries to Install
pip install pandas numpy os json requests subprocess mysql.connector sqlalchemy pymysql streamlit plotly.express

4. Import Libraries
clone libraries

import requests
import subprocess
pandas, numpy and file handling libraries

import pandas as pd
import numpy as np
import os
import json
SQL libraries

import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
import pymysql
Dashboard libraries

import streamlit as st
import plotly.express as px

4. E T L Process
a) Extract data
Initially, we Clone the data from the Phonepe GitHub repository by using Python libraries. https://github.com/PhonePe/pulse.git
b) Process and Transform the data
Process the clone data by using Python algorithms and transform the processed data into DataFrame formate.
c) Load data
Finally, create a connection to the MySQL server and create a Database and stored the Transformed data in the MySQL server by using the given method. df.to_sql('table_name', connection, if_exists = 'replace', index = False, dtype={'Col_name':sqlalchemy.types.datatype()})

5. E D A Process and Frame work
a) Access MySQL DB
Create a connection to the MySQL server and access the specified MySQL DataBase by using pymysql library
b) Filter the data
Filter and process the collected data depending on the given requirements by using SQL queries
c) Visualization
Finally, create a Dashboard by using Streamlit and applying selection and dropdown options on the Dashboard and show the output are Geo visualization, bar chart, and Dataframe Table

User Guide
Step 1.
Select any one option fron All India or State wise or Top Ten categories.

Step 2.
Select any one option fron Transaction or User.

Step 3.
Select any Year, Quarter and additional required option.

Step 4.
Finally, You get the Geo Visualization Analysis or Bar chart Analysis and Table format Analysisks may be performed as necessary.
Database Integration: The transformed data is inserted into a MySQL database, offering efficient storage and retrieval capabilities.
Live Geo Visualization Dashboard: Python's Streamlit and Plotly libraries are utilized to create an interactive and visually appealing dashboard. This dashboard presents the data in real-time, enabling users to explore the insights effectively.
Database Integration with the Dashboard: The relevant data is fetched from the MySQL database and seamlessly integrated into the dashboard, ensuring the displayed information is up-to-date and accurate.
User-Selectable Dropdown Options: The dashboard incorporates a minimum of 10 distinct dropdown options, providing users with the ability to select and view various facts and figures of interest. This feature enhances the customization and flexibility of the dashboard.

