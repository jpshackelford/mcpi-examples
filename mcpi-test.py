from dotenv import load_dotenv
from mcpi.minecraft import Minecraft

import os

# Load environment variables from .env file
load_dotenv()
MC_HOST = os.getenv('MINECRAFT_HOST')

# Connect to the minecraft server and say hello
print("connecting to server at " + MC_HOST + "...")
mc = Minecraft.create(MC_HOST, 4711)
mc.postToChat("Hello Minecraft World")
