import discord
from functions import *
from .closeButton import closeButton
from discord.ui import TextInput, Modal

class aboutModal(Modal):
    def __init__(self) -> None:
        super().__init__(
            title="Raison"
        )

        reason = TextInput(
            min_length=1,
            required=True,
            label="Raison:",
            max_length=2000,
            style=discord.TextStyle.long,
            placeholder="Décrivez votre situation.",
        )
        self.add_item(reason)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        config = load_json()
        
        category = discord.utils.get(interaction.guild.channels, id=config['tickets']['category'])

        if category == None:
            return await interaction.response.send_message("La catégorie d'ouverture des tickets est invalide. Merci de contacter un membre du staff.", ephemeral=True)
        
        try:
            channel = await category.create_text_channel(name=f"ticket-{interaction.user.name}", )
        except Exception:
            return await interaction.response.send_message("Je n'ai pas les permissions pour crée le salon du ticket. Merci de contacter un membre du staff", ephemeral=True)
        
        await channel.set_permissions(interaction.guild.default_role, read_messages=False)
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True, embed_links=True, attach_files=True, use_external_emojis=True)        

        embed = discord.Embed(
            title=f"`⚙️`・Ticket de {interaction.user.name}",
            description=f"***Informations du ticket:***\n\n> **Ouvert Par:** {interaction.user.mention}\n> **Raison:** ```{self.children[0].value}```",
            color=embed_color()
        )
        embed.set_thumbnail(url=interaction.user.avatar)
        embed.set_footer(text=f'{time_now()} - Ticket Bot | Purity Team ')

        view = discord.ui.View(timeout=None)
        view.add_item(closeButton(interaction.user.id))

        await channel.send(embed=embed, view=view)

        await interaction.response.send_message(f"Votre ticket a bien été ouvert dans le channel {channel.mention}", ephemeral=True)