import discord
from discord import app_commands
from discord.ext import commands
from functions import *
from views.createTicket import createTicket

class ticketsEmbed(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="tickets-embed", description="Envoyer l'embed de ticket")
    async def ticketsEmbed(self, interaction: discord.Interaction) -> None:
        config = load_json()
        
        if interaction.user.id != config['buyer']:
            return await unauthorized(interaction)
        
        embed = discord.Embed(
            title=f"`⚙️`・{interaction.guild.name} tickets",
            description="*Utilisez les boutons ci-dessous pour créer un ticket.*",
            color=embed_color()
        )
        embed.set_footer(text="Merci de ne pas ouvrir des tickets inutilement.")

        view = discord.ui.View(timeout=None)
        view.add_item(createTicket())
        
        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot) -> None:
    await bot.add_cog(ticketsEmbed(bot))