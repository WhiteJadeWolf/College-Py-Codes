""" Given a dataset of concerts, count the number of concerts per (artist, venue), per year month. 
Make the resulting table be a wide table - one row per year month with a column for each unique (artist, venue) pair. 
Use the cross product of the artists and venues Series to determine which (artist, venue) pairs to include in the result. """

import pandas as pd
import itertools

data = {
    'artist': ['ZAYN', 'ZAYN', 'Chase Atlantic', 'The Chainsmokers', 'Chase Atlantic', 'ZAYN'],
    'venue': ['New York', 'Las Vegas', 'New York', 'Las Vegas', 'Las Vegas', 'New York'],
    'date': pd.to_datetime([
        '2024-01-10', '2024-01-15', '2024-02-01',
        '2024-01-20', '2024-02-10', '2024-01-25'
    ])
}
df = pd.DataFrame(data)

df['yr_mon'] = df['date'].dt.to_period('M').astype(str)
grouped = df.groupby(['yr_mon', 'artist', 'venue']).size().reset_index(name='concert_count')
months = df['yr_mon'].unique()
artists = df['artist'].unique()
venues = df['venue'].unique()
full_index = pd.DataFrame(list(itertools.product(months, artists, venues)), columns = ['yr_mon','artist','venue'])
merged = pd.merge(full_index, grouped, how = 'left', on = ['yr_mon', 'artist', 'venue']).fillna(0)
pivot = merged.pivot(index = 'yr_mon', columns = ['artist', 'venue'], values = 'concert_count')
pivot.columns = [f"{a}_{v}" for a, v in pivot.columns]
pivot = pivot.sort_index()
print(pivot)