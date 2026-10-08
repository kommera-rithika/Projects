import pandas as pd
import numpy as np
df=pd.read_csv("24241A6632.csv")
'''arr=df[["Chat","Video","Study","Games"]].to_numpy()
print(arr.shape[0])
total_minutes=arr.sum(axis=0)
print(total_minutes)
'''
chat=df["Chat"].to_numpy()
video=df["Video"].to_numpy()
study=df["Study"].to_numpy()
games=df["Games"].to_numpy()
print("Total minutes over all days for each app: ", chat.sum(), video.sum(), study.sum(), games.sum())
print("Mean minutes per day for each app: ", round(chat.mean(),1), video.mean().round(1), study.mean().round(1), games.mean().round(1))
balance=study-games
print(f"Best day for study vs games: {int(balance.argmax())} with a balance of {balance.max()} minutes")
# Which app won each day
names=["Chat","Video","Study","Games"]
winners=[]
for i in range(len(chat)):
    daily=[chat[i],video[i],study[i],games[i]]
    best=0
    for j in range(1,4):
        if daily[j]>daily[best]:
            best=j
    winners.append(names[best])
print(winners)
app_total=chat+video+study+games
chat_percent=chat/app_total*100
video_percent=video/app_total*100
study_percent=study/app_total*100
games_percent=games/app_total*100
print(chat_percent)
print(video_percent)
print(study_percent)
print(games_percent)
print(app_total)