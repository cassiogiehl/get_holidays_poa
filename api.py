import requests
import pandas as pd

# csc_dw.calendario
url = 'https://api.calendario.com.br/?json=true&ano=2020&estado=RS&cidade=PORTO_ALEGRE&token=Y2Fzc2lvLmdpZWhsQGRiY2NvbXBhbnkuY29tLmJyJmhhc2g9MTY2MDYzNTg0'
resp = requests.get(url)
holidays = resp.json()
data = []
name = []

for hol in holidays:
    data.append(hol['date'])
    name.append(hol['name'])

df = pd.DataFrame()
df['Data'] = data
df['Feriado'] = name
df.to_csv('calendario.csv', index=False, sep=';')
