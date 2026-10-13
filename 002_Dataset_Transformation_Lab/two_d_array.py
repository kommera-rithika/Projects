import pandas as pd
import numpy as np
df=pd.read_csv("24241A6632.csv")
#apps=["Chat","Video","Study","Games"]
apps=np.array(df.columns)
#df[apps].to_numpy()
#tables=[df[f"{i}"].to_numpy() for i in apps]
#tables=df[["Chat","Video","Study","Games"]].to_numpy()
tables=df[apps].to_numpy()
#table=np.array(tables)
print(table)
print(table.shape)
per_app=table.sum(axis=0)
per_day=table.sum(axis=1)
print(table[:7])
print(np.round(table.mean(axis=0),1))
print(np.round(table.mean(axis=1),1))
print(table.max(axis=0))
print(table.max(axis=1))
print(table.min(axis=0))
print(table.min(axis=1))
winners=apps[table.argmax(axis=1)]
unique_winners,count=np.unique(winners,return_counts=True)
print(dict(zip(unique_winners,count.tolist())))
shares=table/per_day[:,None]*100
#np.newaccess
