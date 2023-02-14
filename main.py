import discord
from discord.ext import commands
from discord.utils import get
from discord.ui import Select, View
import aiosqlite
from Modulos import *
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
from discord import app_commands
activity = discord.Game(name="Pedras pra dentro do cachimbo com o guinas")
bot = commands.Bot(command_prefix='!', intents=intents, activity=activity, status=discord.Status.dnd)

PRESIDENTE="presidente"
GENERAL="general"
ADM="ADM"

@bot.event
async def on_ready():
    await bot.tree.sync()
    # async with aiosqlite.connect('main.db') as db:
    #         async with db.cursor() as cursor:
                
    #             await cursor.execute(f"UPDATE paises SET presidente = 'NA'")
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Alemanha","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Estados Unidos","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Grã Bretanha","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Japão","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Italia","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Suécia","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("França","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("União Soviética","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("China","NA","NA","0","0","0")')
            #     await cursor.execute('INSERT INTO paises (pais, presidente, general, porcentagem, industria, dinheiro) VALUES ("Israel","NA","NA","0","0","0")')
            # await db.commit()
    print("Graças a Deus")

@bot.tree.command(name="testar",description="Testes")
async def testar(interaction: discord.Interaction):
   pass

class Myselect(View):
    @discord.ui.select(
        placeholder="Escolha uma",
        options=[
            discord.SelectOption(label="M2A4",value="1", description="Blindado Leve",emoji="<:blindado_leve:1060750065196597329>"),
            discord.SelectOption(label="Meu cacete",value="2", description="Isto é meu cacete"),
            discord.SelectOption(label="Meu pinto",value="3", description="Isto é meu pinto"),
        ]
    )    
    async def select_callback(self,interaction,select):
        select.disabled=True
        if select.values[0] == "1":
            em = discord.Embed()
            em.set_author(name="Calvasso")
            em.add_field(name="Calvasso de cria",value="Inscreva-se na minha pica",inline=False)
            await interaction.response.edit_message(embed=em)
        if select.values[0] == "2":
            await interaction.response.edit_message(content="Mensagem editada e va se fuder vu")
        if select.values[0] == "3":
            await interaction.response.send_message("Va capina um lote negão")      


class CadastroFuncionario(View):
    @discord.ui.select(
        placeholder="Escolha um cargo",
        options=[
            discord.SelectOption(label="General",value="1", description="Encarregado pela construção dos recursos de um País",emoji="<:gn:1062284189124284507>"),
            discord.SelectOption(label="Soldado",value="2", description="Tropa de gado pontudo que só a porra",emoji="<:sd:1062284187442356254>"),
            
        ]
    )    
    async def select_callback(self,interaction,select):
        async with aiosqlite.connect('main.db') as db:
            select.disabled=True
            async with db.cursor as cursor:
                await cursor.execute(f'SELECT pais FROM paises WHERE presidente = "{interaction.user.display_name}')
                p = await cursor.fetchone()
                if select.values[0] == "1":
                    await interaction.response.send_message("Clique abaixo para se alistar como General",view=BtGneral(p))
                elif select.values[0] == "2":
                    await interaction.response.send_message("Clique abaixo para se alistar como Soldado",view=BtSdd(p))
            await db.commit()

class CadastroPresidente(View):
    @discord.ui.select(
        placeholder="Escolha um País",
        options=[
            discord.SelectOption(label="Alemanha",value="1",emoji="🇩🇪"),
            discord.SelectOption(label="Estados Unidos",value="2", emoji="🇺🇲"),
            discord.SelectOption(label="Grã Bretanha",value="3", emoji="🇬🇧"),
            discord.SelectOption(label="Japão",value="4", emoji="🇯🇵"),
            discord.SelectOption(label="Italia",value="5", emoji="🇮🇹"),
            discord.SelectOption(label="Suécia",value="6", emoji="🇸🇪"),
            discord.SelectOption(label="França",value="7", emoji="🇫🇷"),
            discord.SelectOption(label="União Soviética",value="8", emoji="<:USSR4:1060845723740020786>"),
            discord.SelectOption(label="China",value="9", emoji="🇨🇳"),
            discord.SelectOption(label="Israel",value="10", emoji="🇮🇱"),
        ]
        
    )
    
        
              
    async def select_callback(self,interaction,select):
        select.disabled=True
        
        if select.values[0] == "1":
            await cadastrar_presidente(interaction,"Alemanha",interaction.user.display_name)            
            
        elif select.values[0] == "2":
            await cadastrar_presidente(interaction,"Estados Unidos",interaction.user.display_name)
        
        elif select.values[0] == "3":
            await cadastrar_presidente(interaction,"Grã Bretanha",interaction.user.display_name)
                
        elif select.values[0] == "4":
            await cadastrar_presidente(interaction,"Japão",interaction.user.display_name)
                
        elif select.values[0] == "5":
            await cadastrar_presidente(interaction,"Italia",interaction.user.display_name)
                
        elif select.values[0] == "6":
            await cadastrar_presidente(interaction,"Suécia",interaction.user.display_name)
                
        elif select.values[0] == "7":
            await cadastrar_presidente(interaction,"França",interaction.user.display_name)
                
        elif select.values[0] == "8":
            await cadastrar_presidente(interaction,"União Soviética",interaction.user.display_name)
                
        elif select.values[0] == "9":
            await cadastrar_presidente(interaction,"China",interaction.user.display_name)
                
        elif select.values[0] == "10":
            await cadastrar_presidente(interaction,"Israel",interaction.user.display_name)
                

@bot.tree.command(name="pais",description="Use no canal #### para colonizar seu País")
async def pais(interaction: discord.Integration):
    role = discord.utils.get(interaction.user.guild.roles, name='Presidente')
    if role in interaction.user.roles:

        if interaction.channel.name == "colonizar":
            view = CadastroPresidente()
            await interaction.response.send_message("Ola", view=view,delete_after=10.0, ephemeral=True) ######################## AUTO DELETE TIMER ######################
            # await ctx.message.delete()
        else:
            await interaction.response.send_message("Este comando só funciona no canal colonizar",delete_after=5.0, ephemeral=True)    

    else:
        await interaction.response.send_message("Você não tem permissão para dar este comando!",delete_after=5.0, ephemeral=True)    

@bot.tree.command(name="recrutar",description="Usado por um presidente para recrutar um general ou soldados")
async def recrutar(interaction: discord.Integration):
    role = discord.utils.get(interaction.user.guild.roles, name="P")
    if role in interaction.user.roles:
        view = CadastroFuncionario()
        await interaction.response.send_message("Ola", view=view,delete_after=10.0,ephemeral=True)

    else:
        await interaction.response.send_message("Você não tem permissão para dar este comando!",delete_after=5.0, ephemeral=True) 

@pais.error 
async def help_mod_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.message.delete()
        await ctx.send(f"{ctx.author.display_name} Você não tem a tag de presidente!",delete_after=5.0)

async def cadastrar_presidente(interaction,pais,presidente):
    async with aiosqlite.connect('main.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute(f'SELECT * FROM paises WHERE presidente = "{presidente}";')
                data = await cursor.fetchone()
                if data:
                    await interaction.user.send(f"Você ja é presidente do País {data[0]}, renuncie-o para trocar de País")
                    await interaction.response.send_message("Erro",delete_after=5.0, ephemeral=True)
                    

                else:
                    await cursor.execute(f'SELECT * FROM paises WHERE pais = "{pais}";')
                    data = await cursor.fetchone()
                    if data:
                        if str(data[1]) == "NA":
                            await cursor.execute(f"UPDATE paises SET presidente = '{presidente}' WHERE pais = '{pais}';")
                            # DAR A TAG, FUNÇÃO IMPORTADA DE MODULOS.PY
                            await dar_tag(pais,interaction)
                            await interaction.user.send(f"Parabens {presidente} Agora voce é o presidente do País {pais}")
                            await interaction.response.send_message("Concluido", delete_after=5.0, ephemeral=True)
                            
                            # await interaction.channel.purge(limit=2)
                        else:
                            em = discord.Embed()
                            em.set_author(name=f"{presidente}")
                            em.add_field(name="Este País ja tem dono",value="Escolha outro País",inline=False)
                            await interaction.response.send_message(embed=em,delete_after=5.0, ephemeral=True)
                            # await interaction.channel.purge(limit=2)
                            # await interaction.user.send("Este País ja tem dono, escolha outro!")   
                            
                await db.commit()





bot.run('MTA1OTk3NTkyNzUzMjA5NzYwNg.G8fRz9.ByNOYYxmVN2M4cD5B9fHQsexf1wM4LAkFfNcpY')