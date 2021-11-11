import discord
import config
import asyncio
from discord.ext import commands
from discord_components import *
from discord_components import DiscordComponents, ComponentsBot, Button
from discord_buttons_plugin import *
from discord import utils

bot = discord.Client()
bot = commands.Bot(command_prefix='!')
bot = ComponentsBot(command_prefix="!")
buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("I WORK")

#Role
@bot.command()
async def role(ctx):
    buttonsArray = [
        Button(label="Gamer role", custom_id="first"),
        Button(label="POLUPOKER role", custom_id="second"),
        Button(label="ЧЕПУШИЛО role", custom_id="third")
    ]
    await ctx.send(
        content=("Click on the button to select a role"),
        components = buttonsArray
    )



@buttons.click
async def first(ctx):
    member = ctx.member
    print(member.id)
    role = discord.utils.get(ctx.guild.roles, name="Гейме")
    user = await ctx.guild.fetch_member(member.id)
    print(type(user))
    if len(user.roles) <= config.Max_roles_per_user:
        await user.add_roles(role)
        await ctx.reply(f"Roll added", flags=MessageFlags().EPHEMERAL)
    else:
        await ctx.reply(f"Too many roles already", flags=MessageFlags().EPHEMERAL)

@buttons.click
async def second(ctx):
    member = ctx.member
    print(member.id)
    role = discord.utils.get(ctx.guild.roles, name="Полупокер")
    user = await ctx.guild.fetch_member(member.id)
    print(type(user))
    if len(user.roles) <= config.Max_roles_per_user:
        await user.add_roles(role)
        await ctx.reply(f"Roll added", flags=MessageFlags().EPHEMERAL)
    else:
        await ctx.reply(f"Too many roles already", flags=MessageFlags().EPHEMERAL)

@buttons.click
async def third(ctx):
    member = ctx.member
    print(member.id)
    role = discord.utils.get(ctx.guild.roles, name="чепушило")
    user = await ctx.guild.fetch_member(member.id)
    print(type(user))
    if len(user.roles) <= config.Max_roles_per_user:
        await user.add_roles(role)
        await ctx.reply(f"Roll added", flags=MessageFlags().EPHEMERAL)
    else:
        await ctx.reply(f"Too many roles already", flags=MessageFlags().EPHEMERAL)

#Rule
@bot.command()
async def rule(ctx):
    buttonsRules1 = [
        Button(label="Next list", custom_id="ListRules1")
    ]
    await ctx.send(
        content=(config.TextRules1),
        components = buttonsRules1)

@buttons.click
async def ListRules1(ctx):
    print("ListRules1 work")

#Help
#1 page
@bot.command()
async def Help(ctx):
    buttonsHelp = [
        Button(label="Next list", custom_id="ListHelpNext1")
    ]
    await ctx.send(
        content=( config.TextHelp1 ),
        components = buttonsHelp)

#2 page
@buttons.click
async def ListHelpNext1(ctx):
    buttonsHelp1 = [
        Button(label="Past list", custom_id="ListHelpPast1"),
        Button(label="Next list", custom_id="ListHelpNext2")
    ]
    await ctx.message.edit(content=config.TextHelp2,
                           components=buttonsHelp1)

#3 page
@buttons.click
async def ListHelpNext2(ctx):
    buttonsHelp2 = [
        Button(label="Past list", custom_id="ListHelpPast2"),
        Button(label="Next list", custom_id="ListHelpNext3")
    ]
    await ctx.message.edit(content=config.TextHelp3,
                           components=buttonsHelp2)

#4 page
@buttons.click
async def ListHelpNext3(ctx):
    buttonsHelp3 = [
        Button(label="Past list", custom_id="ListHelpPast4")
    ]
    await ctx.message.edit(content=config.TextHelp4,
                           components=buttonsHelp3)

@buttons.click
async def ListHelpPast1(ctx):
    buttonsHelp = [
        Button(label="Next list", custom_id="ListHelpNext1")
    ]
    await ctx.message.edit(
        content=(config.TextHelp1),
        components=buttonsHelp)

@buttons.click
async def ListHelpPast2(ctx):
    buttonsHelp1 = [
        Button(label="Past list", custom_id="ListHelpPast1"),
        Button(label="Next list", custom_id="ListHelpNext2")
    ]
    await ctx.message.edit(
        content=(config.TextHelp2),
        components=buttonsHelp1)

@buttons.click
async def ListHelpPast3(ctx):
    buttonsHelp2 = [
        Button(label="Past list", custom_id="ListHelpPast2"),
        Button(label="Next list", custom_id="ListHelpNext3")
    ]
    await ctx.message.edit(
        content=(config.TextHelp2),
        components=buttonsHelp2)

@buttons.click
async def ListHelpPast4(ctx):
    buttonsHelp2 = [
        Button(label="Past list", custom_id="ListHelpPast3"),
        Button(label="Next list", custom_id="ListHelpNext4")
    ]
    await ctx.message.edit(
        content=(config.TextHelp3),
        components=buttonsHelp2)

@commands.has_permissions(administrator=True)
@bot.command()
async def clear(ctx, number: int):
  await ctx.channel.purge(limit=number)

bot.run(config.token)