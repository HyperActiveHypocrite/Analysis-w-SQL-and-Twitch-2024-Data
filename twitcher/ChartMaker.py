import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
#connect sqlite with the .db file 
conn = sqlite3.connect("twitch.db")

#------------------ QUERy 1, AVERAGE views per stream , most watched  ------------------------
#desired query 
query1 = """
SELECT most_streamed_game,
       ROUND(AVG(avg_viewers_per_stream),2) AS avg_viewers
FROM streamers2024
GROUP BY most_streamed_game
ORDER BY avg_viewers DESC
LIMIT 10;
"""

#read the query from the db file using panadas 
gamesq1 = pd.read_sql_query(query1, conn)



#MAT PLOT LIB USES THE REST!!
#create new figure where height is 10 and width is 6
plt.figure(figsize=(10,6))

#make a bar chart where most_streamed game is x and avg_viewers is y 
plt.bar(gamesq1["most_streamed_game"], gamesq1["avg_viewers"])

#labels of the game overlapped ;;
plt.xticks(rotation=45)

# OUR TITLE
plt.title("Average Viewers by Most Streamed Game")

#x axis 
plt.xlabel("Game")
#y axis
plt.ylabel("Average Viewers")

#adjust spacing so things dont get excluded 
plt.tight_layout()

plt.savefig("images/avg_viewers_by_game.png")
plt.close()


#--------------- QUERY 2 --------------------



query2 = """
SELECT CAST(active_days_per_week AS INTEGER) AS days_streamed,
       ROUND(AVG(followers_gained_per_stream),2) AS avg_followers
FROM streamers2024
GROUP BY days_streamed
ORDER BY days_streamed;
"""

df_days = pd.read_sql_query(query2, conn)

plt.figure(figsize=(8,5))
plt.bar(df_days["days_streamed"], df_days["avg_followers"])
plt.title("Followers Gained by Days Streamed")
plt.xlabel("Days Streamed Per Week")
plt.ylabel("Average Followers Gained")
plt.tight_layout()
plt.savefig("images/followers_vs_days.png")
plt.close()





#---------------------- QUERY 4 : MOST ACTIVE DAYS -----------------------#
query3="""

SELECT most_active_day, COUNT(*) AS streamer_count
FROM streamers2024
GROUP BY most_active_day;


"""


active_days = pd.read_sql_query(query3, conn)

plt.figure(figsize=(8,5))
plt.bar(active_days["most_active_day"], active_days["streamer_count"])
plt.title("Most active days of the week")
plt.xlabel("Days")
plt.ylabel("times played")
plt.tight_layout()
plt.savefig("images/mostActiveDays.png")
plt.close()





#---------------------- QUERY 4 : TOP 25 streamers -----------------------#


query4="""
SELECT name,total_followers FROM streamers2024 LIMIT 25;

"""

toptwenty = pd.read_sql_query(query4, conn)
plt.figure(figsize=(10,8))
plt.gca().xaxis.set_major_formatter(
    ticker.StrMethodFormatter('{x:,.0f}')
)
plt.barh(toptwenty["name"], toptwenty["total_followers"])

plt.title("Top 25 Twitch Streamers by Total Followers")
plt.xlabel("Total Followers")
plt.ylabel("Streamer")

plt.tight_layout()
plt.savefig("images/top_25_streamers.png")
plt.close()

print("images made!")

# Close database connection
conn.close()