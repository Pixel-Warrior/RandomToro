import os
import discord
from discord.ext import commands
from random import randint

bot = commands.Bot()


@bot.slash_command(name = "roll", description = "Rolling a number in a range (default is 1-20)")
async def self(
	ctx, 
	min:discord.Option(int, "minimal number", default = 1), 
	max:discord.Option(int, "maximal number", default = 20)
	):
	msg = ''
	if min >= max:
		msg = 'Incorrect numbers'
	else:
		msg = f'Your random number between *{min}* and *{max}* is ... **{randint(min, max)}**!'
	await ctx.respond(msg)

@bot.slash_command(name = "dice", description = "Rolling some dices")
async def self(
	ctx,
	throws: discord.Option(int, "how many times we will roll", default = 1),
	roll_type: discord.Option(str, "dice rolling type", default = "D6", choices = ["D6","D66","D666"])
	):
	total = 0
	dice_list = ""
		    
	roll_types = {
		'd6'   : 1,
		'd66'  : 2,
		'd666' : 3,
	}
    
	for i in range(throws):
		number = 0
		dices = ""
		for digit in range(roll_types[roll_type.lower()]):
			random = randint(1, 6)
			number += random * (10 ** digit)
			emoji = discord.utils.get(bot.emojis, name=f"dice_{random}")
			dices = str(emoji) + " " + dices
		dice_list += f"{dices}\n \n"
		total += number
	await ctx.respond(f"""Your dice(s):

{dice_list[:-2]}
Total is: **{total}**
""")

bot.run(os.getenv("TOKEN"))
