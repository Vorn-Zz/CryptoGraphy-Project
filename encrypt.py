# encrypt.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from utils import key_from_password


def encrypt_file(input_path, output_path, password):
    data = open(input_path, "rb").read()

    salt = get_random_bytes(16)
    key = key_from_password(password, salt)

    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(output_path, "wb") as f:
        f.write(salt + cipher.nonce + tag + ciphertext)
