import streamlit as st
import line_func
import datetime
st.set_page_config(layout="wide")

st.subheader("Occupancy Trend Chart")

c = st.columns(3)
with c[0]:
    date_value = st.date_input("Select a Date", datetime.date(2022, 4, 20))

deep_occ_daily = line_func.trend_line_func(date_value)
with c[1]:
    deep_occ_daily['M1 Threshold'] = st.number_input("Mention Threshold for M1 room", value = 2)
with c[2]:
    deep_occ_daily['M2 Threshold'] = st.number_input("Mention Threshold for M2 room", value = 3)
#st.dataframe(deep_occ_daily)
deep_occ_daily=deep_occ_daily.set_index('Time')
#st.write(deep_occ_daily)
                
st.line_chart(deep_occ_daily,use_container_width=True)

                