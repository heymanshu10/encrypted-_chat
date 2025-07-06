# RSA encrypted Chat Application

This project demonstrates a simple RSA-based encrypted communication system, where a server and multiple clients can securely exchange messages. It uses RSA public-key cryptography, with support for PEM format keys and a secure public exponent (65537).

---
# HOW TO RUN IT
1. INSTALL THE REQUIRED CRYPTOGRAPHY LIBRARY
2.RUN THE SERVER ON ONE TERMINAL
3.RUN MULTIPLE CLIENTS ON OTHER TERMINALS

# FEATURES
RSA Encryption: Messages are securely encrypted using RSA before being sent.

Client-Server Chat: Supports real-time communication between client and server.

Automatic Key Generation: The server generates a fresh RSA key pair on startup.

 Public Key Sharing: The client receives the server’s public key automatically.

 Message Decryption on Server: Only the server can read messages using its private key.

#FUTURE SCOPE
-Adding file transfer
-Implementing GUI

