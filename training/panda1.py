import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])

df = pd.DataFrame({
'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
'population': [17.04, 143.5, 9.5, 45.5],
'square': [2724902, 17125191, 207600, 603628]
},index=['KZ', 'RU', 'BY', 'UA'])
print(df[df['country']=='Ukraine'])
df2 = df.loc['KZ':'BY',['country','square']]
print(df2)


cdf = pd.read_csv('owid-covid-data.csv', index_col=3, parse_dates=True)
print(cdf.head(5))
x = cdf.groupby(['iso_code'])['new_cases'].avg()

ukr = cdf.loc[cdf['iso_code'] == 'UKR', ['iso_code', 'new_cases', 'total_cases']]
ukr['DT'] = ukr.index

#ukr['week'] = ukr['DT'].dt.isocalendar().week
#ukr['week_start'] = ukr['DT'] - pd.to_timedelta(arg=ukr['DT'].dt.weekday, unit='D')
#ukr['week_day'] = ukr['DT'].dt.weekday
ukr_week = ukr[ukr['DT'].dt.weekday == 0].copy()
ukr_week['delta'] = ukr_week['total_cases'] - ukr_week['total_cases'].shift()
print(ukr_week['delta'].max())
cdf.shift()
#print(f'{cdf.shape=} \t {ukr.shape=} \t {ukr_week.shape=}')
# #print(ukr.head(10))
#print(afg.head(10))
#print(ukr_week.head(10))