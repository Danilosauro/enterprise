import pandas as pd
import hashlib 


df = pd.read_csv('synthetic_data.csv') 

df['name'] = df['name'].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest())
df['address'] = df['address'].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()) 

df.to_csv('synthetic_data.csv')