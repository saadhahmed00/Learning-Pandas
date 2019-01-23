#Testing Shoefly

import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#print(ad_clicks.head())

print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

ad_clicks['is_click'] = ~ ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()




clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

#print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[False] + clicks_pivot[True])

#print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

a_or_b_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(columns = 'experimental_group', index = 'is_click', values = 'user_id').reset_index()

a_or_b_clicks['percentage_a'] = a_or_b_clicks['A'] / (a_or_b_clicks['A'] + a_or_b_clicks['B'])

#print(a_or_b_clicks)

a_clicks = ad_clicks[ad_clicks.experimental_group =='A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#print(a_clicks)

a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()

#print(a_clicks)

a_clicks["percent_a"] = a_clicks[True]/(a_clicks[True]+a_clicks[False])

b_clicks = ad_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()



b_clicks["percent_b"] = b_clicks[True]/(b_clicks[True]+b_clicks[False])

print(b_clicks)
print(a_clicks)

 