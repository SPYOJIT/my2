import pandas as pd
import plotly.express as px

df=pd.read_csv(r"C:\Users\PC World\OneDrive\Desktop\Class\c 103\data.csv")
fig=px.bar(df,x='Country',y='InternetUsers')
fig.show()