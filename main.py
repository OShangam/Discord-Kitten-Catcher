from discord_crawler import discord
from adlink_crawler import ad_link

#Step 1
question_1 = input("Do you want to skip Step 1 [y / n] ? ")
if question_1 == "n":
    discord(1126169776918634547, "YOUR_TOKEN", "leak")
elif question_1 == "y":
    #It will keep your file content
    pass

#Step 2
question_2 = input("Do you want to skip Step 2 [y / n] ? ")
if question_2 == "n":
    ad_link("rentry", "https://mega.nz/folder/lyUUAJDa#7qNBAOD2GrYL-tjdJr1mmg")
elif question_2 == "y":
    #It will keep your file content
    pass


