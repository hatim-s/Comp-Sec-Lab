from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Load the recipient's public key from the file
with open("public_key.pem", "rb") as public_key_file:
    recipient_public_key = serialization.load_pem_public_key(public_key_file.read())

# Message to be encrypted
message = b"This is a secret message."

# Encrypt the message using RSA
ciphertext = recipient_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Save the encrypted message (ciphertext) to a file
with open("encrypted_message.bin", "wb") as encrypted_file:
    encrypted_file.write(ciphertext)
