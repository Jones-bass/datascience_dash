import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]),
    hovertemplate="R$ %{y} - %{marker.size}",
    text=["item A", "item B", "item C", "item D"]
))

fig.show()