import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix="instinct!", description="Survival Is Key.")

@bot.event
async def on_ready():
  print("REX_101 is now online, and ready to wreck havoc. >:D")

@bot.command()
async def introduction(ctx, param):
    await ctx.send("RAWR! BEEP-BOOP-BEEP-BOOP. Hello there human! I am REX_101! The security and interigations bot for this server! :sungalsses:".format(param))
    await ctx.send("I hope we can get along nicely :smiley:")
    await ctx.send(":thinking: **What am I?** I am the bot from the sole-purpose of the Roblox gaming company Instinct Survivial™!".format(param))
    await ctx.send(":scream: **Can I be in your server?** No, not at the moment, Uncle Endy says I am in Early-stage development, which means...".format(param))
    await ctx.send(":warning: **COMPUTING...** ".format(param))
    await ctx.send("Nope! Not just yet c;".format(param))
    await ctx.send("Well I hope that has answered some of your non-dino brain questions! If you require further assitónce with my commands, a list of them, or further FAQ's, run \"instinct!help\":sparkles: :tada: ".format(param))
    await ctx.send("Most importantly, always remember: **Survival is key.** :grinning:".format(param))

bot.run(os.environ['TOKEN'])
