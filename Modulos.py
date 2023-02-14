import discord
from discord import ui
from discord.ui import Select, View
import aiosqlite

class Pais:
    def __init__(self,nome,tag_presidente,tag_general):
        self.nome = nome
        self.tag_presidente = tag_presidente
        self.tag_general = tag_general


Alemanha = Pais("Alemanha","P Alemanha","G Alemanha")
USA = Pais("Estados Unidos","P USA","G USA")
GBretanha = Pais("Grã Bretanha","P GBretanha","G GBretanha")
Japao = Pais("Japão","P Japao","G Japao")
Italia = Pais("Italia","P Italia","G Italia")
Suecia = Pais("Suécia","P Suecia","G Suecia")
Franca = Pais("França","P Franca","G Franca")
Sovietica = Pais("União Soviética","P Sovietica","G Sovietica")
China = Pais("China","P China","G China")
Israel = Pais("Israel","P Israel","G Israel")

async def tag(tag_pais,interaction):
    tag_presidente = discord.utils.get(interaction.user.guild.roles, name='Presidente')
    tag_presidente_pais = discord.utils.get(interaction.user.guild.roles, name=tag_pais)
    tag_p = discord.utils.get(interaction.user.guild.roles, name="P")
        
    if tag_presidente in interaction.user.roles:
        await interaction.user.add_roles(tag_presidente_pais)
        await interaction.user.add_roles(tag_p)
        await interaction.user.remove_roles(tag_presidente)

async def dar_tag(nome_pais,interaction):
    #SWITCH PAISES
    match nome_pais:

        case Alemanha.nome:
           await tag(Alemanha.tag_presidente,interaction)
        case USA.nome:
            await tag(USA.tag_presidente,interaction)
        case GBretanha.nome:
            await tag(GBretanha.tag_presidente,interaction)
        case Japao.nome:
            await tag(Japao.tag_presidente,interaction)
        case Italia.nome:
            await tag(Italia.tag_presidente,interaction)
        case Suecia.nome:
            await tag(Suecia.tag_presidente,interaction)
        case Franca.nome:
            await tag(Franca.tag_presidente,interaction)
        case Sovietica.nome:
            await tag(Sovietica.tag_presidente,interaction)
        case China.nome:
            await tag(China.tag_presidente,interaction)
        case Israel.nome:
            await tag(Israel.tag_presidente,interaction)

# async def dar_tag():


########################################  BOTÕES ###########################################################

## CADASTRO DE FUNCIONARIOS

class BtGneral(View):
    def __init__(self,p):
        self.p = p
    @discord.ui.button(label="Alistar-se")
    async def test(self,interaction: discord.Interaction,Button:discord.ui.Button):
        async with aiosqlite.connect('main.db') as db:
            async with db.cursor() as cursor:
                
                await cursor.execute(f"UPDATE paises SET general = '{interaction.user.display_name}' WHERE pais = '{self.p}'")
            
            await db.commit()
        await interaction.response.send_message("opagangnanstar",delete_after=5.0)
        await interaction.message.delete()

class BtSdd(View):
    @discord.ui.button(label="Alistar-se")
    async def test(self,interaction: discord.Interaction,Button:discord.ui.Button):
        await interaction.response.send_message("Sdd cabeça de pica",delete_after=5.0)
        await interaction.message.delete()

