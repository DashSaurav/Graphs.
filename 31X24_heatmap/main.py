import streamlit as st
from PIL import Image
import create_heatmap, h_h_map
import datetime
st.set_page_config(page_title="Heatmap", layout="wide")

st.subheader("Roomwise Hourly Non-Compliances.")
c = st.columns(3)
with c[0]:
    val1 = st.number_input("Mention a threshold Value for Room M1", value=2)
with c[1]:
    val2 = st.number_input("Mention a threshold Value for Room M2", value=2)
with c[2]:
    data_value = st.date_input("Mention a Date",datetime.date(2022, 4, 18))

heat_map_data= create_heatmap.heat_map_func(data_value,int(val1),int(val2))
# heat_map_data= create_heatmap.heat_map_func("2022-04-20",3,4)
save_path = "dynamic_images"
image = h_h_map.create_dashboard_occ_heatmap(heat_map_data,save_path,cmap='Reds')
st.write(image)
