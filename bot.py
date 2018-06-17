import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="instinct!", description="Survival Is Key.")

@bot.command()
async def introduction(ctx):
    await ctx.send("RAWR! BEEP-BOOP-BEEP-BOOP. Hello there human! I am REX_101! The security and interigations bot for this server! :sungalsses:")
    await ctx.send("I hope we can get along nicely :smiley:")
    await ctx.send(":thinking: **What am I?** I am the bot from the sole-purpose of the Roblox gaming company Instinct Survivial™!")
    await ctx.send(":scream: **Can I be in your server?** No, not at the moment, Uncle Endy says I am in Early-stage development, which means...")
    await ctx.send(":warning: **COMPUTING...** ")
    await ctx.send("Nope! Not just yet c;")
    await ctx.send("Well I hope that has answered some of your non-dino brain questions! If you require further assitónce with my commands, a list of them, or further FAQ's, run \"instinct!help\":sparkles: :tada: ")
    await ctx.send("Most importantly, always remember: **Survival is key.** :grinning:")

bot.run("TOKEN")
