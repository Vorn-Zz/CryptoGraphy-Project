# utils.py
import os
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

ENC_DIR = "encrypted"
DEC_DIR = "decrypted"


def ensure_dirs():
    os.makedirs(ENC_DIR, exist_ok=True)
    os.makedirs(DEC_DIR, exist_ok=True)


def key_from_password(password, salt):
    return PBKDF2(password.encode(), salt, dkLen=32, count=200000,
                  hmac_hash_module=SHA256)


def encrypted_path(path):
    name = os.path.basename(path)
    return os.path.join(ENC_DIR, name + ".enc")


def decrypted_path(path):
    name = os.path.basename(path)
    if name.endswith(".enc"):
        name = name[:-4]
    return os.path.join(DEC_DIR, name)
