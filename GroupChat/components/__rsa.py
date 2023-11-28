from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Serialize and save the private key to a file
with open("private_key.pem", "wb") as private_key_file:
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    private_key_file.write(private_key_pem)

# Get the corresponding public key
public_key = private_key.public_key()

# Serialize and save the public key to a file
with open("public_key.pem", "wb") as public_key_file:
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    public_key_file.write(public_key_pem)

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


# Load the recipient's private key from the file
with open("private_key.pem", "rb") as private_key_file:
    recipient_private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=None,  # No password protection
    )

# Load the encrypted message from the file
with open("encrypted_message.bin", "rb") as encrypted_file:
    ciphertext = encrypted_file.read()

# Decrypt the message using the private key
decrypted_message = recipient_private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Print the decrypted message
print("Decrypted Message:", decrypted_message.decode("utf-8"))
