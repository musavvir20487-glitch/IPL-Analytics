# ================================ VISUALIZATIONS ========================
import matplotlib.pyplot as plt
import seaborn as sns

# Chart 1 - Top 10 teams by wins
plt.figure(figsize=(12, 6))
plt.barh(df_team_wins['winner'], df_team_wins['total_wins'], color='steelblue')
plt.xlabel('Total Wins')
plt.title('Top 10 IPL Teams by Total Wins', fontsize=16)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('charts/chart1_team_wins.png', dpi=150)
plt.show()
print("Chart 1 saved!")

df_team_wins['winner'] = df_team_wins['winner'].replace({
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
    'Kings XI Punjab': 'Punjab Kings',
    'Delhi Daredevils': 'Delhi Capitals',
    'Deccan Chargers': 'Sunrisers Hyderabad',
})

# Chart 2 - Top 10 Run Scorers
plt.figure(figsize=(12, 6))
sns.barplot(data=df_top_batsmen, x='total_runs', y='batter', color='steelblue')
plt.xlabel('Total Runs')
plt.ylabel('Batter')
plt.title('Top 10 IPL Run Scorers', fontsize=16)
plt.tight_layout()
plt.savefig('charts/chart2_top_scorers.png', dpi=150)
plt.show()
print("Chart 2 saved!")

# Chart 3 - Season-wise Total Runs Trend
plt.figure(figsize=(12, 6))
plt.plot(df_season_runs['season'], df_season_runs['total_runs'], 
         marker='*', color='steelblue', linewidth=2, markersize=9)
plt.xlabel('Season')
plt.ylabel('Total Runs')
plt.title('Season-wise Total Runs Trend in IPL', fontsize=16)
plt.xticks(df_season_runs['season'], rotation=45)
plt.tight_layout()
plt.savefig('charts/chart3_season_runs.png', dpi=150)
plt.show()
print("Chart 3 saved!")

# Chart 4 - Toss Decision Distribution
# Chart 4 - Toss Decision Distribution
plt.figure(figsize=(8, 8))
plt.pie(df_toss['total_matches'], labels=df_toss['toss_decision'],
        autopct='%1.1f%%', colors=['steelblue', 'lightblue'],
        startangle=90)
plt.title('Toss Decision Distribution (Field vs Bat)', fontsize=16)
plt.tight_layout()
plt.savefig('charts/chart4_toss_decision.png', dpi=150)
plt.show()
print("Chart 4 saved!")

# Chart 5 - Wins per Team per Season Heatmap
plt.figure(figsize=(18, 10))
sns.heatmap(df_heatmap, annot=True, fmt='.0f', cmap='Blues',
            linewidths=0.5, linecolor='gray')
plt.title('IPL Wins per Team per Season', fontsize=16)
plt.xlabel('Season')
plt.ylabel('Team')
plt.tight_layout()
plt.savefig('charts/chart5_heatmap.png', dpi=150)
plt.show()
print("Chart 5 saved!")

# Chart 6 - Top 10 Wicket Takers
plt.figure(figsize=(12, 6))
sns.barplot(data=df_top_bowlers, x='total_wickets', y='bowler', 
            hue='bowler', palette='Blues_d', legend=False)
plt.xlabel('Total Wickets')
plt.ylabel('Bowler')
plt.title('Top 10 IPL Wicket Takers', fontsize=16)
plt.tight_layout()
plt.savefig('charts/chart6_top_bowlers.png', dpi=150)
plt.show()
print("Chart 6 saved!")