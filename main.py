from discord_crawler import discord
from adlink_crawler import ad_link

#Step 1
question_1 = input("Do you want to skip Step 1 [y / n] ? ")
if question_1 == "n":
    discord(1087768671352537239, "YOUR_TOKEN", "nude")
elif question_1 == "y":
    #It will keep your file content
    pass

#Step 2
question_2 = input("Do you want to skip Step 2 [y / n] ? ")
if question_2 == "n":
    ad_link("pastelink")
elif question_2 == "y":
    #It will keep your file content
    pass


