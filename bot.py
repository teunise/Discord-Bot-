import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix=['!'], intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="GRUNTDIXIE#0001 (Dev)"))
    print("Bot Made by GRUNTDIXIE#0001")

@client.slash_command(
    name="slashtest",
    description="A test command (You can change it)",
    options=[
        {
            "name": "opt",
            "description": "The option",
            "type": 3,  # STRING
            "required": False,
            "choices": [
                {"name": "FirstChoice", "value": "Happy"},
                {"name": "SecondChoice", "value": "Sad :("}
            ]
        }
    ]
)
async def slashtest(ctx, opt: str = None):
    await ctx.respond(f"Okay! I'm setting your current mood to {opt} :p")
    await ctx.respond("Contact `GRUNTDIXIE#0001` to know more!\n\nJoin our discord at https://www.discord.gg/mEAsHndCxs")

# Replace 'your_token_here' with your actual bot token
token = "your_token_here"
client.run(token)