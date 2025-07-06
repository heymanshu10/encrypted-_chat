import socket
import threading
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serialize public key to send to clients
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

def handle_client(client_socket, address):
    print(f"✅ Connected to {address}")
    client_socket.send(public_pem)  # Send public key to client

    while True:
        try:
            encrypted_msg = client_socket.recv(256)
            if not encrypted_msg:
                break

            # Decrypt message
            msg = private_key.decrypt(
                encrypted_msg,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ).decode()

            if msg.lower() == "exit":
                print(f"👋 Client {address} exited.")
                break

            print(f"📥 {address} (decrypted): {msg}")

            reply = input("💬 Your reply: ")
            client_socket.send(reply.encode())

            if reply.lower() == "exit":
                break

        except Exception as e:
            print(f"⚠️ Error with {address}: {e}")
            break

    client_socket.close()
    print(f"🔌 Connection closed for {address}")

# Start server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5050))
server_socket.listen()
print("🟢 RSA Server running on port 5050...")

while True:
    try:
        client_socket, address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
    except KeyboardInterrupt:
        print("🛑 Server shutting down.")
        server_socket.close()
        break
