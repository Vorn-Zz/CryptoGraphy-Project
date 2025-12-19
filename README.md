# CryptoGraphy-Project
# Secure File Locker using AES Encryption

## Project Overview
Secure File Locker is a desktop application developed using Python that protects files by encrypting them with AES-256 encryption. The system allows users to securely lock and unlock files using a password through a simple graphical user interface (GUI).

The main purpose of this project is to prevent unauthorized access to sensitive files such as documents, images, and personal data. Even if the encrypted file is copied or stolen, it cannot be read without the correct password.

---

## How to Use the System

### 1. Run the Application
Start the program by running:


A graphical window will open.

---

### 2. Encrypt a File
1. Click **Browse** and select the file you want to protect  
2. Enter a password  
3. Click **Encrypt**  
4. The encrypted file will be saved automatically in the **encrypted/** folder  

The encrypted file will have a `.enc` extension.

---

### 3. Decrypt a File
1. Click **Browse** and select an encrypted `.enc` file  
2. Enter the correct password  
3. Click **Decrypt**  
4. The decrypted file will be saved in the **decrypted/** folder  

If the password is incorrect, the system will not decrypt the file.

---

## How the System Works

1. The user selects a file and enters a password through the GUI  
2. The system generates a secure encryption key from the password using **PBKDF2 with SHA-256**  
3. The file data is encrypted using **AES-256 in GCM mode**  
4. The encrypted output is saved in a dedicated folder  
5. During decryption, the same password is used to regenerate the key  
6. If the key is correct, the file is restored to its original form  

---

## Security Features
- AES-256 encryption (strong industry standard)  
- Password-based key derivation using PBKDF2  
- Salt and authentication tag for integrity protection  
- Encrypted and decrypted files stored in separate folders  

---

## Output Folders
- **encrypted/** → stores encrypted files  
- **decrypted/** → stores decrypted files  

These folders are created automatically when the application runs.

---

## Summary
This project demonstrates a practical application of cryptography by using AES encryption to protect files. It provides a simple and secure way for users to safeguard their data while also illustrating how modern encryption techniques work in real-world systems.
