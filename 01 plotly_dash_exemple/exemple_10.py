import plotly.graph_objects as go
animais=['Girafas', 'Macacos', 'Tigres']

fig = go.Figure(data=[
    go.Bar(name='Zoo SP', x=animais, y=[20, 14, 23]),
    go.Bar(name='Zoo RS', x=animais, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()