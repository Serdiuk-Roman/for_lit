from motor import motor_asyncio as ma
super_db = ma.AsyncIOMotorClient('mongodb://user322:user322@ds147420.mlab.com:47420/light_it_chat')["light_it_chat"]
