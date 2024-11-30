import pandas as pd
import numpy as np
import joblib
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the trained model
model = joblib.load('model.pkl')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Sales Forecasting Dashboard"),
    
    html.Div([
        html.Label("Ad Spend:"),
        dcc.Input(id='input_ad_spend', type='number', value=10000),
        
        html.Label("Price:"),
        dcc.Input(id='input_price', type='number', value=200),
        
        html.Label("Month:"),
        dcc.Input(id='input_month', type='number', value=12),
        
        html.Label("Year:"),
        dcc.Input(id='input_year', type='number', value=2024),
        
        html.Label("Day of Week (0-6):"),
        dcc.Input(id='input_day_of_week', type='number', value=5),
    ]),
    
    html.Br(),
    
    html.Button('Predict Sales', id='predict_button', n_clicks=0),
    html.Hr(),
    
    html.Div(id='output_forecast')
])

# Define callback for prediction
@app.callback(
    Output('output_forecast', 'children'),
    Input('predict_button', 'n_clicks'),
    [Input('input_ad_spend', 'value'),
     Input('input_price', 'value'),
     Input('input_month', 'value'),
     Input('input_year', 'value'),
     Input('input_day_of_week', 'value')]
)
def predict_sales(n_clicks, ad_spend, price, month, year, day_of_week):
    if n_clicks > 0:
        input_data = pd.DataFrame({
            'Month': [month],
            'Year': [year],
            'Day_of_Week': [day_of_week],
            'Ad_Spend': [ad_spend],
            'Price': [price]
        })
        prediction = model.predict(input_data)[0]
        return f"Predicted Sales: {prediction:.2f}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
