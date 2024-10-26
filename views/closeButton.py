from typing import Any
import discord
from functions import *
from discord.ui import Button
import asyncio

class closeButton(Button):
    def __init__(self, userId) -> None:
        self.userId = userId
        super().__init__(
            style=discord.ButtonStyle.red,
            label="Close",
            emoji='🛑'
        )

    async def callback(self, interaction: discord.Interaction) -> Any:
        if interaction.user.id != self.userId:
            return await interaction.response.send_message("Vous n'etes pas le membre qui as ouvert ce ticket.", ephemeral=True)
        
        await interaction.response.send_message("Le ticket sera supprimer dans 5 secondes", ephemeral=True)
        await asyncio.sleep(5)

        embed = discord.Embed(
            title="`✨`・Ticket fermé",
            description="*Votre ticket a bien été fermé.*",
            color=embed_color()
        )
        embed.set_footer(text=f"{time_now()} - Fermé par vous meme.")
        
        await interaction.user.send(embed=embed)
        await interaction.channel.delete(reason="Closed")

