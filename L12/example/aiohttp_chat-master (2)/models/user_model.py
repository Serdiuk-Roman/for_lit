from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256 as sha256
from chat.core.mongo_db import super_db


class User():

    def __init__(self, name, password, **kw):
        self.collection = super_db['users']
        self.name = name
        self.password = password

    async def generate_hash(self, password):
        return sha256.hash(password)

    async def verify_hash(self, password, hash):
        return sha256.verify(password, hash)

    async def check_password(self):
        user = await self.collection.find_one({'name': self.name})
        return await self.verify_hash(self.password, user['password'])

    async def check_user(self, **kw):
        return await self.collection.find_one({'name': self.name})

    async def get_name(self, **kw):
        return self.name

    async def create_user(self, **kw):
        user = await self.check_user()
        if not user:
            result = await self.collection.insert({ 'name': self.name, 'password': await self.generate_hash(self.password)})
            return True
        else:
            return False

