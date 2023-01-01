import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

Password = b'FLAME'
 
SALT = os.urandom(16)

KDF = PBKDF2HMAC(
    algorithm = hashes.SHA256(),
    length = 32,
    salt = SALT,
    iterations = 999999,
)

Key = base64.urlsafe_b64encode(KDF.derive(Password))

File = open('Secret.py', 'w')
File.write("Key = b'" + Key.decode("utf-8") + "'")
File.close()

import Secret

Codec = Fernet(Secret.Key)

File = open('Output.py', 'w')

import Input

File.write("UserIDInput = b'" + Codec.encrypt(Input.UserIDInput.encode()).decode("utf-8") + "'")
File.write('\n')
File.write("PasswordInput = b'" + Codec.encrypt(Input.PasswordInput.encode()).decode("utf-8") + "'")
File.write('\n')
File.write("EMail = b'" + Codec.encrypt(Input.EMail.encode()).decode("utf-8") + "'")
File.write('\n')
File.write("Folder = b'" + Codec.encrypt(Input.Folder.encode()).decode("utf-8") + "'")
File.write('\n')
File.write("Path = b'" + Codec.encrypt(Input.Path.encode()).decode("utf-8") + "'")
File.write('\n')

File.close()
