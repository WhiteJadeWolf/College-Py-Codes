""" Whenever your friends John and Judy visit you together, y'all have a party. 
Given a DataFrame with 10 rows representing the next 10 days of your schedule and whether John and Judy are scheduled to make an appearance, insert a new column called days_till_party that indicates how many days until the next party.
days_till_party should be 0 on days when a party occurs, 1 on days when a party doesn't occur but will occur the next day, etc. """

import pandas as pd

data = {
    'John':  [True, False, True, False, False, True, False, False, False, True],
    'Judy':  [True, False, False, False, True, True, False, True, False, True]
} # True - makes appearance on that particular day, False otherwise

df = pd.DataFrame(data)
df['party'] = df['John'] & df['Judy']
days_till_party = [None] * len(df)
next_party_index = None

for i in range(len(df)-1,-1,-1):
    if df.loc[i, 'party']:
        next_party_index = i
        days_till_party[i] = 0
    elif next_party_index is not None:
        days_till_party[i] = next_party_index - i
    else:
        days_till_party[i] = None
df['days_till_party'] = days_till_party
print(df)