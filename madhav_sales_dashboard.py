# Madhav E-Commerce Sales Dashboard

# Importing Libraries
import kagglehub
from kagglehub import KaggleDatasetAdapter

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import io
import base64
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, html, dcc, Input, Output

# Load `Orders` table
file_path = "Orders.csv"
Orders_df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "amitkumar209/madhav-e-commerce-sales-dataset",
    file_path
)

### Load `Details` table
file_path = "Details.csv"
Details_df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "amitkumar209/madhav-e-commerce-sales-dataset",
    file_path,
)

# Join orders with item details on Order ID
df = pd.merge(Orders_df, Details_df, on="Order ID")

# Parse order date for time-based analysis
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Extract month name for trend charts
df["Order Month"] = pd.to_datetime(df["Order Date"]).dt.strftime("%b")

# Extract quarter for seasonal grouping
df["Quater"] = pd.to_datetime(df["Order Date"]).dt.quarter

# Interactive Dashboard of Madhav Sales Analysis
app = Dash(__name__)

def kpi_figure(value, title, prefix=""):
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=value,
            title={"text": title, "font":{"size":14}},
            number={"prefix": prefix, "font": {"size": 28}},
            domain={"x": [0, 1], "y": [0, 1]}))
    
    fig.update_layout(
        height = 120,
        margin=dict(l=8, r=8, t=30, b=8),
        paper_bgcolor="white")
    
    return fig

app.layout = html.Div(children=[
    html.H1("Madhav E-Commerce Sales Dashboard",
            style={"textAlign":"center", "color":"#1D37CAD6"}),
    html.Br(),
    html.Div([
        "Category",
        dcc.Dropdown(id="input_category",
                     options = [{'label':'All', 'value':"all"},
                                {'label':'Clothing', 'value':"Clothing"},
                                {'label':'Electronics', 'value':"Electronics"},
                                {'label':'Furniture', 'value':"Furniture"}],
                     value = "all",
                     clearable = False,
                     style = {'textAlign':'center', 'height':'25px', 'width':'200px', 'margin':'0 auto'})
            ], style={'textAlign':'center', 'fontSize':20}),
    html.Br(),
    html.Div([
        "Quater: ",
        dcc.Dropdown(id = "input_quater",
                     options=[{'label':'Whole Year', 'value':'all'},
                              {'label':'Jan-Mar', 'value':1},
                              {'label':'Apr-Jun', 'value':2},
                              {'label':'Jul-Sep', 'value':3},
                              {'label':'Oct-Dec', 'value':4}],
                     value='all',
                     clearable=False,
                     style = {'height':'25px', 'width':'200px', 'margin':'0 auto', 'textAlign':'center'})
            ], style={'textAlign':'center', 'fontSize':20}),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Graph(id = 'total_revenue',
                  config = {'displayModeBar':False},
                  style = {'width':'24%', 'height':'130px'}),
        dcc.Graph(id = 'total_profit',
                  config = {'displayModeBar':False},
                  style = {'width':'24%', 'height':'130px'}),
        dcc.Graph(id = 'quantity_sold',
                  config = {'displayModeBar':False},
                  style = {'width':'24%', 'height':'130px'}),
        dcc.Graph(id = 'aov',
                  config = {'displayModeBar':False},
                  style = {'width':'24%', 'height':'130px'})
            ], style={'display':'flex', 'gap':'4px', "justifyContent": "space-between"}),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div(html.Img(id='monthly_profit'), style={'width':'50%'}),
        html.Div(dcc.Graph(id='sub_category_profit'), style={'width':'50%'})
            ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id='revenue_states'), style={'width':'50%'}),
        html.Div(dcc.Graph(id='category_quantity_sold'), style={'width':'50%'})
            ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id='payment_dist'), style={'width':'50%'}),
        html.Div(dcc.Graph(id='top_customers'), style={'width':'50%'})
            ], style={'display':'flex'})
], style={
    'backgroundColor':'white'
})

@app.callback([
    Output('total_revenue', 'figure'),
    Output('total_profit', 'figure'),
    Output('quantity_sold', 'figure'),
    Output('aov', 'figure'),
    Output('monthly_profit', 'src'),
    Output('sub_category_profit', 'figure'),
    Output('revenue_states', 'figure'),
    Output('category_quantity_sold', 'figure'),
    Output('payment_dist', 'figure'),
    Output('top_customers', 'figure')],
    Input('input_quater', 'value'),
    Input('input_category', 'value'))

def get_graph(quater, category):
    filtered_df = df.copy()
    
    if quater != 'all':
        filtered_df = filtered_df[filtered_df['Quater'] == quater]
    if category != 'all':
        filtered_df = filtered_df[filtered_df['Category'] == category]
        
    # Total revenue
    total_revenue = filtered_df['Amount'].sum()
    fig1 = kpi_figure(total_revenue, "Total Revenue", "₹")
    
    # Total Profit
    total_profit = filtered_df['Profit'].sum()
    fig2 = kpi_figure(total_profit, "Total Profit", "₹")
    
    # Quantity Sold
    quantity_sold = filtered_df['Quantity'].sum()
    fig3 = kpi_figure(quantity_sold, "Quantity Sold")
    
    # Average Order value
    aov = filtered_df['Amount'].sum() / filtered_df['Quantity'].sum()
    fig4 = kpi_figure(aov, "Average Order Value", "₹")
    
    # Monthly Profit
    df_month_profit = filtered_df.groupby("Order Month")['Profit'].sum().reset_index()
    df_month_profit['Month_No'] = pd.to_datetime(df_month_profit['Order Month'], format='%b').dt.month
    df_month_profit.sort_values('Month_No', inplace=True)
    df_month_profit.drop("Month_No", axis=1, inplace=True)

    plt.figure(figsize=(7.5, 5))
    sns.set_theme(style='ticks')

    bar_color = ["green" if profit >= 0 else "red" for profit in df_month_profit['Profit']]

    sns.barplot(data = df_month_profit,
                x = 'Order Month',
                y = "Profit",
                edgecolor = 'black',
                palette=bar_color)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f"₹{int(y/1000)}K"))

    plt.title("Profit by Month", fontsize=15)
    plt.ylabel("Profit")
    plt.xlabel("")
    sns.despine()
    
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    fig5 = f"data:image/png;base64,{encoded}"
    
    # Profit by Sub-category
    df_sub_category_profit = filtered_df.groupby(['Sub-Category'])['Profit'].sum().sort_values(ascending=False).head().reset_index()
    
    fig6 = px.bar(data_frame=df_sub_category_profit[::-1],
                 x = "Profit",
                 y = "Sub-Category",
                 template = "plotly_white")
    
    fig6.update_layout(title="Profit by Sub-Category",
                       title_x = 0.5,
                       xaxis_title = "",
                       yaxis_title = "")
    
    fig6.update_traces(marker = {'line':{'width':1, 'color':'black'}},
                       text = [f"₹{x:,}"  for x in df_sub_category_profit['Profit'][::-1]],
                       textposition = 'inside')
    
    fig6.update_xaxes(showticklabels = False)
    
    # Top Revenue States
    df_category_quantity = filtered_df.groupby('Category')['Quantity'].sum().reset_index()
    
    fig7 = px.pie(data_frame=df_category_quantity,
                  values = 'Quantity',
                  names = 'Category',
                  template = 'plotly_white')
    
    fig7.update_layout(title = "Quantity Sold by Category",
                       title_x = 0.5,
                       showlegend = True)
    
    # Quantity Sold by Category
    df_top_revenue_states = filtered_df.groupby('State')['Amount'].sum().sort_values(ascending=False).head().reset_index()
    df_top_revenue_states['Percent'] = df_top_revenue_states['Amount'] / df["Amount"].sum() * 100
    
    fig8 = px.bar(data_frame=df_top_revenue_states.iloc[::-1],
                  x = 'Percent',
                  y = 'State',
                  template = 'plotly_white')
    
    fig8.update_layout(title = "Top Revenue State",
                       title_x = 0.5,
                       xaxis_title = "",
                       yaxis_title = "")
    
    fig8.update_traces(marker = {'line':{'width':1, 'color':'black'}},
                       text = [f"{x:.1f}%" for x in df_top_revenue_states['Percent'][::-1]],
                       textposition = 'inside')
    
    fig8.update_xaxes(showticklabels = False)
    
    # Payment Mode Distribution
    df_payment_mode = df["PaymentMode"].value_counts().reset_index()
    
    fig9 = px.pie(data_frame=df_payment_mode,
                  values = 'count',
                  names = 'PaymentMode',
                  template = 'plotly_white')
    
    fig9.update_layout(title = "Payment Mode Distribution",
                       title_x = 0.5,
                       showlegend = True)
    
    # Top 5 Customers
    df_top_customers = filtered_df.groupby("CustomerName")['Amount'].sum().sort_values(ascending=False).head().reset_index()
    
    fig10 = px.bar(data_frame = df_top_customers,
                   x = 'CustomerName',
                   y = 'Amount',
                   template = "plotly_white")
    
    fig10.update_layout(title = "Top 5 Customers",
                        title_x = 0.5,
                        xaxis_title = "",
                        yaxis_title = "")
    
    fig10.update_traces(marker = {'line': {'width':1, 'color':'black'}},
                        text = [f"₹{x/1000:.1f}K" for x in df_top_customers['Amount']],
                        textposition = 'outside')
    
    fig10.update_yaxes(showticklabels = False)
    
    return [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10]

if __name__ == '__main__':
    app.run(debug=True)