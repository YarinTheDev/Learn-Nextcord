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
@bot.event
async def on_guild_channel_create(channel):
    guild = bot.get_guild(955063096450355290)
    channel1 = discord.utils.get(guild.channels, id=971736823397232670)
    embed = discord.Embed(
        title="New Channel Has Been Created!",
        description=f" Channel: `{str(channel.name)}`\n Channel Mention: <#{str(channel.id)}>",
        colour=discord.Colour.from_rgb(0, 85, 255)
    )
    embed.set_footer(text=f"{guild.name} | Channel System", icon_url=guild.icon_url)
    embed.set_author(name="Channel System", icon_url=guild.icon_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872450263171100692/955082464513126430/icon.png")
    await channel1.send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
    guild = bot.get_guild(955063096450355290)
    channel1 = discord.utils.get(guild.channels, id=971736823397232670)
    embed = discord.Embed(
        title="Channel Has Been Removed",
        description=f" Channel: `{str(channel.name)}`",
        colour=discord.Colour.from_rgb(252, 3, 32)
    )
    embed.set_footer(text=f"{guild.name} | Channel System", icon_url=guild.icon_url)
    embed.set_author(name="Channel System", icon_url=guild.icon_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872450263171100692/955082464513126430/icon.png")
    await channel1.send(embed=embed)
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id=971736823397232670)
    embed = discord.Embed(
        title="User Left The Server",
        description=f":icon: User: `{str(member)}`\n:icon: Mention: <@{str(member.id)}>",
        colour=discord.Colour.from_rgb(252, 3, 48)
    )
    embed.set_footer(text=f"{member.guild.name} | Leave System", icon_url=member.guild.icon_url)
    embed.set_author(name="Leave System", icon_url=member.guild.icon_url)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id=971736823397232670)
    embed = discord.Embed(
        title="User Left The Server",
        description=f":icon: User: `{str(member)}`\n:icon: Mention: <@{str(member.id)}>",
        colour=discord.Colour.from_rgb(252, 3, 48)
    )
    embed.set_footer(text=f"{member.guild.name} | Leave System", icon_url=member.guild.icon_url)
    embed.set_author(name="Leave System", icon_url=member.guild.icon_url)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
@bot.event
async def on_message_delete(message):
    channel = discord.utils.get(message.guild.channels, id=971736823397232670)
    embed = discord.Embed(
        title="New Message Has Been Deleted",
        description=f":icon: User: `{str(message.author)}`\n:icon: Channel: `{str(message.channel)}`\n:icon: Message: `{str(message.content)}`",
        colour=discord.Colour.from_rgb(0, 85, 255)
    )
    embed.set_footer(text=f"{message.guild.name} | Delete System", icon_url=message.guild.icon_url)
    embed.set_author(name="Delete System", icon_url=message.guild.icon_url)
    embed.set_thumbnail(url=message.author.avatar_url)
    if message.author.bot:
        pass
    else:
        await channel.send(embed=embed)



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
            
            
#### nextcord buttons
class ButtonName(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
    @nextcord.ui.button(label="Button Label", style=nextcord.ButtonStyle.grey)### Please Fill Out "Button Label" And Put Any color You Want in style
    async def dfdfdfd(self, button: nextcord.ui.Button ,interaction: Interaction):
        await interaction.response.send_message("ujrjrjfidijgdjgjgijdgijdij")
        self.value=True
@bot.slash_command(name="jamal")
async def jamal(interaction: Interaction):
    view = ButtonName()
    await interaction.response.send_message("What's Up?", view=view)
    if view.value == None:
        pass
    ### do whatever you want i usually pass
    else:
        pass
    ### do whatever you want i usually pass
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
@bot.command()
async def invites(ctx):

    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"**You have `{totalInvites}` invites !**")
@bot.slash_command(name="verify_setup", description="set verify")
async def verify_setup(interaction: Interaction):
    view = verifyB()
    embed = nextcord.Embed(title="__Verify System - Derei & Yarin Developers__", description="**Click The Button To Be Verified.**")
    await interaction.response.send_message(embed=embed, view=view)
bot.run(token)
        
    
