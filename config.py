from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25666163")
    API_HASH = environ.get("API_HASH", "74dbdbac7abcf0e1f7af1295eaf7a338")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6846150351:AAFXxlIiTPBQuvZ8u37H2e6grZ7nQYmmsRw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://forward-bot.qgqremp.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7220533955').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
