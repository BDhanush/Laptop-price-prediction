import pandas as pd
import re

df = pd.read_excel("complete laptop data.xlsx")
req = df["Screen Resolution"]
ar = list(req)

for i in range(len(ar)):
    res =" ".join(re.split(r'\D+',ar[i])).split()
    if len(res)==1:
        ar[i]=int(res[0])
    else:
        ar[i]=min(int(res[0]),int(res[1]))
for i in range(len(ar)):
    if ar[i]>=2160:
        ar[i]=2160
    elif ar[i]>=1440:
        ar[i]=1440
    elif ar[i]>=1080:
        ar[i]=1080
    elif ar[i]>=720:
        ar[i]=720
    else:
        ar[i]=480
print(ar)
