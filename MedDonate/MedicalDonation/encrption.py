from passlib.hash import pbkdf2_sha256


def store(password):
    hash = pbkdf2_sha256.encrypt(password,rounds=2000,salt_size=16)
    return hash


def verifyPassword(entered_Password, hash):
    return pbkdf2_sha256.verify(entered_Password ,hash)
