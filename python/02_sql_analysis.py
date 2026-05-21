import subprocess
subprocess.run(['pip','install','mysql-connector-python'])

import mysql.connector
print("mysql connector ready")

conn = mysql.connector.connect(
    host  = 'localhost',
    user = 'root',
    password = 'syedrehan20487',
    database = 'ipl_analytics'
)

cursor = conn.cursor()
print("Connected to MySQL Successfully")

conn.reconnect()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM matches")
result = cursor.fetchone()
print("Total matches:", result[0])

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:syedrehan20487@localhost/ipl_analytics')

df_top_batsmen = pd.read_sql_query(query1, engine)
print("Top 10 Batsmen:")
print(df_top_batsmen)

# Q002 - Top 10 bowlers by wickets
query2 = """
SELECT bowler, COUNT(*) AS total_wickets
FROM deliveries
WHERE is_wicket = 1 AND dismissal_kind != 'run out'
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10
"""
df_top_bowlers = pd.read_sql_query(query2, engine)
print("Top 10 Bowlers:")
print(df_top_bowlers)

# Q003 - Toss decision analysis
query3 = """
SELECT toss_decision,
       COUNT(*) AS total_matches,
       SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) AS toss_winner_won,
       ROUND(SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS win_pct
FROM matches
WHERE winner IS NOT NULL
GROUP BY toss_decision
"""
df_toss = pd.read_sql_query(query3, engine)
print("\nToss Decision Analysis:")
print(df_toss)

# Q004 - Season wise average first innings score
query4 = """
SELECT m.season, ROUND(AVG(innings_total), 2) AS avg_first_innings_score
FROM matches m
JOIN (
    SELECT match_id, SUM(total_runs) AS innings_total
    FROM deliveries
    WHERE inning = 1
    GROUP BY match_id
) d ON m.id = d.match_id
GROUP BY m.season
ORDER BY m.season ASC
"""
df_season_scores = pd.read_sql_query(query4, engine)
print("\nSeason-wise Avg First Innings Score:")
print(df_season_scores)

# Q005 - Top 10 run scorers (for visualization later)
query5 = """
SELECT batter, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10
"""
df_run_scorers = pd.read_sql_query(query5, engine)

# Q006 - Top 10 wicket takers (for visualization later)
query6 = """
SELECT bowler, COUNT(*) AS total_wickets
FROM deliveries
WHERE is_wicket = 1 AND dismissal_kind != 'run out'
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10
"""
df_wicket_takers = pd.read_sql_query(query6, engine)

# Q007 - Team wins (for visualization later)
query7 = """
SELECT winner, COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 10
"""
df_team_wins = pd.read_sql_query(query7, engine)
print("Team Wins:")
print(df_team_wins)

# Q008 - Season wise total runs (for line chart)
query8 = """
SELECT m.season, SUM(d.total_runs) AS total_runs
FROM matches m
JOIN deliveries d ON m.id = d.match_id
GROUP BY m.season
ORDER BY m.season ASC
"""
df_season_runs = pd.read_sql_query(query8, engine)
print("\nSeason-wise Total Runs:")
print(df_season_runs)

print("\nAll DataFrames ready for visualization!")

query_heatmap = """
SELECT season, winner, COUNT(*) AS wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY season, winner
ORDER BY season ASC
"""
df_heatmap_raw = pd.read_sql_query(query_heatmap, engine)
df_heatmap = df_heatmap_raw.pivot_table(
    index='winner', columns='season', values='wins', fill_value=0
)
print("Heatmap data ready")
print(df_heatmap.shape)