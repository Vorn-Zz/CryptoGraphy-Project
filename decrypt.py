# decrypt.py
from Crypto.Cipher import AES
from utils import key_from_password


def decrypt_file(input_path, output_path, password):
    data = open(input_path, "rb").read()

    salt = data[:16]
    nonce = data[16:32]
    tag = data[32:48]
    ciphertext = data[48:]

    key = key_from_password(password, salt)

    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        return False

    open(output_path, "wb").write(plaintext)
    return True
