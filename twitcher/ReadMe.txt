Twitch-streamer-analysis 2024 | Practice with SQL

OVERVIEW:
This project analyzes Twitch streamer data using SQL to identify trends regarding streaming on twitch. The goal was to practice querying a relational database and answer business-oriented questions using real-world data.

DataSet:
Dataset: datasetV2.csv
Database: SQLite
Language: SQL & python


As much as I want to do an analysis on 2025 or 2026, twitchtracker doesn't legally allow scraping so I got the data from Kaggle from user HIBRAHIMAG1

Credits for the CSV file:
 HIBRAHIMAG1 "Top 1000 Twitch Streamers Data" : https://www.kaggle.com/datasets/hibrahimag1/top-1000-twitch-streamers-data-may-2024

Project Objective

Which games are streamed the most?
What days are streamers most active?
Is there a relationship between number of days streaming and followers gained?
Is there a relationship with most played game and most number of viewers?



SET-UP:
created a folder called twitcher, opened up in VSCode, make sure to have SQLite and or SQLite viewer so it works.
Also helps when you can visually see your table. Yes you could probably just use the command line if you download
SQLite x86 or something, but it hurts my soul looking at it.



NOTES : probably nicer to set the mode to .mode table to make it visually easier to understand 


notes to myself :
group by when doing things like AVG(), if you don't use group by it only gives one number, we want the avg of individual groups (separates games like MC with Just Chatting)