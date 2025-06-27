import discord_bot
from discord.ext import commands
import os
import random

TOKEN = "TU_TOKEN_ACA"

intents = discord.Intents.default()
intents.menssage_content = True

bot = commands.Bot(commnd_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def saludo(ctx):
    await ctx.send("Hola!, Soy tu primer bot")

@bot.command()
async def hora(ctx):
    from datetime import datetime
    ahora = datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"La hora actual es {ahora}")

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"el dado toco en {numero}")

@bot.command()
async def tarea(ctx, *, texto):
    with open("tareas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{texto}\n")
    await ctx.send("Tarea guardad correctamente.")

preguntas = [
    {"pregunta": "Cual es la capital de Francia", "respuesta": "paris"},
    {"pregunta": "Cuanto es 5 x 6?", "respuesta": "30"},
    {"pregunta": "Quien escribio 'El Quijote'?", "respuesta":"cervantes"}
]

@bot.command()
async def quiz(ctx):
    pregunta = random.choice(preguntas)
    await ctx.send(f"{pregunta['pregunta']}")

    def check(mensaje):
        return (
            mensaje.author == ctx.author and
            mensaje.channel == ctx.channel
        )
    
    try:
        respuesta = await bot.wait_for("menssage", check=check, timeout=15)
        if respuesta.content.lower() == pregunta["respuesta"]:
            await ctx.send("Correcto")
        else:
            await ctx.send(f"Incorrecto. La respuesta era: {pregunta['respuesta']}")
    except:
        await ctx.send("Tiempo agotado")

bot.run(TOKEN)

