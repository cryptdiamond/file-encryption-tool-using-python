from cryptography.fernet import Fernet
with open("secret.key", "rb") as key_file:
  key = key_file.read()
  fernet = Fernet(key)
  with open ("encrypted.txt", "rb") as file:
    encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open("derypted.txt", "wb") as decrypted_file:
      decrypted_file.write(decrypted)
      print("File decrypted successfully")
