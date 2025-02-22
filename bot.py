import discord
import random
import os
from discord.ext import commands

chistes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Qué hace una abeja en el gimnasio? Zum-ba.",
    "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué le dice una iguana a su hermana gemela? Iguanita."
]
    
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/b ', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def jaja(ctx, name, count_heh = 5):
    await ctx.send(name + "se cayó al piso" + "jajaja" * count_heh)
    
@bot.command()
async def registrar_evento(ctx, nombre_evento: str, fecha: str, hora: str, ubicacion: str):
    await ctx.send(f'¡Evento registrado!\nNombre del evento: {nombre_evento}\nFecha: {fecha}\nHora: {hora}\nUbicación: {ubicacion}')
    
@bot.command()
async def chiste(ctx):
    chiste_aleatorio = random.choice(chistes)
    await ctx.send(chiste_aleatorio)

@bot.command()
async def m1(ctx):
    with open('C5/img/m1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def m2(ctx):
    with open('C5/img/m2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
   
@bot.command()
async def m3(ctx):
    with open('C5/img/m3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def m4(ctx):
    with open('C5/img/m4.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



@bot.command()
async def showimg(ctx):
    # Obtener la lista de imágenes
    listaimg = os.listdir('C5/img')
    # Enviar la lista de imágenes al usuario
    await ctx.send(f'Imágenes disponibles: {", ".join(listaimg)}\nPor favor, escribe el nombre de la imagen que deseas ver (incluyendo la extensión).')

@bot.command()
async def mostrar_imagen(ctx, nombre_imagen: str):
    # Construir la ruta de la imagen
    ruta_imagen = os.path.join('C5/img', nombre_imagen)
    
    # Verificar si la imagen existe
    if os.path.isfile(ruta_imagen):
        with open(ruta_imagen, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send(f'No se encontró la imagen: {nombre_imagen}. Asegúrate de que el nombre sea correcto y que incluya la extensión.')



carpetas_permitidas = ['minecraft', 'programacion', 'fifa', 'colegio']

# Comando para listar las carpetas disponibles
@bot.command()
async def carpetas(ctx):
    await ctx.send(f'Carpetas disponibles: {", ".join(carpetas_permitidas)}')

# Comando para mostrar una imagen aleatoria de la carpeta especificada
@bot.command()
async def imagen(ctx, nombre_carpeta: str):
    if nombre_carpeta in carpetas_permitidas:
        ruta_carpeta = os.path.join('C5', nombre_carpeta)
        
        if os.path.isdir(ruta_carpeta):
            imagenes = [img for img in os.listdir(ruta_carpeta) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            
            if imagenes:
                imagen_aleatoria = random.choice(imagenes)
                ruta_imagen = os.path.join(ruta_carpeta, imagen_aleatoria)
                with open(ruta_imagen, 'rb') as f:
                    await ctx.send(file=discord.File(f))
            else:
                await ctx.send(f'No hay imágenes en la carpeta: {nombre_carpeta}.')
        else:
            await ctx.send(f'La carpeta "{nombre_carpeta}" no existe.')
    else:
        await ctx.send(f'La carpeta "{nombre_carpeta}" no está permitida. Usa uno de los siguientes nombres: {", ".join(carpetas_permitidas)}.')

@bot.command()
async def b_ambiental(ctx):
    n = str (random.randint(1,3))
    ruta_img = f'C6/ambiental/b{n}.png'
    with open(ruta_img, 'rb') as f:
        await ctx.send(file=discord.File(f))
    
@bot.command()
async def m_ambiental(ctx):
    n = str (random.randint(1,3))
    ruta_img = f'C6/ambiental/m{n}.png'
    with open(ruta_img, 'rb') as f:
        await ctx.send(file=discord.File(f))
        
    
    
        
        

