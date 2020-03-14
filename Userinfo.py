import discord
from discord.ext import commands

class Userinfo (commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events

    #Commands

    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User ID: ", value=member.id)
        embed.add_field(name="Server Nickname: ", value=member.display_name)

        embed.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top Role: ", value=member.top_role.mention)

        await ctx.send(embed=embed)

    #Errors

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"I could not find that member, Please specify.")

def setup(client):
    client.add_cog(Userinfo(client))
