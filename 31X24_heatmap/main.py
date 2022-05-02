import streamlit as st
from PIL import Image
import create_heatmap, h_h_map
st.set_page_config(page_title="Heatmap", layout="wide")

st.subheader("Roomwise Hourly Non-Compliances.")
#heat_map_data= read_data.heat_map_func(str(currenttime.date()),saved_result,saved_result1)
heat_map_data= create_heatmap.heat_map_func("2022-04-20",3,4)
# heat_map_data = {"M1":[0,0,0,0,0,0,3,8,9,9,9,15,15,13,7,16,5,5,0,0,0,0,0,0],
#                 "M2":[0,0,0,0,0,3,5,8,7,10,10,15,15,14,19,2,2,2,0,0,0,0,0,0]}
save_path = "dynamic_images"
image = h_h_map.create_dashboard_occ_heatmap(heat_map_data,save_path,cmap='Reds')
st.write(image)