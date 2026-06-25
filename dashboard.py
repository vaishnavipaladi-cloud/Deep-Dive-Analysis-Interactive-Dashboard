import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_excel("Customer_sales_dataset_EDA.xlsx")
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
df['Month'] = df['Purchase_Date'].dt.to_period('M').astype(str)

app = dash.Dash(__name__)

# Pre-compute charts
cat_fig = px.bar(df.groupby('Category')['Total_Sales'].sum().reset_index(),
                 x='Category', y='Total_Sales', title='Revenue by Category', color='Category')

city_fig = px.bar(df.groupby('City')['Total_Sales'].sum().reset_index(),
                  x='City', y='Total_Sales', title='Revenue by City', color='City')

monthly = df.groupby('Month')['Total_Sales'].sum().reset_index()
trend_fig = px.line(monthly, x='Month', y='Total_Sales', title='Monthly Revenue Trend', markers=True)

gender_fig = px.pie(df, names='Gender', values='Total_Sales', title='Revenue by Gender')

scatter_fig = px.scatter(df, x='Quantity', y='Total_Sales', color='Category',
                         title='Quantity vs Total Sales', hover_data=['Product', 'City'])

# KPI values
total_rev = f"₹{df['Total_Sales'].sum():,.0f}"
aov = f"₹{df['Total_Sales'].mean():,.0f}"
top_city = df.groupby('City')['Total_Sales'].sum().idxmax()
top_cat = df.groupby('Category')['Total_Sales'].sum().idxmax()

app.layout = html.Div([
    html.H1("Customer Sales Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),

    # KPI Cards
    html.Div([
        html.Div([html.H3("Total Revenue"), html.H2(total_rev)], className='kpi-card',
                 style={'background':'#3498db','color':'white','padding':'20px','borderRadius':'10px','flex':'1','margin':'10px','textAlign':'center'}),
        html.Div([html.H3("Avg Order Value"), html.H2(aov)], className='kpi-card',
                 style={'background':'#2ecc71','color':'white','padding':'20px','borderRadius':'10px','flex':'1','margin':'10px','textAlign':'center'}),
        html.Div([html.H3("Top City"), html.H2(top_city)], className='kpi-card',
                 style={'background':'#e74c3c','color':'white','padding':'20px','borderRadius':'10px','flex':'1','margin':'10px','textAlign':'center'}),
        html.Div([html.H3("Top Category"), html.H2(top_cat)], className='kpi-card',
                 style={'background':'#9b59b6','color':'white','padding':'20px','borderRadius':'10px','flex':'1','margin':'10px','textAlign':'center'}),
    ], style={'display':'flex','flexWrap':'wrap','justifyContent':'center'}),

    # Charts Row 1
    html.Div([
        dcc.Graph(figure=cat_fig, style={'flex':'1'}),
        dcc.Graph(figure=city_fig, style={'flex':'1'}),
    ], style={'display':'flex'}),

    # Charts Row 2
    html.Div([
        dcc.Graph(figure=trend_fig, style={'flex':'2'}),
        dcc.Graph(figure=gender_fig, style={'flex':'1'}),
    ], style={'display':'flex'}),

    # Scatter
    dcc.Graph(figure=scatter_fig),
])

if __name__ == '__main__':
    app.run(debug=True)