# Import necessary libraries
import discord
from discord import app_commands
import aiohttp
import asyncio

# Configuration
TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your actual bot token
API_URL = 'https://talkomatic.co/rooms'  # URL of the Talkomatic API

# Custom Discord client class
class TalkomaticBot(discord.Client):
    def __init__(self):
        # Initialize the client with default intents
        super().__init__(intents=discord.Intents.default())
        # Create a command tree for slash commands
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync the command tree with Discord
        await self.tree.sync()

# Create an instance of the custom client
client = TalkomaticBot()

# Function to fetch room data from the Talkomatic API
async def fetch_room_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                # If the request is successful, return the JSON data
                return await response.json()
            else:
                # If the request fails, raise an exception
                raise Exception(f"API request failed with status {response.status}")

# Function to update the bot's status periodically
async def update_status():
    while True:
        try:
            # Fetch the latest room data
            data = await fetch_room_data()
            rooms = data['rooms']
            # Calculate total rooms and users
            total_rooms = len(rooms)
            total_users = sum(room['current_people_count'] for room in rooms)
            
            # Update the bot's status with the current information
            status = f'{total_rooms} rooms | {total_users} users online'
            await client.change_presence(activity=discord.Game(name=status))
        except Exception as e:
            # If an error occurs, print it to the console
            print(f"Error updating status: {e}")
        # Wait for 10 seconds before the next update
        await asyncio.sleep(10)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Start the status update loop
    client.loop.create_task(update_status())

# Slash command to get overall Talkomatic stats
@client.tree.command(name="stats", description="Get overall Talkomatic stats")
async def stats(interaction: discord.Interaction):
    try:
        # Fetch the latest room data
        data = await fetch_room_data()
        rooms = data['rooms']
        
        # Calculate total rooms and users
        total_rooms = len(rooms)
        total_users = sum(room['current_people_count'] for room in rooms)
        
        # Create an embed to display the stats
        embed = discord.Embed(title="Talkomatic Overall Stats", color=discord.Color.blue())
        embed.add_field(name="Total Rooms", value=total_rooms, inline=False)
        embed.add_field(name="Total Users Online", value=total_users, inline=False)
        
        # Send the embed as a response to the interaction
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        # If an error occurs, send an error message
        await interaction.response.send_message(f"Error fetching stats: {e}", ephemeral=True)

# Slash command to get detailed information about Talkomatic rooms
@client.tree.command(name="rooms", description="Get detailed information about Talkomatic rooms")
async def rooms(interaction: discord.Interaction):
    try:
        # Fetch the latest room data
        data = await fetch_room_data()
        rooms = data['rooms']
        
        # Create an embed to display the room information
        embed = discord.Embed(title="Talkomatic Rooms", color=discord.Color.green())
        
        # Add each room's information to the embed
        for room in rooms:
            room_info = f"{room['current_people_count']}/{room['max_people_count']} users"
            embed.add_field(name=f"{room['room_name']} (ID: {room['room_id']})", value=room_info, inline=False)
        
        # If there are no rooms, add a message to the embed
        if not rooms:
            embed.description = "No rooms are currently available."
        
        # Send the embed as a response to the interaction
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        # If an error occurs, send an error message
        await interaction.response.send_message(f"Error fetching room data: {e}", ephemeral=True)

# Run the bot
client.run(TOKEN)
