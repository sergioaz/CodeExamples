import hashlib, os
import sqlite3

password = "mypassword123"
salt = os.urandom(16)

# Derive a key using PBKDF2 + SHA-256
hashed = hashlib.pbkdf2_hmac(
    'sha256',                  # Hash algorithm
    password.encode('utf-8'),  # Convert password to bytes
    salt,                      # Salt
    100_000                    # Iterations (the higher, the slower)
)

print("Salt:", salt.hex())
print("Derived key:", hashed.hex())

# store salt and hashed key into sqlite
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS password_hashes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        salt TEXT NOT NULL,
        hashed_key TEXT NOT NULL
    )
''')
cursor.execute('''
    INSERT INTO password_hashes (salt, hashed_key)
    VALUES (?, ?)
''', (salt.hex(), hashed.hex()))
conn.commit()


# input password and confirm it's in database
input_password = input("Enter password to check: ")

cursor = conn.cursor()
cursor.execute('SELECT salt, hashed_key FROM password_hashes')
rows = cursor.fetchall()
conn.close()

found = False
for db_salt_hex, db_hash_hex in rows:
    db_salt = bytes.fromhex(db_salt_hex)
    db_hash = bytes.fromhex(db_hash_hex)
    test_hash = hashlib.pbkdf2_hmac(
        'sha256',
        input_password.encode('utf-8'),
        db_salt,
        100_000
    )
    if test_hash == db_hash:
        found = True
        break

if found:
    print("Password is in the database.")
else:
    print("Password not found.")
