from discord_crawler import discord
from adlink_crawler import ad_link

#Step 1
question_1 = input("Do you want to skip Step 1 [y / n] ? ")
if question_1 == "n":
    discord(channel_id, "discord_token", "url_to_grab")
elif question_1 == "y":
    #It will keep your file content
    pass

#Step 2
question_2 = input("Do you want to skip Step 2 [y / n] ? ")
if question_2 == "n":
    ad_link("adlink_url", "last_mega_banned")
elif question_2 == "y":
    #It will keep your file content
    pass


