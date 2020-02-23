# visuals/scratch.py

import pandas as pd
import plotly.offline as plo
import plotly.graph_objects as go

df = pd.read_csv("../data/main/mainDataFeeder.csv")

#print(df.head())

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


plo.plot(net_income_fig, filename="net_income_test.html")



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

plo.plot(rev_fig, filename="revenue_test.html")

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

plo.plot(pct_fig, filename="pct_test.html")
