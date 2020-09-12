import discord
import json
import random




token = "Njk4Njc5MTA3NzU1NTczMjU4.XpJVoA.kJD-Gq2vlTP2t7YL9INJOk1Za4w"

client = discord.Client()
#TODO THINGS
# 1 - fix the shuffle tracking system so that it actually tracks it from the file and the arrays
#

playerDicts = []


####FUNCTIONS
##Backend functions

#file + data processing
async def resetFileData(message):
    members = message.guild.members
    channel = message.channel
    await channel.send('Resetting Data')
    for i in range(len(members)):
        f = open(str(members[i].discriminator)+'.json', 'w+')
        person_dict = {"discriminator": members[i].discriminator, "username": members[i].name, "points": "0", "shuffles": "0"}
        json.dump(person_dict, f)
        f.close()

async def takeDataFromJsonFile(message):
    global playerDicts
    members = message.guild.members
    #Setting up the json file data
    for i in range(len(members)):
        with open(str(members[i].discriminator)+'.json') as f:
            playerDicts.append(json.load(f))
    #print(playerDicts)

async def addDataToJsonFile(message, currentPlayerIndex):
    global playerDicts
    members = message.guild.members
    channel = message.channel
    currentPlayer = playerDicts[currentPlayerIndex]
    f = open(str(members[currentPlayerIndex].discriminator)+'.json', 'w+')
    person_dict = {"discriminator": currentPlayer["discriminator"], "username": currentPlayer["username"], "points": currentPlayer["points"], "shuffles": currentPlayer["shuffles"]}
    print(person_dict)
    json.dump(person_dict, f)
    f.close()

#Command functions
async def showPoints(message, channel):
    members = message.guild.members
    for i in range(len(members)):
        messageauthor = message.author
        if members[i].id == messageauthor.id:
            currentPlayer = playerDicts[i]
            currentPlayerPoints = currentPlayer["points"]
            await channel.send(str(currentPlayer["username"])+"'s Points: "+str(currentPlayerPoints))

async def showInventory(message, channel):
    members = message.guild.members
    for i in range(len(members)):
        messageauthor = message.author
        if members[i].id == messageauthor.id:
            currentPlayer = playerDicts[i]
            currentPlayerShuffles = currentPlayer["shuffles"]
            await channel.send(str(currentPlayer["username"])+"'s Inventory: Shuffles -> x"+str(currentPlayerShuffles))

async def showShop(channel):
    shopMessage = "--The Dealer's Shop-- \n Shuffles -> 100 points each"
    await channel.send(shopMessage)

async def buyItem(message, channel, gambleAmount, currentPlayerIndex):
    global playerDicts
    if gambleAmount.lower() == "shuffle":
        currentPlayer = playerDicts[currentPlayerIndex]
        currentPlayer["shuffles"] = str(int(currentPlayer["shuffles"]) + 1)
        currentPlayer["points"] = str(int(currentPlayer["points"]) - 100)
        await channel.send("Purchase Confirmed!")
        await addDataToJsonFile(message, currentPlayerIndex)

async def showHelp(channel):
    helpMessage = "--HELP--\n$help - shows all the commands \n$play xx - flips a coin and gambles the amount of points specified by, xx. If you have <= 10 points you can gamble up to 10 free ones.\n$points - shows your points\n$inventory - shows the items you have\n$shop - shows everything for sale currently\n$buy xx - same thing as $play xx, you buy whatever item you type after the command\n$use xx - you use whatever item you type after the command\n$reset:PASSWORD - who ever is running the server can use this to reset the data for everyone\n$idea XX - users can add ideas to the suggestions file to suggest new features"
    await channel.send(helpMessage)

async def useItem(message, channel, currentPlayerIndex, item):
    global playerDicts
    currentPlayer = playerDicts[currentPlayerIndex]
    if item == "shuffle":
        currentPlayer["shuffles"] = str(int(currentPlayer["shuffles"]) - 1)
    await channel.send("Shuffling")
    await shuffle(message, channel)


##Game functions
async def flipCoin(message, channel, gambleAmount, currentPlayerIndex):
    global playerDicts
    win = round(random.randint(0,1))
    if win == 0:
        await channel.send("You Win!")
        currentPlayer = playerDicts[currentPlayerIndex]
        currentPlayerPoints = currentPlayer["points"]
        currentPlayer["points"] = str(int(currentPlayerPoints) + int(gambleAmount))
        await addDataToJsonFile(message, currentPlayerIndex)
    elif win == 1:
        await channel.send("You Lose.")
        currentPlayer = playerDicts[currentPlayerIndex]
        currentPlayerPoints = currentPlayer["points"]
        currentPlayer["points"] = str(int(currentPlayerPoints) - int(gambleAmount))
        await addDataToJsonFile(message, currentPlayerIndex)

##Shop item functions
async def shuffle(message, channel):
    members = message.guild.members
    totalChannels = message.guild.channels
    voiceChannels = []
    onlineMembers = []
    for i in range(len(totalChannels)):
        
        totalChannelsName = totalChannels[i].name
        if "corner" in totalChannelsName.lower():
            voiceChannels.append(totalChannels[i])
    for i in range(len(members)):
        if members[i].status != "offline":
            onlineMembers.append(members[i])
    for i in range(len(onlineMembers)):
        try:
            randomVC = voiceChannels[round(random.randint(0,(len(voiceChannels) - 1)))]
            await onlineMembers[i].move_to(randomVC, reason="Shuffle Activated")
            # print(True)
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
    global playerDicts
    ##VARIABLES
    members = message.guild.members
    channel = message.channel

    ##INITIALIZING DATA FUNCTIONS
    await takeDataFromJsonFile(message)
    #print(playerDicts)
    #muting the players for games
    if message.author != client:
        messageContent = message.content
        ## Commands with an input
                    if "$mute" in messageContent.lower():
            if str(message.author.discriminator) == "5252" or str(message.author.discriminator) == "3321" or str(message.author.discriminator) == "4629":
                for i in range(len(vcIds)):
                    print(vcIds[i])
                    currentChannel = client.get_channel(vcIds[i])
                    if message.author in currentChannel.members:
                        print("Found the VC")
                        for i in range(len(members)):
                            if members[i].name == message.author.name:
                                pass
                            else:
                                try:
                                    await members[i].edit(mute=True)
                                except discord.errors.HTTPException:
                                    pass
                                else:
                                    pass

        if "$unmute" in messageContent.lower():
            if str(message.author.discriminator) == "5252" or str(message.author.discriminator) == "3321" or str(
                    message.author.discriminator) == "4629":
                for i in range(len(vcIds)):
                    print(vcIds[i])
                    currentChannel = client.get_channel(vcIds[i])
                    if message.author in currentChannel.members:
                        print("Found the VC")
                        for i in range(len(members)):
                            if members[i].name == message.author.name:
                                pass
                            else:
                                try:
                                    await members[i].edit(mute=False)
                                except discord.errors.HTTPException:
                                    pass
                                else:
                                    pass
        
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
                    currentPlayer = playerDicts[i]
                    currentPlayerPoints = int(currentPlayer["points"])
                    if currentPlayerPoints >= int(gambleAmount):
                        await flipCoin(message, channel, gambleAmount, i)
                    elif int(gambleAmount) <= 10 and currentPlayerPoints <= 10:
                        await flipCoin(message, channel, gambleAmount, i)
                    else:
                        await channel.send("Not Enough Points")
        if "$buy" in messageContent:
            #gambleAmount in this function takes the item to buy instead of the gamble amount from $play
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
                    currentPlayer = playerDicts[i]
                    currentPlayerPoints = int(currentPlayer["points"])
                    if gambleAmount.lower() == "shuffle":
                        if currentPlayerPoints >= 100:
                            await buyItem(message, channel, gambleAmount, i)
                        else:
                            await channel.send("Not Enough Points")
        if "$use" in messageContent:
            #gambleAmount in this function takes the item to use instead of the gamble amount from $play
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
                    currentPlayer = playerDicts[i]
                    currentPlayerShuffles = int(currentPlayer["shuffles"])
                    if gambleAmount.lower() == "shuffle":
                        if currentPlayerShuffles > 0:
                            await useItem(message, channel, i, "shuffle")
                        else:
                            await channel.send("Not enough shuffles")
        #function call commands
        if messageContent == "$points":
            await showPoints(message, channel)
        if messageContent == "$inventory" or messageContent == "$inv":
            await showInventory(message, channel)
        if messageContent == "$shop":
            await showShop(channel)
        if messageContent == "$help":
            await showHelp(channel)
        
        if messageContent == "$reset:uiop19hjkl":
            #print("True")
            await resetFileData(message)

client.run(token)
