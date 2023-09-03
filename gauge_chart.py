import streamlit as st
import plotly.graph_objects as go

col = st.columns(3)
with col[1]:
    st.header('Parking Management System')
col = st.columns(3)
with col[0]:
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = 40,
        mode = "gauge+number+delta",
        title = {'text': "Parking Space-A"},
        delta = {'reference': 38},
        gauge = {'axis': {'range': [None, 50]},
                # 'steps' : [
                #     {'range': [0, 25], 'color': "lightgray"},
                #     {'range': [25, 40], 'color': "gray"},
                #     {'range': [45, 50], 'color': "lightblue"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 38}}))

    st.plotly_chart(fig, use_container_width=True)
with col[1]:
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = 26,
        mode = "gauge+number+delta",
        title = {'text': "Parking Space-B"},
        delta = {'reference': 38},
        gauge = {'axis': {'range': [None, 50]},
                # 'steps' : [
                #     {'range': [0, 25], 'color': "lightgray"},
                #     {'range': [25, 40], 'color': "gray"},
                #     {'range': [45, 50], 'color': "lightblue"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 38}}))

    st.plotly_chart(fig, use_container_width=True)
with col[2]:
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = 46,
        mode = "gauge+number+delta",
        title = {'text': "Parking Space-C"},
        delta = {'reference': 38},
        gauge = {'axis': {'range': [None, 50]},
                'steps' : [
                    {'range': [0, 25], 'color': "lightgray"},
                    {'range': [25, 40], 'color': "gray"},
                    {'range': [45, 50], 'color': "lightblue"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 38}}))

    st.plotly_chart(fig, use_container_width=True)
