import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5050))

# Receive public key from server
public_pem = client_socket.recv(1024)
server_public_key = serialization.load_pem_public_key(public_pem)

print("🔐 Received server public key.")

while True:
    msg = input("💬 You: ")

    # Encrypt message with server's public key
    encrypted_msg = server_public_key.encrypt(
        msg.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    client_socket.send(encrypted_msg)

    if msg.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()
    if reply.lower() == "exit":
        print("❌ Server ended the chat.")
        break

    print("📥 Server:", reply)

client_socket.close()
