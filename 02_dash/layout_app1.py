import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#f5f7fa',
    'text': '#2c3e50',
    'header': '#2980b9',
    'card': '#ffffff',
    'graph_bg': '#ecf0f1'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['graph_bg'],
    paper_bgcolor=colors['card'],
    font_color=colors['text'],
    legend_bgcolor=colors['graph_bg'],
    legend_borderwidth=1
)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '30px'}, children=[
    html.Div([
        html.H1('Hello Dash', style={
            'textAlign': 'center',
            'color': colors['header'],
            'margin': '0',
            'padding': '0'
        }),
        html.H3('Dash: Um framework web para Python.', style={
            'textAlign': 'center',
            'color': colors['text'],
            'margin': '0',
            'padding': '0'
        }),
    ]),

    html.Div([
        dcc.Graph(id='example-graph-2', figure=fig)
    ], style={
        'backgroundColor': colors['card'],
        'borderRadius': '8px',
        'boxShadow': '0 8px 8px 0 rgba(0,0,0,0.1)',
        'margin': '0 auto'
    })
])

if __name__ == "__main__":
    app.run(debug=True)
