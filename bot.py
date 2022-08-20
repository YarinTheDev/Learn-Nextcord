import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

#### Please Turn Intents On 
token = ""###put your token here


intents = nextcord.Intents.default()
intents.members = True


### Creating Bot veritable
bot = commands.Bot(intents=intents)


#### bot event
@bot.event
async def on_ready():
    print("im Ready")
    
    
    
##### bot commands
@bot.slash_command(name="sd", description="sd")### name= Your Command Name, description= Your command description
async def name(interaction: Interaction):
    await interaction.response.send_message("Message")
#### embeds
@bot.slash_command(name="embed", description="sends embed")
async def embed(interaction: Interaction):
    embed=nextcord.Embed(title="embed Title", description="Embed Desc", color=nextcord.Colour.red)
    await interaction.response.send_message(embed=embed)




### reaction roles
@bot.slash_command(name="reaction", description="add reaction to message")
async def reaction(interaction: Interaction, role:nextcord.Role, channel: nextcord.TextChannel):
    msg = await channel.send("Reaction Role Message")
    await msg.add_reaction("🎉")
    @bot.event
    async def on_raw_reaction_add(payload):
        if payload.message_id == msg.id:
            member = payload.member
            await member.add_roles(role)
bot.run(token)
        
    
