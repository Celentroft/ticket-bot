import json
import discord
from datetime import datetime
from typing import Dict, Any

def load_json() -> Dict[str, Any]:
    config = json.load(open("config.json", 'r'))
    return config

def embed_color() -> int:
    config = load_json()
    return int(config['color'], 16)

def time_now() -> str:
    now = datetime.now().strftime("%H:%M:%S")
    return f"[{now}]"

async def unauthorized(interaction: discord.Interaction) -> None:
    embed = discord.Embed(
        title="`❌`・Commande non autorisée",
        description="*Vous n'avez pas la permission d'utiliser cette commande.*",
        color=embed_color()
    )
    return await interaction.response.send_message(embed=embed, ephemeral=True)