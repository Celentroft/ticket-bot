import json
import discord
from functions import *
from discord import app_commands
from discord.ext import commands

class setupCategory(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="setup-category", description="Configurer la categorie d'ouverture des tickets")
    async def setupCategory(self, interaction: discord.Interaction, category: discord.CategoryChannel):
        config = load_json()
        if interaction.user.id != config['buyer']:
            return await unauthorized(interaction)
        
        config['tickets']['category'] = category.id
        json.dump(config, open("config.json", 'w'), indent=4)

        embed = discord.Embed(
            title="`✅`・Configuration",
            description=f"*La categorie **{category.name}** à bien été configurée comme la catégorie d'ouverture des tickets*",
            color=embed_color()
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot) -> None:
    await bot.add_cog(setupCategory(bot))