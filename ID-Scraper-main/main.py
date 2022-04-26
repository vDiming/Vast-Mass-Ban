import discum 
token = input("Please provide a token: ") 
guild = input("Please provide a guild id: ") 
channel = input("Please provide a channel id: ") 
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild, channel, startIndex=0, method='overlap',wait=1)
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

with open('result.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild).members:
        id = str(memberID)
        user = str(bot.gateway.session.guild(guild).members[memberID].get('username'))
        print(f'ID: {id}\n')
        file.write(f'{id}\n')