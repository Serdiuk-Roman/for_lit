from bson.objectid import ObjectId
from chat.core.mongo_db import super_db


class Message():

    def __init__(self):
        self.collection = super_db['messages']

    def get_all(self):
        result = self.collection.find()
        return result.to_list(length=None)

    async def check_user(self, name):
        result = await self.collection.find_one({'name': name})
        return result

    async def message_create(self, name, text, time):
        await self.collection.insert({ 'name': name, 'text': text, 'time': time})
        return True


