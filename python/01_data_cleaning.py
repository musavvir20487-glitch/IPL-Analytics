import pandas as pd

matches= pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print(matches.shape)
print(deliveries.shape)

print(deliveries.isnull().sum())

matches['city'] = matches['city'].fillna('Unknown')

print(matches.isnull().sum())

team_name_map = {
    'Deccan Chargers' : 'Sunrisers Hyderabad',
    'Delhi Daredevils' : 'Delhi Capitals',
    'Rising Pune Supergiant':'Rising Pune Supergiants',
    'Royal Challengers Bangalore':'Royal Challengers Bengaluru',
    'Kings XI Punjab':'Punjab Kings'
}

for col in ['team1', 'team2','toss_winner','winner']:
    matches[col] = matches[col].replace(team_name_map)
for col in ['batting_team','bowling_team']:
    deliveries[col] = deliveries[col].replace(team_name_map)

print(sorted(matches['team1'].unique()))

matches.to_csv('matches_cleaned.csv',index = False)
deliveries.to_csv('deliveries_cleaned.csv',index = False)

print("Done! Cleaned files saved.")