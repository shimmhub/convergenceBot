import hikari
import lightbulb

bot = lightbulb.BotApp(token='MTAxNjg2MjEyNTU1NTE5NTk5Ng.GdRBqI.POsMcmAn08r-VDJdc4T6MuJsras_OQQst3y62o',
                       default_enabled_guilds=(1016864198497685564)
                       )

@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print('Bot has started!')

bot.load_extensions_from('./extensions')
bot.run()
