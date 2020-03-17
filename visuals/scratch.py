
import os
import pandas as pd
import plotly.offline as plo
import plotly.graph_objects as go

base_dir = os.path.dirname(__file__)

df = pd.read_csv("../data/cdc/National_Custom_Data.csv")



df = df[["SEASON", "WEEK", "NUM PNEUMONIA DEATHS", "NUM INFLUENZA DEATHS"]]
df = df.sort_values(by=["WEEK"], ascending=True)
print(df)
df2019_20 = df[df["SEASON"]=="2019-20"]
df2018_19 = df[df["SEASON"]=="2018-19"]
df2017_18 = df[df["SEASON"]=="2017-18"]
df2016_17 = df[df["SEASON"]=="2016-17"]
df2015_16 = df[df["SEASON"]=="2015-16"]
df2014_15 = df[df["SEASON"]=="2014-15"]
df2013_14 = df[df["SEASON"]=="2013-14"]


tr2019_20 = go.Scatter(
    x=df2019_20["WEEK"],
    y=df2019_20["NUM PNEUMONIA DEATHS"],
    name="2019-20"
)
tr2018_19 = go.Scatter(
    x=df2018_19["WEEK"],
    y=df2018_19["NUM PNEUMONIA DEATHS"],
    name="2018-19"
)
tr2017_18 = go.Scatter(
    x=df2017_18["WEEK"],
    y=df2017_18["NUM PNEUMONIA DEATHS"],
    name="2017-18"
)
tr2016_17 = go.Scatter(
    x=df2016_17["WEEK"],
    y=df2016_17["NUM PNEUMONIA DEATHS"],
    name="2016-18"
)
tr2015_16 = go.Scatter(
    x=df2015_16["WEEK"],
    y=df2015_16["NUM PNEUMONIA DEATHS"],
    name="2015-16"
)
tr2014_15 = go.Scatter(
    x=df2014_15["WEEK"],
    y=df2014_15["NUM PNEUMONIA DEATHS"],
    name="2014-15"
)
tr2013_14 = go.Scatter(
    x=df2013_14["WEEK"].astype(int),
    y=df2013_14["NUM PNEUMONIA DEATHS"],
    name="2013-14"
)

layout = go.Layout(
    title="National Pneumonia Deaths by Week of Season",
    template="plotly_dark",
    xaxis=dict(
        title="Week of Season"
    ),
    yaxis=dict(
        title="Number of Pneumonia Deaths"
    )
)

data = [tr2013_14, tr2014_15, tr2015_16, tr2016_17, tr2017_18, tr2018_19, tr2019_20]

fig = go.Figure(data=data, layout=layout)

#plo.plot(fig, filename="pnoTest.html")

trfl2019_20 = go.Scatter(
    x=df2019_20["WEEK"],
    y=df2019_20["NUM INFLUENZA DEATHS"],
    name="2019-20"
)
trfl2018_19 = go.Scatter(
    x=df2018_19["WEEK"],
    y=df2018_19["NUM INFLUENZA DEATHS"],
    name="2018-19"
)
trfl2017_18 = go.Scatter(
    x=df2017_18["WEEK"],
    y=df2017_18["NUM INFLUENZA DEATHS"],
    name="2017-18"
)
trfl2016_17 = go.Scatter(
    x=df2016_17["WEEK"],
    y=df2016_17["NUM INFLUENZA DEATHS"],
    name="2016-18"
)
trfl2015_16 = go.Scatter(
    x=df2015_16["WEEK"],
    y=df2015_16["NUM INFLUENZA DEATHS"],
    name="2015-16"
)
trfl2014_15 = go.Scatter(
    x=df2014_15["WEEK"],
    y=df2014_15["NUM INFLUENZA DEATHS"],
    name="2014-15"
)
trfl2013_14 = go.Scatter(
    x=df2013_14["WEEK"].astype(int),
    y=df2013_14["NUM INFLUENZA DEATHS"],
    name="2013-14"
)

fl_layout = go.Layout(
    title="National Influenza Deaths by Week of Season",
    template="plotly_dark",
    xaxis=dict(
        title="Week of Season"
    ),
    yaxis=dict(
        title="Number of Influenza Deaths"
    )
)

data = [trfl2013_14, trfl2014_15, trfl2015_16, trfl2016_17, trfl2017_18, trfl2018_19, trfl2019_20]

fig = go.Figure(data=data, layout=layout)

plo.plot(fig, filename="flTest.html")
