import os

from cryptography.fernet import Fernet

import Secret

Codec = Fernet(Secret.Key)

import Output

print()

print('UserIDInput:', Codec.decrypt(Output.UserIDInput).decode())
print('PasswordInput:', Codec.decrypt(Output.PasswordInput).decode())
print('EMail:', Codec.decrypt(Output.EMail).decode())
print('Folder:', Codec.decrypt(Output.Folder).decode())
print('Path:', Codec.decrypt(Output.Path).decode())
