import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load the list of top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file]
    
    # Function to hash a password using SHA-1
    def sha1_hash(password):
        return hashlib.sha1(password.encode()).hexdigest()
    
    # If use_salts is True, load the known salts
    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as file:
            salts = [line.strip() for line in file]
    
    # Iterate through all passwords and compare hashes
    for password in passwords:
        # If use_salts is False, just hash and compare each password
        if not use_salts:
            if sha1_hash(password) == hash:
                return password
        # If use_salts is True, prepend and append each salt to the password
        else:
            for salt in salts:
                # Hash with salt prepended and compare
                if sha1_hash(salt + password) == hash:
                    return password
                # Hash with salt appended and compare
                if sha1_hash(password + salt) == hash:
                    return password
    

    return "PASSWORD NOT IN DATABASE"
