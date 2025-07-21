import dash
from dash import dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    # Cabeçalho bonito
    html.Div(
        style={
            'backgroundColor': '#2C3E50',
            'padding': '30px 0',
            'textAlign': 'center',
            'color': 'white',
            'borderRadius': '0 0 10px 10px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.2)'
        },
        children=html.H1("Formulário de Seleção - Dash", style={'margin': 0, 'fontSize': '32px'})
    ),

    # Conteúdo principal
    html.Div(
        style={
            'padding': '40px',
            'maxWidth': '600px',
            'margin': '30px auto',
            'backgroundColor': '#f9f9f9',
            'borderRadius': '10px',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.1)'
        },
        children=[
            html.Div([
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Rio Grande do Sul', 'value': 'NYC'},
                        {'label': 'São Paulo', 'value': 'SP'},
                        {'label': 'Santa Catarina', 'value': 'SC'}
                    ],
                    value='SP'
                )
            ], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Rio Grande do Sul', 'value': 'NYC'},
                        {'label': 'São Paulo', 'value': 'SP'},
                        {'label': 'Santa Catarina', 'value': 'SC'}
                    ],
                    value=['SP', 'SC'],
                    multi=True
                )
            ], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('Radio Items'),
                dcc.RadioItems(
                    options=[
                        {'label': 'Rio Grande do Sul', 'value': 'NYC'},
                        {'label': 'São Paulo', 'value': 'SP'},
                        {'label': 'Santa Catarina', 'value': 'SC'}
                    ],
                    value='SP'
                )
            ], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'Rio Grande do Sul', 'value': 'NYC'},
                        {'label': 'São Paulo', 'value': 'SP'},
                        {'label': 'Santa Catarina', 'value': 'SC'}
                    ],
                    value=['SP', 'SC']
                )
            ], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('Text Input'),
                dcc.Input(value='SP', type='text', style={'width': '100%', 'padding': '8px'})
            ], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
                    value=5,
                )
            ], style={'marginBottom': '20px'}),
        ]
    )
])

if __name__ == "__main__":
    app.run(debug=True)
