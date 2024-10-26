import discord
from discord.ext import commands

class messageCreate(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message) -> None:
        if self.bot.user.mention in message.content:
            await message.reply("Hey, tu peux m'utiliser avec les slash commandes ! Utilise /help pour t'aider.")

async def setup(bot) -> None:
    await bot.add_cog(messageCreate(bot))