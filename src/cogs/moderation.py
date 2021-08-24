import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        elif isinstance(error, commands.BadArgument):
            return await ctx.send("Укажите верные аргументы")
        
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(f"У вас недостаточно прав: {','.join(error.missing_perms)}")
        
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"У меня недостаточно прав: {','.join(error.missing_perms)}")

    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    @commands.command()
    async def clear(self, ctx, amount:int):
        messages = await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f"{len(messages)} сообщений было очищено")


def setup(bot):
    bot.add_cog(Moderation(bot = bot))