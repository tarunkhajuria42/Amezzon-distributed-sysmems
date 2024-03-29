import random
import bcrypt

class UserService:
    def __init__(self):
        return

    def generate_hash(self):
        return random.getrandbits(128)

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def check_password(self, password, hash):
        return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
