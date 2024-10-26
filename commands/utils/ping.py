import discord
from discord import app_commands
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="ping", description="show bot latency")
    async def ping(self, interaction: discord.Interaction) -> None:
        return await interaction.response.send_message("Pong !", ephemeral=True)
    
async def setup(bot) -> None:
    await bot.add_cog(PingCommand(bot))