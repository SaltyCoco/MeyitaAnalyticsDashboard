# app.py


import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

########################################################################################################################
########################################################################################################################
# Pharma Visuals
########################################################################################################################
########################################################################################################################
# Pharma Data
########################################################################################################################
df = pd.read_csv("data/main/mainDataFeeder.csv")
# net income
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# pct
df["pct_ni_rev_2010"] = (df["ni_2010"]/df["rev_2010"]) * 100
df["pct_ni_rev_2011"] = (df["ni_2011"]/df["rev_2011"]) * 100
df["pct_ni_rev_2012"] = (df["ni_2012"]/df["rev_2012"]) * 100
df["pct_ni_rev_2013"] = (df["ni_2013"]/df["rev_2013"]) * 100
df["pct_ni_rev_2014"] = (df["ni_2014"]/df["rev_2014"]) * 100
df["pct_ni_rev_2015"] = (df["ni_2015"]/df["rev_2015"]) * 100
df["pct_ni_rev_2016"] = (df["ni_2016"]/df["rev_2016"]) * 100
df["pct_ni_rev_2017"] = (df["ni_2017"]/df["rev_2017"]) * 100
df["pct_ni_rev_2018"] = (df["ni_2018"]/df["rev_2018"]) * 100
df["pct_ni_rev_2019"] = (df["ni_2019"]/df["rev_2019"]) * 100
#company dfs
df_jnj = df[df["symbol"]=="JNJ"]
df_pfe = df[df["symbol"]=="PFE"]
df_abbv = df[df["symbol"]=="ABBV"]
df_bmy = df[df["symbol"]=="BMY"]
df_tmo = df[df["symbol"]=="TMO"]
df_amgn = df[df["symbol"]=="AMGN"]
df_gild = df[df["symbol"]=="GILD"]
df_mrk = df[df["symbol"]=="MRK"]
########################################################################################################################
# Pharma Visuals
########################################################################################################################
def pharma_net_income():
    # net income
    jnj_ni = [df_jnj["ni_2010"].item(), df_jnj["ni_2011"].item(), df_jnj["ni_2012"].item(), df_jnj["ni_2013"].item(), df_jnj["ni_2014"].item(), df_jnj["ni_2015"].item(), df_jnj["ni_2016"].item(), df_jnj["ni_2017"].item(), df_jnj["ni_2018"].item(), df_jnj["ni_2019"].item()]
    pfe_ni = [df_pfe["ni_2010"].item(), df_pfe["ni_2011"].item(), df_pfe["ni_2012"].item(), df_pfe["ni_2013"].item(), df_pfe["ni_2014"].item(), df_pfe["ni_2015"].item(), df_pfe["ni_2016"].item(), df_pfe["ni_2017"].item(), df_pfe["ni_2018"].item(), df_pfe["ni_2019"].item()]
    abbv_ni = [df_abbv["ni_2010"].item(), df_abbv["ni_2011"].item(), df_abbv["ni_2012"].item(), df_abbv["ni_2013"].item(), df_abbv["ni_2014"].item(), df_abbv["ni_2015"].item(), df_abbv["ni_2016"].item(), df_abbv["ni_2017"].item(), df_abbv["ni_2018"].item(), df_abbv["ni_2019"].item()]
    bmy_ni = [df_bmy["ni_2010"].item(), df_bmy["ni_2011"].item(), df_bmy["ni_2012"].item(), df_bmy["ni_2013"].item(), df_bmy["ni_2014"].item(), df_bmy["ni_2015"].item(), df_bmy["ni_2016"].item(), df_bmy["ni_2017"].item(), df_bmy["ni_2018"].item(), df_bmy["ni_2019"].item()]
    tmo_ni = [df_tmo["ni_2010"].item(), df_tmo["ni_2011"].item(), df_tmo["ni_2012"].item(), df_tmo["ni_2013"].item(), df_tmo["ni_2014"].item(), df_tmo["ni_2015"].item(), df_tmo["ni_2016"].item(), df_tmo["ni_2017"].item(), df_tmo["ni_2018"].item(), df_tmo["ni_2019"].item()]
    amgn_ni = [df_amgn["ni_2010"].item(), df_amgn["ni_2011"].item(), df_amgn["ni_2012"].item(), df_amgn["ni_2013"].item(), df_amgn["ni_2014"].item(), df_amgn["ni_2015"].item(), df_amgn["ni_2016"].item(), df_amgn["ni_2017"].item(), df_amgn["ni_2018"].item(), df_amgn["ni_2019"].item()]
    gild_ni = [df_gild["ni_2010"].item(), df_gild["ni_2011"].item(), df_gild["ni_2012"].item(), df_gild["ni_2013"].item(), df_gild["ni_2014"].item(), df_gild["ni_2015"].item(), df_gild["ni_2016"].item(), df_gild["ni_2017"].item(), df_gild["ni_2018"].item(), df_gild["ni_2019"].item()]
    mrk_ni = [df_mrk["ni_2010"].item(), df_mrk["ni_2011"].item(), df_mrk["ni_2012"].item(), df_mrk["ni_2013"].item(), df_mrk["ni_2014"].item(), df_mrk["ni_2015"].item(), df_mrk["ni_2016"].item(), df_mrk["ni_2017"].item(), df_mrk["ni_2018"].item(), df_mrk["ni_2019"].item()]

    # Net Income
    jnj_net_income_trace = go.Scatter(
        x=years,
        y=jnj_ni,
        name="JNJ",
        mode='markers + lines',
        marker=dict(
            color='rgb(66, 245, 203)',
            size=15,
            line=dict(
                color='rgb(66, 75, 245)',
                width=2
            )
        )
    )
    pfe_net_income_trace = go.Scatter(
        x=years,
        y=pfe_ni,
        name="PFE",
        mode='markers + lines',
        marker=dict(
                color='rgb(239, 66, 245)',
                size=15,
                line=dict(
                    color='rgb(245, 66, 69)',
                    width=2
                )
            )
    )
    abbv_net_income_trace = go.Scatter(
        x=years,
        y=abbv_ni,
        name="ABBV",
        mode='markers + lines',
            marker=dict(
                color='rgb(250, 5, 5)',
                size=15,
                line=dict(
                    color='rgb(255,122,171)',
                    width=2
                )
            )
    )
    bmy_net_income_trace = go.Scatter(
        x=years,
        y=bmy_ni,
        name="BMY",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(229, 29, 49)',
                    width=2
                )
            )
    )
    tmo_net_income_trace = go.Scatter(
        x=years,
        y=tmo_ni,
        name="TMO",
        mode='markers + lines',
            marker=dict(
                color='rgb(14, 21, 211)',
                size=15,
                line=dict(
                    color='rgb(62, 242, 46)',
                    width=2
                )
            )
    )
    amgn_net_income_trace = go.Scatter(
        x=years,
        y=amgn_ni,
        name="AMGN",
        mode='markers + lines',
            marker=dict(
                color='rgb(227, 161, 234)',
                size=15,
                line=dict(
                    color='rgb(2, 83, 234)',
                    width=2
                )
            )
    )
    gild_net_income_trace = go.Scatter(
        x=years,
        y=gild_ni,
        name="GILD",
        mode='markers + lines',
            marker=dict(
                color='rgb(224, 229, 66)',
                size=15,
                line=dict(
                    color='rgb(110, 229, 66)',
                    width=2
                )
            )
    )
    mrk_net_income_trace = go.Scatter(
        x=years,
        y=mrk_ni,
        name="MRK",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(100, 183, 140)',
                    width=2
                )
            )
    )
    net_income_layout = go.Layout(
        title="Net Income by Year",
        template="plotly_dark",
        shapes=[
            dict(
                name="Obama",
                type="line",
                x0="2010",
                y0=25000000000,
                x1="2016",
                y1=25000000000,
                line=dict(
                    color="Blue",
                    width=10
                )
            ),
            dict(
                name="Trump",
                type="line",
                x0="2016",
                y0=25000000000,
                x1="2019",
                y1=25000000000,
                line=dict(
                    color="Red",
                    width=10
                )
            ),
        ]
    )
    net_income_data = [jnj_net_income_trace, pfe_net_income_trace, abbv_net_income_trace, bmy_net_income_trace, tmo_net_income_trace, amgn_net_income_trace, gild_net_income_trace, mrk_net_income_trace]
    net_income_fig = go.Figure(data=net_income_data, layout=net_income_layout)
    return net_income_fig

def pharma_revenue():
    # revenue
    jnj_rev = [df_jnj["rev_2010"].item(), df_jnj["rev_2011"].item(), df_jnj["rev_2012"].item(), df_jnj["rev_2013"].item(), df_jnj["rev_2014"].item(), df_jnj["rev_2015"].item(), df_jnj["rev_2016"].item(), df_jnj["rev_2017"].item(), df_jnj["rev_2018"].item(), df_jnj["rev_2019"].item()]
    pfe_rev = [df_pfe["rev_2010"].item(), df_pfe["rev_2011"].item(), df_pfe["rev_2012"].item(), df_pfe["rev_2013"].item(), df_pfe["rev_2014"].item(), df_pfe["rev_2015"].item(), df_pfe["rev_2016"].item(), df_pfe["rev_2017"].item(), df_pfe["rev_2018"].item(), df_pfe["rev_2019"].item()]
    abbv_rev = [df_abbv["rev_2010"].item(), df_abbv["rev_2011"].item(), df_abbv["rev_2012"].item(), df_abbv["rev_2013"].item(), df_abbv["rev_2014"].item(), df_abbv["rev_2015"].item(), df_abbv["rev_2016"].item(), df_abbv["rev_2017"].item(), df_abbv["rev_2018"].item(), df_abbv["rev_2019"].item()]
    bmy_rev = [df_bmy["rev_2010"].item(), df_bmy["rev_2011"].item(), df_bmy["rev_2012"].item(), df_bmy["rev_2013"].item(), df_bmy["rev_2014"].item(), df_bmy["rev_2015"].item(), df_bmy["rev_2016"].item(), df_bmy["rev_2017"].item(), df_bmy["rev_2018"].item(), df_bmy["rev_2019"].item()]
    tmo_rev = [df_tmo["rev_2010"].item(), df_tmo["rev_2011"].item(), df_tmo["rev_2012"].item(), df_tmo["rev_2013"].item(), df_tmo["rev_2014"].item(), df_tmo["rev_2015"].item(), df_tmo["rev_2016"].item(), df_tmo["rev_2017"].item(), df_tmo["rev_2018"].item(), df_tmo["rev_2019"].item()]
    amgn_rev = [df_amgn["rev_2010"].item(), df_amgn["rev_2011"].item(), df_amgn["rev_2012"].item(), df_amgn["rev_2013"].item(), df_amgn["rev_2014"].item(), df_amgn["rev_2015"].item(), df_amgn["rev_2016"].item(), df_amgn["rev_2017"].item(), df_amgn["rev_2018"].item(), df_amgn["rev_2019"].item()]
    gild_rev = [df_gild["rev_2010"].item(), df_gild["rev_2011"].item(), df_gild["rev_2012"].item(), df_gild["rev_2013"].item(), df_gild["rev_2014"].item(), df_gild["rev_2015"].item(), df_gild["rev_2016"].item(), df_gild["rev_2017"].item(), df_gild["rev_2018"].item(), df_gild["rev_2019"].item()]
    mrk_rev = [df_mrk["rev_2010"].item(), df_mrk["rev_2011"].item(), df_mrk["rev_2012"].item(), df_mrk["rev_2013"].item(), df_mrk["rev_2014"].item(), df_mrk["rev_2015"].item(), df_mrk["rev_2016"].item(), df_mrk["rev_2017"].item(), df_mrk["rev_2018"].item(), df_mrk["rev_2019"].item()]

    jnj_revenue_trace = go.Scatter(
        x=years,
        y=jnj_rev,
        name="JNJ",
        mode='markers + lines',
        marker=dict(
                color='rgb(66, 245, 203)',
                size=15,
                line=dict(
                    color='rgb(66, 75, 245)',
                    width=2
                )
            )
    )
    pfe_revenue_trace = go.Scatter(
        x=years,
        y=pfe_rev,
        name="PFE",
        mode='markers + lines',
        marker=dict(
                color='rgb(239, 66, 245)',
                size=15,
                line=dict(
                    color='rgb(245, 66, 69)',
                    width=2
                )
            )
    )
    abbv_revenue_trace = go.Scatter(
        x=years,
        y=abbv_rev,
        name="ABBV",
        mode='markers + lines',
            marker=dict(
                color='rgb(250, 5, 5)',
                size=15,
                line=dict(
                    color='rgb(255,122,171)',
                    width=2
                )
            )
    )
    bmy_revenue_trace = go.Scatter(
        x=years,
        y=bmy_rev,
        name="BMY",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(229, 29, 49)',
                    width=2
                )
            )
    )
    tmo_revenue_trace = go.Scatter(
        x=years,
        y=tmo_rev,
        name="TMO",
        mode='markers + lines',
            marker=dict(
                color='rgb(14, 21, 211)',
                size=15,
                line=dict(
                    color='rgb(62, 242, 46)',
                    width=2
                )
            )
    )
    amgn_revenue_trace = go.Scatter(
        x=years,
        y=amgn_rev,
        name="AMGN",
        mode='markers + lines',
            marker=dict(
                color='rgb(227, 161, 234)',
                size=15,
                line=dict(
                    color='rgb(2, 83, 234)',
                    width=2
                )
            )
    )
    gild_revenue_trace = go.Scatter(
        x=years,
        y=gild_rev,
        name="GILD",
        mode='markers + lines',
            marker=dict(
                color='rgb(224, 229, 66)',
                size=15,
                line=dict(
                    color='rgb(110, 229, 66)',
                    width=2
                )
            )
    )
    mrk_revenue_trace = go.Scatter(
        x=years,
        y=mrk_rev,
        name="MRK",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(100, 183, 140)',
                    width=2
                )
            )
    )
    rev_layout = go.Layout(
        title="Revenue by Year",
        template="plotly_dark",
        shapes=[
                dict(
                    name="Obama",
                    type="line",
                    x0="2010",
                    y0=90000000000,
                    x1="2016",
                    y1=90000000000,
                    line=dict(
                        color="Blue",
                        width=10
                    )
                ),
                dict(
                    name="Trump",
                    type="line",
                    x0="2016",
                    y0=90000000000,
                    x1="2019",
                    y1=90000000000,
                    line=dict(
                        color="Red",
                        width=10
                    )
                ),
        ]
    )
    rev_data = [jnj_revenue_trace, pfe_revenue_trace, abbv_revenue_trace, bmy_revenue_trace, tmo_revenue_trace, amgn_revenue_trace, gild_revenue_trace, mrk_revenue_trace]
    rev_fig = go.Figure(data=rev_data, layout=rev_layout)
    return rev_fig

def pharma_profit():
    # % profit
    jnj_pct = [df_jnj["pct_ni_rev_2010"].item(), df_jnj["pct_ni_rev_2011"].item(), df_jnj["pct_ni_rev_2012"].item(), df_jnj["pct_ni_rev_2013"].item(), df_jnj["pct_ni_rev_2014"].item(), df_jnj["pct_ni_rev_2015"].item(), df_jnj["pct_ni_rev_2016"].item(), df_jnj["pct_ni_rev_2017"].item(), df_jnj["pct_ni_rev_2018"].item(), df_jnj["pct_ni_rev_2019"].item()]
    pfe_pct = [df_pfe["pct_ni_rev_2010"].item(), df_pfe["pct_ni_rev_2011"].item(), df_pfe["pct_ni_rev_2012"].item(), df_pfe["pct_ni_rev_2013"].item(), df_pfe["pct_ni_rev_2014"].item(), df_pfe["pct_ni_rev_2015"].item(), df_pfe["pct_ni_rev_2016"].item(), df_pfe["pct_ni_rev_2017"].item(), df_pfe["pct_ni_rev_2018"].item(), df_pfe["pct_ni_rev_2019"].item()]
    abbv_pct = [df_abbv["pct_ni_rev_2010"].item(), df_abbv["pct_ni_rev_2011"].item(), df_abbv["pct_ni_rev_2012"].item(), df_abbv["pct_ni_rev_2013"].item(), df_abbv["pct_ni_rev_2014"].item(), df_abbv["pct_ni_rev_2015"].item(), df_abbv["pct_ni_rev_2016"].item(), df_abbv["pct_ni_rev_2017"].item(), df_abbv["pct_ni_rev_2018"].item(), df_abbv["pct_ni_rev_2019"].item()]
    bmy_pct = [df_bmy["pct_ni_rev_2010"].item(), df_bmy["pct_ni_rev_2011"].item(), df_bmy["pct_ni_rev_2012"].item(), df_bmy["pct_ni_rev_2013"].item(), df_bmy["pct_ni_rev_2014"].item(), df_bmy["pct_ni_rev_2015"].item(), df_bmy["pct_ni_rev_2016"].item(), df_bmy["pct_ni_rev_2017"].item(), df_bmy["pct_ni_rev_2018"].item(), df_bmy["pct_ni_rev_2019"].item()]
    tmo_pct = [df_tmo["pct_ni_rev_2010"].item(), df_tmo["pct_ni_rev_2011"].item(), df_tmo["pct_ni_rev_2012"].item(), df_tmo["pct_ni_rev_2013"].item(), df_tmo["pct_ni_rev_2014"].item(), df_tmo["pct_ni_rev_2015"].item(), df_tmo["pct_ni_rev_2016"].item(), df_tmo["pct_ni_rev_2017"].item(), df_tmo["pct_ni_rev_2018"].item(), df_tmo["pct_ni_rev_2019"].item()]
    amgn_pct = [df_amgn["pct_ni_rev_2010"].item(), df_amgn["pct_ni_rev_2011"].item(), df_amgn["pct_ni_rev_2012"].item(), df_amgn["pct_ni_rev_2013"].item(), df_amgn["pct_ni_rev_2014"].item(), df_amgn["pct_ni_rev_2015"].item(), df_amgn["pct_ni_rev_2016"].item(), df_amgn["pct_ni_rev_2017"].item(), df_amgn["pct_ni_rev_2018"].item(), df_amgn["pct_ni_rev_2019"].item()]
    gild_pct = [df_gild["pct_ni_rev_2010"].item(), df_gild["pct_ni_rev_2011"].item(), df_gild["pct_ni_rev_2012"].item(), df_gild["pct_ni_rev_2013"].item(), df_gild["pct_ni_rev_2014"].item(), df_gild["pct_ni_rev_2015"].item(), df_gild["pct_ni_rev_2016"].item(), df_gild["pct_ni_rev_2017"].item(), df_gild["pct_ni_rev_2018"].item(), df_gild["pct_ni_rev_2019"].item()]
    mrk_pct = [df_mrk["pct_ni_rev_2010"].item(), df_mrk["pct_ni_rev_2011"].item(), df_mrk["pct_ni_rev_2012"].item(), df_mrk["pct_ni_rev_2013"].item(), df_mrk["pct_ni_rev_2014"].item(), df_mrk["pct_ni_rev_2015"].item(), df_mrk["pct_ni_rev_2016"].item(), df_mrk["pct_ni_rev_2017"].item(), df_mrk["pct_ni_rev_2018"].item(), df_mrk["pct_ni_rev_2019"].item()]

    jnj_pct_trace = go.Scatter(
        x=years,
        y=jnj_pct,
        name="JNJ",
        mode='markers + lines',
        marker=dict(
                color='rgb(66, 245, 203)',
                size=15,
                line=dict(
                    color='rgb(66, 75, 245)',
                    width=2
                )
            )
    )
    pfe_pct_trace = go.Scatter(
        x=years,
        y=pfe_pct,
        name="PFE",
        mode='markers + lines',
        marker=dict(
                color='rgb(239, 66, 245)',
                size=15,
                line=dict(
                    color='rgb(245, 66, 69)',
                    width=2
                )
            )
    )
    abbv_pct_trace = go.Scatter(
        x=years,
        y=abbv_pct,
        name="ABBV",
        mode='markers + lines',
            marker=dict(
                color='rgb(250, 5, 5)',
                size=15,
                line=dict(
                    color='rgb(255,122,171)',
                    width=2
                )
            )
    )
    bmy_pct_trace = go.Scatter(
        x=years,
        y=bmy_pct,
        name="BMY",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(229, 29, 49)',
                    width=2
                )
            )
    )
    tmo_pct_trace = go.Scatter(
        x=years,
        y=tmo_pct,
        name="TMO",
        mode='markers + lines',
            marker=dict(
                color='rgb(14, 21, 211)',
                size=15,
                line=dict(
                    color='rgb(62, 242, 46)',
                    width=2
                )
            )
    )
    amgn_pct_trace = go.Scatter(
        x=years,
        y=amgn_pct,
        name="AMGN",
        mode='markers + lines',
            marker=dict(
                color='rgb(227, 161, 234)',
                size=15,
                line=dict(
                    color='rgb(2, 83, 234)',
                    width=2
                )
            )
    )
    gild_pct_trace = go.Scatter(
        x=years,
        y=gild_pct,
        name="GILD",
        mode='markers + lines',
            marker=dict(
                color='rgb(224, 229, 66)',
                size=15,
                line=dict(
                    color='rgb(110, 229, 66)',
                    width=2
                )
            )
    )
    mrk_pct_trace = go.Scatter(
        x=years,
        y=mrk_pct,
        name="MRK",
        mode='markers + lines',
            marker=dict(
                color='rgb(242, 183, 82)',
                size=15,
                line=dict(
                    color='rgb(100, 183, 140)',
                    width=2
                )
            )
    )
    pct_layout = go.Layout(
        title="% of Revenue as Income",
        template="plotly_dark",
        shapes=[
                dict(
                    name="Obama",
                    type="line",
                    x0="2010",
                    y0=60,
                    x1="2016",
                    y1=60,
                    line=dict(
                        color="Blue",
                        width=10
                    )
                ),
                dict(
                    name="Trump",
                    type="line",
                    x0="2016",
                    y0=60,
                    x1="2019",
                    y1=60,
                    line=dict(
                        color="Red",
                        width=10
                    )
                ),
        ]
    )
    pct_data = [jnj_pct_trace, pfe_pct_trace, abbv_pct_trace, bmy_pct_trace, tmo_pct_trace, amgn_pct_trace, gild_pct_trace, mrk_pct_trace]
    pct_fig = go.Figure(data=pct_data, layout=pct_layout)
    return pct_fig

def pharma_diff_in_rev():
    jnj_diff_ni_rev = [df_jnj["diff_ni_rev_2010"].item(), df_jnj["diff_ni_rev_2011"].item(),
                       df_jnj["diff_ni_rev_2012"].item(), df_jnj["diff_ni_rev_2013"].item(),
                       df_jnj["diff_ni_rev_2014"].item(), df_jnj["diff_ni_rev_2015"].item(),
                       df_jnj["diff_ni_rev_2016"].item(), df_jnj["diff_ni_rev_2017"].item(),
                       df_jnj["diff_ni_rev_2018"].item(), df_jnj["diff_ni_rev_2019"].item()]
    pfe_diff_ni_rev = [df_pfe["diff_ni_rev_2010"].item(), df_pfe["diff_ni_rev_2011"].item(),
                       df_pfe["diff_ni_rev_2012"].item(), df_pfe["diff_ni_rev_2013"].item(),
                       df_pfe["diff_ni_rev_2014"].item(), df_pfe["diff_ni_rev_2015"].item(),
                       df_pfe["diff_ni_rev_2016"].item(), df_pfe["diff_ni_rev_2017"].item(),
                       df_pfe["diff_ni_rev_2018"].item(), df_pfe["diff_ni_rev_2019"].item()]
    abbv_diff_ni_rev = [df_abbv["diff_ni_rev_2010"].item(), df_abbv["diff_ni_rev_2011"].item(),
                        df_abbv["diff_ni_rev_2012"].item(), df_abbv["diff_ni_rev_2013"].item(),
                        df_abbv["diff_ni_rev_2014"].item(), df_abbv["diff_ni_rev_2015"].item(),
                        df_abbv["diff_ni_rev_2016"].item(), df_abbv["diff_ni_rev_2017"].item(),
                        df_abbv["diff_ni_rev_2018"].item(), df_abbv["diff_ni_rev_2019"].item()]
    bmy_diff_ni_rev = [df_bmy["diff_ni_rev_2010"].item(), df_bmy["diff_ni_rev_2011"].item(),
                       df_bmy["diff_ni_rev_2012"].item(), df_bmy["diff_ni_rev_2013"].item(),
                       df_bmy["diff_ni_rev_2014"].item(), df_bmy["diff_ni_rev_2015"].item(),
                       df_bmy["diff_ni_rev_2016"].item(), df_bmy["diff_ni_rev_2017"].item(),
                       df_bmy["diff_ni_rev_2018"].item(), df_bmy["diff_ni_rev_2019"].item()]
    tmo_diff_ni_rev = [df_tmo["diff_ni_rev_2010"].item(), df_tmo["diff_ni_rev_2011"].item(),
                       df_tmo["diff_ni_rev_2012"].item(), df_tmo["diff_ni_rev_2013"].item(),
                       df_tmo["diff_ni_rev_2014"].item(), df_tmo["diff_ni_rev_2015"].item(),
                       df_tmo["diff_ni_rev_2016"].item(), df_tmo["diff_ni_rev_2017"].item(),
                       df_tmo["diff_ni_rev_2018"].item(), df_tmo["diff_ni_rev_2019"].item()]
    amgn_diff_ni_rev = [df_amgn["diff_ni_rev_2010"].item(), df_amgn["diff_ni_rev_2011"].item(),
                        df_amgn["diff_ni_rev_2012"].item(), df_amgn["diff_ni_rev_2013"].item(),
                        df_amgn["diff_ni_rev_2014"].item(), df_amgn["diff_ni_rev_2015"].item(),
                        df_amgn["diff_ni_rev_2016"].item(), df_amgn["diff_ni_rev_2017"].item(),
                        df_amgn["diff_ni_rev_2018"].item(), df_amgn["diff_ni_rev_2019"].item()]
    gild_diff_ni_rev = [df_gild["diff_ni_rev_2010"].item(), df_gild["diff_ni_rev_2011"].item(),
                        df_gild["diff_ni_rev_2012"].item(), df_gild["diff_ni_rev_2013"].item(),
                        df_gild["diff_ni_rev_2014"].item(), df_gild["diff_ni_rev_2015"].item(),
                        df_gild["diff_ni_rev_2016"].item(), df_gild["diff_ni_rev_2017"].item(),
                        df_gild["diff_ni_rev_2018"].item(), df_gild["diff_ni_rev_2019"].item()]
    mrk_diff_ni_rev = [df_mrk["diff_ni_rev_2010"].item(), df_mrk["diff_ni_rev_2011"].item(),
                       df_mrk["diff_ni_rev_2012"].item(), df_mrk["diff_ni_rev_2013"].item(),
                       df_mrk["diff_ni_rev_2014"].item(), df_mrk["diff_ni_rev_2015"].item(),
                       df_mrk["diff_ni_rev_2016"].item(), df_mrk["diff_ni_rev_2017"].item(),
                       df_mrk["diff_ni_rev_2018"].item(), df_mrk["diff_ni_rev_2019"].item()]

    jnj_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=jnj_diff_ni_rev,
        name="JNJ",
        mode='markers + lines',
        marker=dict(
            color='rgb(66, 245, 203)',
            size=15,
            line=dict(
                color='rgb(66, 75, 245)',
                width=2
            )
        )
    )
    pfe_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=pfe_diff_ni_rev,
        name="PFE",
        mode='markers + lines',
        marker=dict(
            color='rgb(239, 66, 245)',
            size=15,
            line=dict(
                color='rgb(245, 66, 69)',
                width=2
            )
        )
    )
    abbv_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=abbv_diff_ni_rev,
        name="ABBV",
        mode='markers + lines',
        marker=dict(
            color='rgb(250, 5, 5)',
            size=15,
            line=dict(
                color='rgb(255,122,171)',
                width=2
            )
        )
    )
    bmy_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=bmy_diff_ni_rev,
        name="BMY",
        mode='markers + lines',
        marker=dict(
            color='rgb(242, 183, 82)',
            size=15,
            line=dict(
                color='rgb(229, 29, 49)',
                width=2
            )
        )
    )
    tmo_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=tmo_diff_ni_rev,
        name="TMO",
        mode='markers + lines',
        marker=dict(
            color='rgb(14, 21, 211)',
            size=15,
            line=dict(
                color='rgb(62, 242, 46)',
                width=2
            )
        )
    )
    amgn_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=amgn_diff_ni_rev,
        name="AMGN",
        mode='markers + lines',
        marker=dict(
            color='rgb(227, 161, 234)',
            size=15,
            line=dict(
                color='rgb(2, 83, 234)',
                width=2
            )
        )
    )
    gild_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=gild_diff_ni_rev,
        name="GILD",
        mode='markers + lines',
        marker=dict(
            color='rgb(224, 229, 66)',
            size=15,
            line=dict(
                color='rgb(110, 229, 66)',
                width=2
            )
        )
    )
    mrk_diff_ni_rev_trace = go.Scatter(
        x=years,
        y=mrk_diff_ni_rev,
        name="MRK",
        mode='markers + lines',
        marker=dict(
            color='rgb(242, 183, 82)',
            size=15,
            line=dict(
                color='rgb(100, 183, 140)',
                width=2
            )
        )
    )
    diff_ni_rev_layout = go.Layout(
        title="Difference from Net Income to Revenue",
        template="plotly_dark",
        shapes=[
            dict(
                name="Obama",
                type="line",
                x0="2010",
                y0=83000000000,
                x1="2016",
                y1=83000000000,
                line=dict(
                    color="Blue",
                    width=10
                )
            ),
            dict(
                name="Trump",
                type="line",
                x0="2016",
                y0=83000000000,
                x1="2019",
                y1=83000000000,
                line=dict(
                    color="Red",
                    width=10
                )
            ),
        ]
    )
    diff_ni_rev_data = [jnj_diff_ni_rev_trace, pfe_diff_ni_rev_trace, abbv_diff_ni_rev_trace, bmy_diff_ni_rev_trace,
                        tmo_diff_ni_rev_trace, amgn_diff_ni_rev_trace, gild_diff_ni_rev_trace, mrk_diff_ni_rev_trace]
    diff_ni_rev_fig = go.Figure(data=diff_ni_rev_data, layout=diff_ni_rev_layout)
    return diff_ni_rev_fig

def pharma_approve_of_ceo():
    ave_cr_jnj = (df_jnj["gd_app_ceo"] + df_jnj["ind_app_ceo"]) / 2
    ave_cr_pfe = (df_pfe["gd_app_ceo"] + df_pfe["ind_app_ceo"]) / 2
    ave_cr_abbv = (df_abbv["gd_app_ceo"] + df_abbv["ind_app_ceo"]) / 2
    ave_cr_bmy = (df_bmy["gd_app_ceo"] + df_bmy["ind_app_ceo"]) / 2
    ave_cr_tmo = (df_tmo["gd_app_ceo"] + df_tmo["ind_app_ceo"]) / 2
    ave_cr_amgn = (df_amgn["gd_app_ceo"] + df_amgn["ind_app_ceo"]) / 2
    ave_cr_gild = (df_gild["gd_app_ceo"] + df_gild["ind_app_ceo"]) / 2
    ave_cr_mrk = (df_mrk["gd_app_ceo"] + df_mrk["ind_app_ceo"]) / 2
    # Net Income
    jnj_cr_trace = go.Bar(
        x=["JNJ"],
        y=ave_cr_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_cr_trace = go.Bar(
        x=["PFE"],
        y=ave_cr_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_cr_trace = go.Bar(
        x=["ABBV"],
        y=ave_cr_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_cr_trace = go.Bar(
        x=["BMY"],
        y=ave_cr_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_cr_trace = go.Bar(
        x=["TMO"],
        y=ave_cr_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_cr_trace = go.Bar(
        x=["AMGN"],
        y=ave_cr_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_cr_trace = go.Bar(
        x=["GILD"],
        y=ave_cr_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    cr_layout = go.Layout(
        title="Average Employee Approval Rating of Company CEO",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="% Approval",
            range=[0,100]
        )
    )
    cr_data = [jnj_cr_trace, pfe_cr_trace, abbv_cr_trace, bmy_cr_trace, tmo_cr_trace, amgn_cr_trace, gild_cr_trace]
    cr_fig = go.Figure(data=cr_data, layout=cr_layout)
    return cr_fig

def pharma_benefits_pay():
    ave_pb_jnj = (df_jnj["gd_benefits"] + df_jnj["ind_pay_ben"]) / 2
    ave_pb_pfe = (df_pfe["gd_benefits"] + df_pfe["ind_pay_ben"]) / 2
    ave_pb_abbv = (df_abbv["gd_benefits"] + df_abbv["ind_pay_ben"]) / 2
    ave_pb_bmy = (df_bmy["gd_benefits"] + df_bmy["ind_pay_ben"]) / 2
    ave_pb_tmo = (df_tmo["gd_benefits"] + df_tmo["ind_pay_ben"]) / 2
    ave_pb_amgn = (df_amgn["gd_benefits"] + df_amgn["ind_pay_ben"]) / 2
    ave_pb_gild = (df_gild["gd_benefits"] + df_gild["ind_pay_ben"]) / 2
    # Net Income
    jnj_pb_trace = go.Bar(
        x=["JNJ"],
        y=ave_pb_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_pb_trace = go.Bar(
        x=["PFE"],
        y=ave_pb_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_pb_trace = go.Bar(
        x=["ABBV"],
        y=ave_pb_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_pb_trace = go.Bar(
        x=["BMY"],
        y=ave_pb_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_pb_trace = go.Bar(
        x=["TMO"],
        y=ave_pb_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_pb_trace = go.Bar(
        x=["AMGN"],
        y=ave_pb_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_pb_trace = go.Bar(
        x=["GILD"],
        y=ave_pb_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    pb_layout = go.Layout(
        title="Average Employee Satisfaction for Pay & Benefits",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(title="% Approval")
    )
    pb_data = [jnj_pb_trace, pfe_pb_trace, abbv_pb_trace, bmy_pb_trace, tmo_pb_trace, amgn_pb_trace, gild_pb_trace]
    pb_fig = go.Figure(data=pb_data, layout=pb_layout)
    return pb_fig

def pharma_work_life():
    work_life_jnj = df_jnj["ind_work_life"]
    work_life_pfe = df_pfe["ind_work_life"]
    work_life_abbv = df_abbv["ind_work_life"]
    work_life_bmy = df_bmy["ind_work_life"]
    work_life_tmo = df_tmo["ind_work_life"]
    work_life_amgn = df_amgn["ind_work_life"]
    work_life_gild = df_gild["ind_work_life"]
    # Net Income
    jnj_work_life_trace = go.Bar(
        x=["JNJ"],
        y=work_life_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_work_life_trace = go.Bar(
        x=["PFE"],
        y=work_life_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_work_life_trace = go.Bar(
        x=["ABBV"],
        y=work_life_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_work_life_trace = go.Bar(
        x=["BMY"],
        y=work_life_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_work_life_trace = go.Bar(
        x=["TMO"],
        y=work_life_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_work_life_trace = go.Bar(
        x=["AMGN"],
        y=work_life_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_work_life_trace = go.Bar(
        x=["GILD"],
        y=work_life_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    work_life_layout = go.Layout(
        title="Likeliness to Recommed Company to a Friend",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="Out of 5 Employee Score",
            range=[0,5]
        )
    )
    work_life_data = [jnj_work_life_trace, pfe_work_life_trace, abbv_work_life_trace, bmy_work_life_trace, tmo_work_life_trace, amgn_work_life_trace, gild_work_life_trace]
    work_life_fig = go.Figure(data=work_life_data, layout=work_life_layout)
    return work_life_fig

def pharma_job_sec_adv():
    job_sec_adv_jnj = df_jnj["ind_job_sec_adv"]
    job_sec_adv_pfe = df_pfe["ind_job_sec_adv"]
    job_sec_adv_abbv = df_abbv["ind_job_sec_adv"]
    job_sec_adv_bmy = df_bmy["ind_job_sec_adv"]
    job_sec_adv_tmo = df_tmo["ind_job_sec_adv"]
    job_sec_adv_amgn = df_amgn["ind_job_sec_adv"]
    job_sec_adv_gild = df_gild["ind_job_sec_adv"]
    # Net Income
    jnj_job_sec_adv_trace = go.Bar(
        x=["JNJ"],
        y=job_sec_adv_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_job_sec_adv_trace = go.Bar(
        x=["PFE"],
        y=job_sec_adv_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_job_sec_adv_trace = go.Bar(
        x=["ABBV"],
        y=job_sec_adv_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_job_sec_adv_trace = go.Bar(
        x=["BMY"],
        y=job_sec_adv_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_job_sec_adv_trace = go.Bar(
        x=["TMO"],
        y=job_sec_adv_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_job_sec_adv_trace = go.Bar(
        x=["AMGN"],
        y=job_sec_adv_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_job_sec_adv_trace = go.Bar(
        x=["GILD"],
        y=job_sec_adv_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    job_sec_adv_layout = go.Layout(
        title="Work Life Balance",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="Out of 5 Employee Score",
            range=[0,5]
        )
    )
    job_sec_adv_data = [jnj_job_sec_adv_trace, pfe_job_sec_adv_trace, abbv_job_sec_adv_trace, bmy_job_sec_adv_trace, tmo_job_sec_adv_trace, amgn_job_sec_adv_trace, gild_job_sec_adv_trace]
    job_sec_adv_fig = go.Figure(data=job_sec_adv_data, layout=job_sec_adv_layout)
    return job_sec_adv_fig

def pharma_mgnt():
    mgnt_jnj = df_jnj["ind_mgnt"]
    mgnt_pfe = df_pfe["ind_mgnt"]
    mgnt_abbv = df_abbv["ind_mgnt"]
    mgnt_bmy = df_bmy["ind_mgnt"]
    mgnt_tmo = df_tmo["ind_mgnt"]
    mgnt_amgn = df_amgn["ind_mgnt"]
    mgnt_gild = df_gild["ind_mgnt"]
    # Net Income
    jnj_mgnt_trace = go.Bar(
        x=["JNJ"],
        y=mgnt_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_mgnt_trace = go.Bar(
        x=["PFE"],
        y=mgnt_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_mgnt_trace = go.Bar(
        x=["ABBV"],
        y=mgnt_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_mgnt_trace = go.Bar(
        x=["BMY"],
        y=mgnt_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_mgnt_trace = go.Bar(
        x=["TMO"],
        y=mgnt_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_mgnt_trace = go.Bar(
        x=["AMGN"],
        y=mgnt_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_mgnt_trace = go.Bar(
        x=["GILD"],
        y=mgnt_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    mgnt_layout = go.Layout(
        title="Employee Management Satisfaction",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="Employee Score Out of 5",
            range=[0,5]
        )
    )
    mgnt_data = [jnj_mgnt_trace, pfe_mgnt_trace, abbv_mgnt_trace, bmy_mgnt_trace, tmo_mgnt_trace, amgn_mgnt_trace, gild_mgnt_trace]
    mgnt_fig = go.Figure(data=mgnt_data, layout=mgnt_layout)
    return mgnt_fig

def pharma_culture():
    ind_culture_jnj = df_jnj["ind_culture"]
    ind_culture_pfe = df_pfe["ind_culture"]
    ind_culture_abbv = df_abbv["ind_culture"]
    ind_culture_bmy = df_bmy["ind_culture"]
    ind_culture_tmo = df_tmo["ind_culture"]
    ind_culture_amgn = df_amgn["ind_culture"]
    ind_culture_gild = df_gild["ind_culture"]
    # Net Income
    jnj_ind_culture_trace = go.Bar(
        x=["JNJ"],
        y=ind_culture_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_ind_culture_trace = go.Bar(
        x=["PFE"],
        y=ind_culture_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_ind_culture_trace = go.Bar(
        x=["ABBV"],
        y=ind_culture_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_ind_culture_trace = go.Bar(
        x=["BMY"],
        y=ind_culture_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_ind_culture_trace = go.Bar(
        x=["TMO"],
        y=ind_culture_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_ind_culture_trace = go.Bar(
        x=["AMGN"],
        y=ind_culture_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_ind_culture_trace = go.Bar(
        x=["GILD"],
        y=ind_culture_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    ind_culture_layout = go.Layout(
        title="Employee Management Satisfaction",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="Employee Score Out of 5",
            range=[0,5]
        )
    )
    ind_culture_data = [jnj_ind_culture_trace, pfe_ind_culture_trace, abbv_ind_culture_trace, bmy_ind_culture_trace, tmo_ind_culture_trace, amgn_ind_culture_trace, gild_ind_culture_trace]
    ind_culture_fig = go.Figure(data=ind_culture_data, layout=ind_culture_layout)
    return ind_culture_fig

def pharma_salary_sat():
    ind_salary_sat_jnj = df_jnj["ind_salary_sat"]
    ind_salary_sat_pfe = df_pfe["ind_salary_sat"]
    ind_salary_sat_abbv = df_abbv["ind_salary_sat"]
    ind_salary_sat_bmy = df_bmy["ind_salary_sat"]
    ind_salary_sat_tmo = df_tmo["ind_salary_sat"]
    ind_salary_sat_amgn = df_amgn["ind_salary_sat"]
    ind_salary_sat_gild = df_gild["ind_salary_sat"]
    # Net Income
    jnj_ind_salary_sat_trace = go.Bar(
        x=["JNJ"],
        y=ind_salary_sat_jnj,
        name="JNJ",
        marker=dict(
            color='rgb(66, 245, 203)')
    )
    pfe_ind_salary_sat_trace = go.Bar(
        x=["PFE"],
        y=ind_salary_sat_pfe,
        name="PFE",
        marker=dict(
                color='rgb(239, 66, 245)',
            )
    )
    abbv_ind_salary_sat_trace = go.Bar(
        x=["ABBV"],
        y=ind_salary_sat_abbv,
        name="ABBV",
        marker=dict(
            color='rgb(250, 5, 5)',
            )
    )
    bmy_ind_salary_sat_trace = go.Bar(
        x=["BMY"],
        y=ind_salary_sat_bmy,
        name="BMY",
        marker=dict(
            color='rgb(242, 183, 82)',
            )
    )
    tmo_ind_salary_sat_trace = go.Bar(
        x=["TMO"],
        y=ind_salary_sat_tmo,
        name="TMO",
        marker=dict(
            color='rgb(14, 21, 211)',
            )
    )
    amgn_ind_salary_sat_trace = go.Bar(
        x=["AMGN"],
        y=ind_salary_sat_amgn,
        name="AMGN",
        marker=dict(
            color='rgb(227, 161, 234)',
            )
    )
    gild_ind_salary_sat_trace = go.Bar(
        x=["GILD"],
        y=ind_salary_sat_gild,
        name="GILD",
        marker=dict(
            color='rgb(224, 229, 66)',
        )
    )
    ind_salary_sat_layout = go.Layout(
        title="Employee Salary Satisfaction",
        template="plotly_dark",
        xaxis=dict(title="Company"),
        yaxis=dict(
            title="Employee Score Out of 5",
            range=[0,5]
        )
    )
    ind_salary_sat_data = [jnj_ind_salary_sat_trace, pfe_ind_salary_sat_trace, abbv_ind_salary_sat_trace, bmy_ind_salary_sat_trace, tmo_ind_salary_sat_trace, amgn_ind_salary_sat_trace, gild_ind_salary_sat_trace]
    ind_salary_sat_fig = go.Figure(data=ind_salary_sat_data, layout=ind_salary_sat_layout)
    return ind_salary_sat_fig
########################################################################################################################
# Navbar
########################################################################################################################
navbar = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Meyita Analytics", className="ml-2"))
                ],
                align="left"
            )
        )
    ],
    color="dark",
    dark=True,
)
########################################################################################################################
# big pharma card
########################################################################################################################
rev_parma_content = [
    dbc.CardHeader("Revenue", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_revenue())
    ),
    dbc.CardFooter(
        html.P(
            "Revenue represents gains from sale of goods before costs such as taxes and pay role.  It shows how much "
            "a company sells. The blue line at the top shows what party the president of the time is a member of.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

net_income_parma_content = [
    dbc.CardHeader("Net Income", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_net_income())
    ),
    dbc.CardFooter(
        html.P(
            "Net Income is revenue less all costs of manufacturing, sales, pay roll and taxes. This shows how much the "
            "company is really profiting.  For example, if a company sells 1 billion dollars worth of product but has costs "
            "totaling 1.5 billion dollars the company operated at a huge loss. The blue line at the top shows what "
            "party the president of the time is a member of.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

profit_parma_content = [
    dbc.CardHeader("Profit to Revenue", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_profit())
    ),
    dbc.CardFooter(
        html.P(
            "This graph shows the percentage of profit to revenue.  In basic terms you would consider this the amount "
            "of one would take home from a paycheck after all deductions. This is an indiction of how much the company "
            "pays in taxes, pays employees, conducts research & development and more. The blue line at the top shows what" 
            "party the president of the time is a member of.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

diff_in_rev_parma_content = [
    dbc.CardHeader("Difference in Net Income to Revenue", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_diff_in_rev())
    ),
    dbc.CardFooter(
        html.P(
            "This graph shows the difference between revenue and net income. This indicates the amount of money the company "
            "spends to do business. The blue line at the top shows what party the president of the time is a member of.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

ceo_rating_parma_content = [
    dbc.CardHeader("Employee CEO Rating", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_approve_of_ceo())
    ),
    dbc.CardFooter(
        html.P(
            "This is the average between employee ratings of the organization's CEO. Scores were taken from indeed and Glassdoor.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

benefits_pay_parma_content = [
    dbc.CardHeader("Employee Benefits & Pay Rating", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_benefits_pay())
    ),
    dbc.CardFooter(
        html.P(
            "This is the average between employee ratings of the organization's pay and benefits. Scores were taken from indeed and Glassdoor.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

work_life_parma_content = [
    dbc.CardHeader("Work Life Balance", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_work_life())
    ),
    dbc.CardFooter(
        html.P(
            "This score is by employees on the work life balance from the position. ",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

job_sec_adv_parma_content = [
    dbc.CardHeader("Job Security & AQdvancement", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_job_sec_adv())
    ),
    dbc.CardFooter(
        html.P(
            "This score is by employees for how secure they feel in their position and the career advancement opportunities they have. ",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

mgnt_parma_content = [
    dbc.CardHeader("Employee Satisfaction with Management", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_mgnt())
    ),
    dbc.CardFooter(
        html.P(
            "This is a score by employees rating their Management at the company.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

culture_parma_content = [
    dbc.CardHeader("Employee Culture Score", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_culture())
    ),
    dbc.CardFooter(
        html.P(
            "This is a score by employees rating regarding the culture at the company.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

salary_sat_parma_content = [
    dbc.CardHeader("Employee Salary Satisfaction Score", style={"color": "white"}),
    dbc.CardBody(
        dcc.Graph(figure=pharma_salary_sat())
    ),
    dbc.CardFooter(
        html.P(
            "This is a score by employees rating regarding the salary for employees.",
            className="card-text",
            style={"color": "white"}
        ),
    )
]

########################################################################################################################
# big pharma card
########################################################################################################################
rev_parma_card = html.Div(
    [
        dbc.Row(
            dbc.Col(dbc.Card(rev_parma_content, color="dark"))
        )
    ]
)

net_income_parma_card = html.Div(
    [
        dbc.Row(
            dbc.Col(dbc.Card(net_income_parma_content, color="dark"))
        )
    ]
)

profit_parma_card = html.Div(
    [
        dbc.Row(
            dbc.Col(dbc.Card(profit_parma_content, color="dark"))
        )
    ]
)

diff_in_rev_parma_card = html.Div(
    [
        dbc.Row(
            dbc.Col(dbc.Card(diff_in_rev_parma_content, color="dark"))
        )
    ]
)

ceo_rating_parma_card = html.Div(
    [
        dbc.Row(
            dbc.Col(dbc.Card(ceo_rating_parma_content, color="dark")),
        )
    ]
)

benefits_pay_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(benefits_pay_parma_content, color="dark"))
    )
])

work_life_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(work_life_parma_content, color="dark"))
    )
])

job_sec_adv_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(job_sec_adv_parma_content, color="dark"))
    )
])

mgnt_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(mgnt_parma_content, color="dark"))
    )
])

culture_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(culture_parma_content, color="dark"))
    )
])

salary_sat_pharma_card = html.Div([
    dbc.Row(
        dbc.Col(dbc.Card(salary_sat_parma_content, color="dark"))
    )
])


########################################################################################################################
# Pharma Row
########################################################################################################################
pharma_row_1 = html.Div([
    dbc.Row([
        dbc.Col(rev_parma_card),
        dbc.Col(net_income_parma_card)
    ])
])

pharma_row_2 = html.Div([
    dbc.Row([
        dbc.Col(profit_parma_card),
        dbc.Col(diff_in_rev_parma_card)
    ])
])

pharma_row_3 = html.Div([
    dbc.Row([
        dbc.Col(ceo_rating_parma_card),
        dbc.Col(benefits_pay_pharma_card),
    ])
])

pharma_row_4 = html.Div([
    dbc.Row([
        dbc.Col(job_sec_adv_pharma_card),
        dbc.Col(mgnt_pharma_card),
        dbc.Col(culture_pharma_card),
    ])
])

pharma_row_5 = html.Div([
    dbc.Row([
        dbc.Col(work_life_pharma_card),
        dbc.Col(salary_sat_pharma_card)
    ])
])

########################################################################################################################
# big pharma - jumbotron big pharma
########################################################################################################################
jumbotron_big_pharma = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H3("Big Pharma Industry", className="display-5"),
                html.P(
                    "The purpose for this is wedsite to provide information so people can form their own opinion on popular topics."
                    "The site makes no assumptions or conclusions.  Rather, it consolidates data from multiple sources and "
                    "displays it in easy to analyze visuals.  This complete project with all data is available on github at "
                    "https://github.com/SaltyCoco/MeyitaAnalyticsDashboard",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "This dashboard displays metrics for pharmaceutical organizations which are incorporated within the United States. "
                    "The main metrics look at revenue, net income and employee ratings.  Each Company is identified by its stock symbol. ",
                    className="lead",
                ),
            ],
            fluid=True,
        )
    ],
    fluid=True
)
########################################################################################################################
# Navbar
########################################################################################################################
app.layout = html.Div(children=[
    navbar,
    jumbotron_big_pharma,
    pharma_row_1,
    html.Br(),
    html.Br(),
    html.Br(),
    pharma_row_2,
    html.Br(),
    html.Br(),
    html.Br(),
    pharma_row_3,
    html.Br(),
    html.Br(),
    html.Br(),
    pharma_row_4,
    html.Br(),
    html.Br(),
    html.Br(),
    pharma_row_5,
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4("This website was developed by and owned by Ryan Schulte"),
    html.Br(),
    html.Br(),
    html.Br(),
], style={"background-color": "black"})
########################################################################################################################
# Application
########################################################################################################################
if __name__ == '__main__':
    app.run_server()
