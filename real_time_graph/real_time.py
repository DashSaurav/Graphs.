import streamlit as st
import random
import pandas as pd
from csv import writer

from streamlit_autorefresh import st_autorefresh
# # update every 300 seconds [limited to 100 refreshes. add (limit=100) if required,]
st_autorefresh(interval=10000, limit=50000000)

Line_1 = random.randint(0,10)
Line_2 = random.randint(0,10)

list_data = [Line_1,Line_2]
with open('data.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(list_data)  
    f_object.close()

st.header("Real Time Graph")
df = pd.read_csv("data.csv")

col = st.columns(3)
with col[0]:
    st.metric(value=Line_1, label='Line 1 Value')
with col[2]:
    st.metric(value = Line_2, label='Line 2 Value')
def line_chart():  
    # fig = st.write(df)
    fig = st.line_chart(df, use_container_width=True)
line_chart()
        