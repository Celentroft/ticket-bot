import discord
from discord import app_commands
from discord.ext import commands
from functions import embed_color

class helpCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="help", description="Afficher le panel d'aide")
    async def helpcommand(self, interaction: discord.Interaction) -> None:
        
        embed = discord.Embed(
            title="`✨`・Panel d'aide",
            color=embed_color()
        )
        embed.add_field(name="`/setup-category`", value="*Configurer la categorie d'ouverture des tickets*", inline=False)
        embed.add_field(name="`/tickets-embed`", value="*Envoyer l'embed d'ouverture des tickets*", inline=False)
        embed.add_field(name="`/help`", value="*Afficher le panel d'aide (celui-ci)*", inline=False)
        embed.add_field(name="`/ping`", value="*Pong !*", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(helpCommand(bot))