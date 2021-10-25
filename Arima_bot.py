import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$say'):
        input()

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$wish'):
        await message.channel.send('Happy Birthday, Divyika-san!!')

    if message.content.startswith('$confess'):
        await message.channel.send('Should I really ? RISHI LOVES DIVYIKA-SAN VERY MUCH!!!')

    if message.content.startswith('$comfort'):
        await message.channel.send('Ganbatte, Divyika-san!')

    if message.content.startswith('$thank you') or message.content.startswith('$thankyou'):
        await message.channel.send('YOU ARE MOST WELCOME, Divyika-san!')

    if message.content.startswith('$friends'):
        await message.channel.send('All bots are my friends and OFCOURSE YOU TOO, Divyika-san!')

    if message.content.startswith('$dconfess'):
        await message.channel.send('The truth is ...... DIVYIKA-SAN LOVES RISHI TOO')

    if message.content.startswith('$derogatory'):
        await message.channel.send("You are Rishi's little slut, Divyika-san.")

client.run('ODIwNTEwNjcxMDk1MzMyODgw.YE2OHA.ko7kd5_wYHXNG-yz8FaRoVwaRc0')
