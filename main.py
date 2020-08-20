import discord
import random




token = "Njk4Njc5MTA3NzU1NTczMjU4.XpJVoA.kJD-Gq2vlTP2t7YL9INJOk1Za4w"

client = discord.Client()

#TODO THINGS
# 2 - add tic tac toe
#
#


##ARRAYS
#player data arrays
playerIds = []
playerPoints = []

##FUNCTIONS
#Backend functions
async def resetFileData(message):
    members = message.guild.members
    channel = message.channel
    await channel.send('Resetting Data')
    f = open("players.txt", "w+")
    g = open("points.txt", "w+")
    for i in range(len(members)):
        f.write(members[i].discriminator + "\n")
        g.write("0\n")
    f.close()
    g.close()

async def addDataToFiles(message):
    global playerIds
    global playerPoints
    members = message.guild.members
    f = open("players.txt", "w+")
    g = open("points.txt", "w+")
    for i in range(len(members)):
        f.write(members[i].discriminator + "\n")
        g.write(playerPoints[i]+"\n")
    f.close()
    g.close()
    # print(playerPoints)


async def addFilesToData(message):
    global playerIds
    global playerPoints
    members = message.guild.members
    f = open("players.txt", "r+")
    g = open("points.txt", "r+")
    playerData = f.read()
    pointData = g.read()
    playerIds = playerData.split("\n")
    playerPoints = pointData.split("\n")
    # print(playerIds)
    f.close()
    g.close()

async def showPoints(message, channel):
    members = message.guild.members
    messageauthor = message.author
    for i in range(len(members)):
        if members[i].id == messageauthor.id:
            await channel.send(playerPoints[i])


#Games
async def flipCoin(message, channel, gambleAmount):
    members = message.guild.members
    messageauthor = message.author
    win = 0 #round(random.randint(0, 1))
    if win == 0:
        await channel.send("You Win!")
        for i in range(len(members)):
            if members[i].id == messageauthor.id:
                playerPoints[i] = str(int(playerPoints[i]) + int(gambleAmount))
        await addDataToFiles(message)
    elif win == 1:
        await channel.send("You Lose.")
        for i in range(len(members)):
            if members[i].id == messageauthor.id and int(playerPoints[i]) - 5 >= 0:
                playerPoints[i] = str(int(playerPoints[i]) - int(gambleAmount))
            else:
                playerPoints[i] = "0"
        await addDataToFiles(message)




##CLIENT EVENTS
@client.event
async def on_ready():
    print("Red Online")
    print("----------")


@client.event
async def on_message(message):
    ##VARIABLES
    members = message.guild.members
    channel = message.channel

    ##INITIALIZING DATA FUNCTIONS
    await addFilesToData(message)

    if message.author != client:
        messageContent = message.content
        if "$play" in messageContent.lower():
            gambleAmount = ""
            addingGamble = False
            for i in range(len(messageContent)):
                gambleAmount
                addingGamble
                if addingGamble == True:
                    gambleAmount += messageContent[i]
                if messageContent[i] == "-":
                    addingGamble = True
            for i in range(len(members)):
                messageauthor = message.author
                if members[i].id == messageauthor.id:
                    currentPlayerPoints = int(playerPoints[i])
                    print(currentPlayerPoints > int(gambleAmount))
                    if currentPlayerPoints >= int(gambleAmount):
                        await flipCoin(message, channel, gambleAmount)
                    else:
                        await channel.send("Not Enough Points")
        if messageContent == "$points":
            await showPoints(message, channel)
        if messageContent == "$reset:Joshlandia15":
            #print("True")
            await resetFileData(message)


client.run(token)