import hikari
import lightbulb

plugin = lightbulb.Plugin('Example')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

# Creating a group of /slash commands
@plugin.command
@lightbulb.command('group', 'This is a group.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

# Creating a sub-group of /slash commands
@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')

def load(bot):
    bot.add_plugin(plugin)