import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import datetime as dt
import streamlit as st
from PIL import Image
# this set_page_config()--> always go first 
st.set_page_config(page_title="Heatmap", page_icon=":shark", layout="wide")


data = pd.read_csv("data_folder/processed_clean_df.csv")
pd.options.display.width = 0
#print(data)

def event_time_to_day(event_time):
   return dt.datetime.strptime(event_time, '%d-%m-%Y').day
   #return dt.datetime.strptime(event_time, '%Y-%m-%d').day
   
def event_time_to_month(event_time):
   return dt.datetime.strptime(event_time, '%d-%m-%Y').month
   #return dt.datetime.strptime(event_time, '%Y-%m-%d').month

def event_time_to_year(event_time):
   return dt.datetime.strptime(event_time, '%d-%m-%Y').year
   #return dt.datetime.strptime(event_time, '%Y-%m-%d').year

def event_time_to_hour(event_time):
   #return dt.datetime.strptime(event_time, '%H:%M:%S').hour
   return dt.datetime.strptime(event_time, '%H:%M:%S').hour


data['year'] = data['date'].apply(lambda event_datetime: event_time_to_year(event_datetime))
data['month'] = data['date'].apply(lambda event_datetime: event_time_to_month(event_datetime))
data['day'] = data['date'].apply(lambda event_datetime: event_time_to_day(event_datetime))
data['T_time'].replace(['0',''], '00:00:00', inplace=True)
data['Hour'] = data['T_time'].apply(lambda event_datetime: event_time_to_hour(event_datetime))

weekdays =['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

def calculate_weekday(day, month, year):
   return calendar.weekday(year, month, day)

data['weekday'] = data.apply(lambda row: calculate_weekday(year=row['year'], month=row['month'], day=row['day']), axis=1)

def create_full_chart(data):
   global p_heatmap
   p_heatmap = pd.pivot_table(data, values=['T_Occupancy'], index=['Hour'], columns=['weekday'], aggfunc='count')
   p_heatmap = p_heatmap.fillna(0)
   print(p_heatmap)
   median = np.median(p_heatmap)
   heatmap = sns.heatmap(p_heatmap, center=median, linewidths=.5, cbar=True, cmap="coolwarm")
   figure = heatmap.get_figure()
   plt.title("No of Occupants.")
   plt.xlabel("Weekday")
   plt.xticks(ticks=[num + .5 for num in range(7)], labels=weekdays)
   axes = figure.axes

   figure.savefig("new_map.png", bbox_inches="tight")
   #figure.show()

create_full_chart(data)

#..streamlit code..
st.subheader("Heatmap For the Occupancy on Each Days of Week.")
image = Image.open('new_map.png')
st.image(image, use_column_width=False)