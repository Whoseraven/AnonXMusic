from pyrogram import Client
import config

app = Client("my_account", api_id=config.API_ID, api_hash=config.API_HASH)

app.run()
