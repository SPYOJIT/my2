import pandas as pd
import plotly.express as px

df=pd.read_csv(r"C:\Users\PC World\OneDrive\Desktop\Class\c 103\data.csv")
fig=px.scatter(df,x="Population",y="Per capita ",size="Percentage",color="Country",size_max=60)
fig.show()