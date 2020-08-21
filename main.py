import discord
import json
import random




token = "Njk4Njc5MTA3NzU1NTczMjU4.XpJVoA.kJD-Gq2vlTP2t7YL9INJOk1Za4w"

client = discord.Client()
#TODO THINGS
# 1 - fix the shuffle tracking system so that it actually tracks it from the file and the arrays
#

playerDicts = []


##FUNCTIONS
#Backend functions
async def resetFileData(message):
    members = message.guild.members
    channel = message.channel
    await channel.send('Resetting Data')
    f = open("players.txt", "w+")
    for i in range(len(members)):
        tempPersonDict = '{"discriminator": "'+str(members[i].discriminator)+'", "points": "0", "shuffles": "0", nameChanges: "0"}'
        f.write(tempPersonDict+"\n")
    f.close()

async def takeDataFromJsonFile(message):
    #Setting up the json file data
    global playerDicts
    dataArray = ""
    f = open("players.txt","r+")
    data = f.read()
    dataArray = data.split("\n")
    f.close()
    for i in range(len(dataArray)):
        tempDict = json.loads(dataArray[i])
        playerDicts.append(tempDict)
    print(playerDicts)

async def showPoints(message, channel):
    global playerIds
    global playerPoints
    global playerInventory
    members = message.guild.members
    messageauthor = message.author
    for i in range(len(members)):
        if members[i].id == messageauthor.id:
            await channel.send(playerPoints[i])

async def showInventory(message, channel):
    global playerIds
    global playerPoints
    global playerInventory
    members = message.guild.members
    messageauthor = message.author
    for i in range(len(members)):
        if members[i].id == messageauthor.id:
            await channel.send(playerInventory[i])

async def showHelp(message, channel):
    await channel.send("The Dealer Commands: \n$play-XX -> $play- followed by a number of points will allow you to gamble that number of points. If you have less than 10 points you can gamble up to 10.\n$points -> this command will show you how many points you currently have.\n $shop -> This command will show everything that is for sale currently along with it's price.\n $inventory will show how many items you have in your inventory.\n $buy XX -> This command followed by what you want to buy will buy that item from the shop, provided you have the necesary point count.\n $use XX -> This command will use the item that you type from your inventory, provided you have that item.\n $idea XX -?> This command followed by an idea for the bot will be tracked on the suggestion folder for the devs to add features.\n $help -> This command will show this message again.")

async def showShop(message, channel):
    await channel.send("\n--The Shop--\n VC Shuffle -> 100 points \n Rename an 100% user -> 300 points")

async def addToInventory(message, channel, item):  
    #print(playerPoints[playerIndex])
    for i in range(len(members)):
            if members[i].id == messageauthor.id:
                playerInventory[playerIndex] = str( int(playerInventory[playerIndex]) + 1)
                playerPoints[playerIndex] = str(int(playerPoints[playerIndex]) - 100)
                #print(playerPoints[playerIndex])
    await channel.send("Purchase Completed!")

async def useShuffle(message, channel, playerIndex):
    playerInventory[playerIndex] = str(int(playerInventory[playerIndex])-1)
    await shuffle(message, channel)

#Games
async def flipCoin(message, channel, gambleAmount):
    members = message.guild.members
    messageauthor = message.author
    win = round(random.randint(0, 1))
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


#Shop item functions
async def shuffle(message, channel):
    members = message.guild.members
    onlineMembers = []
    for i in range(len(members)):
        if members[i].status == "online":
            onlinerMembers.append(members[i])
    totalChannels = message.guild.channels
    voiceChannels = []
    for i in range(len(totalChannels)):
        if "corner" in totalChannels[i].name.lower():
            voiceChannels.append(totalChannels[i])
    for i in range(len(onlineMembers)):
        try:
            randomVC = voiceChannels[round(random.randint(0,(len(voiceChannels) - 1)))]
            await onlineMembers[i].move_to(randomVC, reason="Shuffle Activated")
        except discord.HTTPException:
            print("ERR")
        else:
            pass
            
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
    #await takeDataFromJsonFile(message)

    if message.author != client:
        messageContent = message.content
        if "$play" in messageContent:
            gambleAmount = ""
            addingGamble = False
            for i in range(len(messageContent)):
                gambleAmount
                addingGamble
                if addingGamble == True:
                    gambleAmount += messageContent[i]
                if messageContent[i] == " ":
                    addingGamble = True
            for i in range(len(members)):
                messageauthor = message.author
                if members[i].id == messageauthor.id:
                    currentPlayerPoints = int(playerPoints[i])
                    # print(currentPlayerPoints > int(gambleAmount))
                    if currentPlayerPoints >= int(gambleAmount):
                        await flipCoin(message, channel, gambleAmount)
                        await addDataToFiles(message)
                        await addFilesToData(message)
                    elif int(gambleAmount) <= 10 and currentPlayerPoints <= 10:
                        await flipCoin(message, channel, gambleAmount)
                        await addDataToFiles(message)
                        await addFilesToData(message)
                    else:
                        await channel.send("Not Enough Points")
        if messageContent == "$points":
            await showPoints(message, channel)
        if messageContent == "$inventory":
            await showInventory(message, channel)
        if messageContent == "$reset:KerrySpice15":
            #print("True")
            await resetFileData(message)
        if messageContent == "$help":
            await showHelp(message, channel)
        if messageContent == "$shop":
            await showShop(message, channel)
        if "$buy" in messageContent:
            itemToBuy = ""
            addingItemText = False
            for i in range(len(messageContent)):
                itemToBuy
                addingItemText
                if addingItemText == True:
                    itemToBuy += messageContent[i]
                if messageContent[i] == " ":
                    addingItemText = True
            print(itemToBuy)
            for i in range(len(members)):
                messageauthor = message.author
                if members[i].id == messageauthor.id:
                    if itemToBuy == "shuffle":
                        print(playerIds[i])
                        currentPlayerPoints = int(playerPoints[i])
                        print(members[i].name)
                        if currentPlayerPoints >= 100:
                            await addToInventory(message, channel, "shuffle")
                            await addDataToFiles(message)
                            await addFilesToData(message)
                        else:
                            await channel.send("Not Enough Points")
        if "$use" in messageContent:
            itemToUse = ""
            addingItemText = False
            for i in range(len(messageContent)):
                itemToUse
                addingItemText
                if addingItemText == True:
                    itemToUse += messageContent[i]
                if messageContent[i] == " ":
                    addingItemText = True
            print(itemToUse)
            for i in range(len(members)):
                messageauthor = message.author
                if members[i].id == messageauthor.id:
                    if itemToUse == "shuffle":
                        print(playerIds[i])
                        currentPlayerShuffles = int(playerInventory[i])
                        print(members[i].name)
                        if currentPlayerShuffles >= 1:
                            await useShuffle(message, channel, i)
                            await addDataToFiles(message)
                            await addFilesToData(message)
                        else:
                            await channel.send("No Shuffles Available.")
        if "$idea" in messageContent:
            idea = ""
            addingItemText = False
            for i in range(len(messageContent)):
                idea
                addingItemText
                if addingItemText == True:
                    idea += messageContent[i]
                if messageContent[i] == " ":
                    addingItemText = True
            print(idea)
            f = open("suggestions.txt", "a+")
            f.write(idea+"\n")
            f.close()
            await channel.send("Suggestion Noted!")
client.run(token)
