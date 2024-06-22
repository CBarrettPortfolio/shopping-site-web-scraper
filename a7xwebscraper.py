# Import necessary libraries
import discord
import asyncio
import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Define intents
intents = discord.Intents.default()

# Discord client
client = discord.Client(intents=intents)

# Function to send message via Discord
async def send_message():
    channel = client.get_channel(0)  # Replace with your channel ID
    role_id = 0  # Role ID to mention
    role = f'<@&{role_id}>'  # Tag the role using the role ID
    message = f"{role} New item added to the merchandise site: https://a7xworld.com/"
    await channel.send(message)

# Function to check the website for updates
async def check_website():
    url = 'https://a7xworld.com/'
    previous_items = set()

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='product')
        current_items = {item.find('h2').text.strip() for item in items}
        new_items = current_items - previous_items

        if new_items:
            await send_message()

        previous_items = current_items
        await asyncio.sleep(300)  # 300 seconds = 5 minutes

@client.event
async def on_ready():
    print('Logged in as', client.user)
    await check_website()

# GUI setup
root = tk.Tk()
root.title("Discord Bot Test Message")

# Function to send test message
def send_test_message():
    asyncio.create_task(send_message())

# Button to send test message
button = tk.Button(root, text="Send Test Message", command=send_test_message)
button.pack()

# Run the Tkinter main loop
async def run_tkinter():
    while True:
        root.update()
        await asyncio.sleep(0.1)

# Run the Tkinter and Discord bot together
async def main():
    asyncio.create_task(run_tkinter())
    await client.start('YOUR_DISCORD_BOT_TOKEN')

asyncio.run(main())
