import random
import hashlib, uuid


class UserServices:
    def __init__(self):
        self.salt = uuid.uuid4.hex
        return

    def generate_hash(self):
        return random.getrandbits(128)

    def hash_password(self, password):
        hashed_password = hashlib.sha512(password + self.salt).hexdigest()
        return hashed_password

    def get_salt(self):
        return self.salt

    def check_password(self, password, salt, hash):
        return hash == hashlib.sha512(password + salt).hexdigest()
