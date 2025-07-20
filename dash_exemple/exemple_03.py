import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, subplot_titles=("Gráfico de Barras", "Gráfico de Linhas"))

fig.add_trace(go.Bar(y=[2, 3, 5], marker_color="green"), row=1, col=1)

fig.add_trace(go.Scatter(y=[8, 3, 2, 4], mode="lines", line=dict(color="blue")), row=1, col=2)

fig.update_layout(title_text="Exemplo com Subplots", template="plotly_white")

fig.show()
