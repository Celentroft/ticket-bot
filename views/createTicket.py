import discord
from typing import Any
from discord.ui import Button
from .aboutModal import aboutModal

class createTicket(Button):
    def __init__(self) -> None:
        super().__init__(
            style=discord.ButtonStyle.blurple,
            label="Ticket",
            emoji="✨"
        )

    async def callback(self, interaction: discord.Interaction) -> Any:
        await interaction.response.send_modal(aboutModal())