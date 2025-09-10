import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Magic 8 Ball responses (expanded with more variety and humor)
MAGIC_8_BALL_RESPONSES = [
    # Positive responses
    "🔮 It is certain",
    "🔮 It is decidedly so",
    "🔮 Without a doubt",
    "🔮 Yes definitely",
    "🔮 You may rely on it",
    "🔮 As I see it, yes",
    "🔮 Most likely",
    "🔮 Outlook good",
    "🔮 Yes",
    "🔮 Signs point to yes",
    "✨ Absolutely!",
    "⭐ The stars align in your favor",
    "🌟 Fortune smiles upon you",
    "💫 The universe says yes",
    "🎯 Bulls-eye! Go for it!",
    "🚀 Launch into action!",
    "🌈 Rainbow of possibilities ahead",
    "🔥 Hot prospects await",
    
    # Non-committal responses
    "🔮 Reply hazy, try again",
    "🔮 Ask again later",
    "🔮 Better not tell you now",
    "🔮 Cannot predict now",
    "🔮 Concentrate and ask again",
    "🌫️ The mists of time obscure the answer",
    "⏰ Time will tell",
    "🎲 The dice are still rolling",
    "🌊 The tides of fate are shifting",
    "🔄 The wheel of fortune spins",
    "💭 The answer lies within you",
    "🤔 Hmm, let me think about that...",
    "⚖️ The scales are perfectly balanced",
    
    # Negative responses
    "🔮 Don't count on it",
    "🔮 My reply is no",
    "🔮 My sources say no",
    "🔮 Outlook not so good",
    "🔮 Very doubtful",
    "❌ Not in this lifetime",
    "🚫 The path is blocked",
    "⛈️ Storm clouds gather",
    "🌑 The signs are dark",
    "💔 Sorry, but no",
    "🛑 Stop right there",
    "📉 Chances are slim",
    
    # Humorous "No Answer" responses
    "🤷 I'm just a magic 8 ball, not a miracle worker",
    "😴 The magic 8 ball is taking a nap",
    "🔋 Battery low, answer unclear",
    "📵 Magic signal not found",
    "🎭 The answer is behind a paywall",
    "🍕 Ask me after I finish this pizza",
    "🎪 The circus of fate is closed today",
    "🦄 Even unicorns don't know this one",
    "🎮 Error 404: Answer not found",
    "☕ I need more coffee to answer that",
    "🎨 The answer is a work of art in progress",
    "🔮 My crystal ball is in the shop",
    "🎪 The magic show is intermission",
    "🌮 Taco Tuesday has clouded my judgment",
    "🎯 That question is outside my target range",
    "🎪 The fortune teller union is on strike",
    "🎲 My dice rolled off the table",
    "🎭 That's above my pay grade",
    "🎪 The magic department is closed",
    "🔮 Ask your local wizard instead"
]

# Bot setup - Using minimal intents to avoid privileged intent requirements
intents = discord.Intents.default()
# Commenting out message_content intent to avoid privileged intent error
# intents.message_content = True  # Enable this in Discord Developer Portal if you want message content features
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready to answer your questions! 🔮')
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

# Slash command version (works without message content intent)
@bot.tree.command(name="8ball", description="Ask the Magic 8 Ball a question!")
async def magic_8_ball_slash(interaction: discord.Interaction, question: str):
    """
    Magic 8 Ball slash command - ask a question and get a mystical answer!
    """
    # Get random response
    response = random.choice(MAGIC_8_BALL_RESPONSES)
    
    # Create embed for better formatting
    embed = discord.Embed(
        title="🎱 Magic 8 Ball",
        color=0x800080  # Purple color
    )
    embed.add_field(name="❓ Question", value=question, inline=False)
    embed.add_field(name="🔮 Answer", value=response, inline=False)
    embed.set_footer(text=f"Asked by {interaction.user.display_name}")
    
    await interaction.response.send_message(embed=embed)

# Traditional command (requires message content intent)
@bot.command(name='8ball', aliases=['magic8ball', 'ask'])
async def magic_8_ball(ctx, *, question=None):
    """
    Magic 8 Ball command - ask a question and get a mystical answer!
    Usage: !8ball <your question>
    Note: This requires Message Content Intent to be enabled in Discord Developer Portal
    """
    if question is None:
        await ctx.send("🔮 **You must ask a question for the Magic 8 Ball to answer!**\n*Example: `!8ball Will I have a good day?`*\n*Or use the slash command: `/8ball question:Will I have a good day?`*")
        return
    
    # Get random response
    response = random.choice(MAGIC_8_BALL_RESPONSES)
    
    # Create embed for better formatting
    embed = discord.Embed(
        title="🎱 Magic 8 Ball",
        color=0x800080  # Purple color
    )
    embed.add_field(name="❓ Question", value=question, inline=False)
    embed.add_field(name="🔮 Answer", value=response, inline=False)
    embed.set_footer(text=f"Asked by {ctx.author.display_name}")
    
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # Don't respond to bot messages
    if message.author == bot.user:
        return
    
    # Check if bot is mentioned and message contains a question
    if bot.user in message.mentions and '?' in message.content:
        # Extract the question (remove the mention)
        question = message.content.replace(f'<@{bot.user.id}>', '').strip()
        
        # Get random response
        response = random.choice(MAGIC_8_BALL_RESPONSES)
        
        # Create embed
        embed = discord.Embed(
            title="🎱 Magic 8 Ball",
            color=0x800080
        )
        embed.add_field(name="❓ Question", value=question, inline=False)
        embed.add_field(name="🔮 Answer", value=response, inline=False)
        embed.set_footer(text=f"Asked by {message.author.display_name}")
        
        await message.channel.send(embed=embed)
    
    # Process commands
    await bot.process_commands(message)

@bot.tree.command(name="help", description="Show help information for the Magic 8 Ball bot")
async def help_magic_8_ball_slash(interaction: discord.Interaction):
    """
    Show help information for the Magic 8 Ball bot (slash command version)
    """
    embed = discord.Embed(
        title="🎱 Magic 8 Ball Bot Help",
        description="Ask the mystical Magic 8 Ball your yes/no questions!",
        color=0x800080
    )
    
    embed.add_field(
        name="📝 How to use:",
        value="• **Slash Command (Recommended):** `/8ball question:Your question here`\n• **Traditional Command:** `!8ball <question>` (requires special setup)\n• **Mention:** `@Magic8Ball Should I do this?` (requires special setup)",
        inline=False
    )
    
    embed.add_field(
        name="💡 Examples:",
        value="• `/8ball question:Will I pass my exam?`\n• `!8ball Should I go out tonight?`\n• `@Magic8Ball Will it rain today?`",
        inline=False
    )
    
    embed.add_field(
        name="🔮 Features:",
        value="• 20 classic Magic 8 Ball responses\n• Beautiful embed formatting\n• Slash commands (no special permissions needed)\n• Traditional commands (requires Message Content Intent)",
        inline=False
    )
    
    embed.add_field(
        name="⚙️ Setup Note:",
        value="Slash commands work immediately! Traditional commands require enabling 'Message Content Intent' in Discord Developer Portal.",
        inline=False
    )
    
    await interaction.response.send_message(embed=embed)

@bot.command(name='help_8ball')
async def help_magic_8_ball(ctx):
    """
    Show help information for the Magic 8 Ball bot (traditional command)
    """
    embed = discord.Embed(
        title="🎱 Magic 8 Ball Bot Help",
        description="Ask the mystical Magic 8 Ball your yes/no questions!",
        color=0x800080
    )
    
    embed.add_field(
        name="📝 How to use:",
        value="• **Slash Command (Recommended):** `/8ball question:Your question here`\n• **Traditional Command:** `!8ball <question>`\n• **Mention:** `@Magic8Ball Should I do this?`",
        inline=False
    )
    
    embed.add_field(
        name="💡 Examples:",
        value="• `/8ball question:Will I pass my exam?`\n• `!8ball Should I go out tonight?`\n• `@Magic8Ball Will it rain today?`",
        inline=False
    )
    
    embed.add_field(
        name="🔮 Features:",
        value="• 20 classic Magic 8 Ball responses\n• Beautiful embed formatting\n• Slash commands (no special permissions needed)\n• Traditional commands and mentions",
        inline=False
    )
    
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore unknown commands
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("🔮 **Please ask a question!** Use `!help_8ball` for more info.")
    else:
        print(f'Error: {error}')

if __name__ == '__main__':
    # Get bot token from environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        bot.run(token)
    else:
        print("❌ Error: DISCORD_BOT_TOKEN not found in environment variables!")
        print("Please create a .env file with your bot token.")