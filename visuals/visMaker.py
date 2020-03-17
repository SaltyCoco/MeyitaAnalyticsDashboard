import numpy as np
import pandas as pd
import plotly.express as px
import plotly.offline as plo
import plotly.graph_objects as go

def flu_sct_line():
    df_state = pd.read_csv('../data/cdc/State_Custom_Data.csv')
    df_state['SEASON'] = (df_state['SEASON'].str.split("-").str[0]).astype(int)
    df_state['SEASON'] = np.where(df_state['WEEK'] < 5, df_state['SEASON'], df_state['SEASON'] + 1)
    df_state['SEASON'] = df_state['SEASON'].astype(str)
    df_state['WEEK'] = df_state['WEEK'].astype(str)
    df_state.loc[df_state['WEEK'].str.contains("1"), 'WEEK'] = "01"
    df_state.loc[df_state['WEEK'].str.contains("2"), 'WEEK'] = "02"
    df_state.loc[df_state['WEEK'].str.contains("3"), 'WEEK'] = "03"
    df_state.loc[df_state['WEEK'].str.contains("4"), 'WEEK'] = "04"
    df_state['date_id'] = df_state['SEASON'] + df_state['WEEK']
    df_state = df_state[['date_id', 'state', 'SEASON', 'WEEK', 'NUM INFLUENZA DEATHS', 'NUM PNEUMONIA DEATHS', 'PERCENT P&I']]
    df_dates = pd.read_csv('../data/cdc/dateTable.csv')
    df_dates['date_id'] = df_dates['date_id'].astype(str)
    df_state_data = pd.merge(df_state, df_dates, on='date_id')

    df_state_data.to_csv('../data/etl/test.csv')

    df_nat = pd.read_csv('../data/cdc/National_Custom_Data.csv')
    df_nat_flu_test = pd.read_csv('../data/cdc/influenza_national_testing.csv')

    typeA = go.Scatter(
        x=df_nat_flu_test['WeekDate'],
        y=df_nat_flu_test['Total A'],
        name="Type A"
    )
    typeB = go.Scatter(
        x=df_nat_flu_test['WeekDate'],
        y=df_nat_flu_test['Total B'],
        name="Type B"
    )
    typeData = [typeA, typeB]
    typeLayout = go.Layout(
        title="Infection Counts Influenza type A & B 2019-2020 Nationally",
        #template='plotly_dark',
        paper_bgcolor="red",
        yaxis=dict(
            title="Number of People Infected"
        ),
        xaxis=dict(
            title="Date"
        )
    )
    fig = go.Figure(data=typeData, layout=typeLayout)
    #plo.plot(fig, filename='test.html')

def flu_map():
    df_map = pd.read_csv('../data/cdc/State_Custom_Data.csv')
    df_code = pd.read_csv('../data/cdc/state_data.csv')
    df_state_map = pd.merge(df_map, df_code, on='state')
    df_state_map = df_state_map[df_map["WEEK"]==52]
    df_state_map["flu_deaths"] = df_state_map["NUM PNEUMONIA DEATHS"] + df_map["NUM INFLUENZA DEATHS"]

    fig = go.Figure(data=go.Choropleth(
        locations=df_state_map["code"], # Spatial coordinates
        z = df_state_map["flu_deaths"], # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        #range_color=(0, 15000),
        # autocolorscale=True,
        colorbar_title = "Flu Related Deaths",
    ))
    fig.update_layout(
        title_text = '2019 Flu Related Deaths',
        geo_scope='usa', # limite map scope to USA
        #template="plotly_dark"
        paper_bgcolor="red",
    )

    fig.show()

    # fig = px.choropleth(df_state_map, locations="code", color="flu_deaths", locationmode="USA-states", color_continuous_scale=px.colors.sequential.Plasma, scope="usa")
    # fig.show()

def flu_nat_by_season():
    df_nat = pd.read_csv('../data/cdc/National_Custom_Data.csv')
    df_nat = df_nat[df_nat["WEEK"]==52]
