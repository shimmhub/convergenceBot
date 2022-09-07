import hikari
import lightbulb

plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

# Creating a singular /slash command
@plugin.command
@lightbulb.command('ping', 'says Pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

# Creating a function command
@plugin.command
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

def load(bot):
    bot.add_plugin(plugin)