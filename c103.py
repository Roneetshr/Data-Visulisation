import pandas as pd
import plotly.express as px

Population = [2003,2004,2005,2006,2007,2008]
df = pd.read_csv("Copy+of+data+-+data.csv")
#fig = px.scatter(df,x = "Population",y = "Per capita",color = "Country",title = "Per Capita Income", size = "Percentage", size_max = 60)
#fig = px.bar(df,x = "Country",y = "InternetUsers",color = "Country", title = "Internet Users in Countries")
fig = px.line(df,x="date",y="cases",color="country",title="Capita Income Per Country")
fig.show()