import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 4000,
    mode = "gauge+number+delta",
    title = {'text': "Free-Occupied Frequency"},
    delta = {'reference': 3800},
    gauge = {'axis': {'range': [None, 5000]},
             'steps' : [
                 {'range': [0, 2500], 'color': "lightgray"},
                 {'range': [2500, 4000], 'color': "gray"},
                 {'range': [4500, 4900], 'color': "lightblue"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 4900}}))

fig.show()