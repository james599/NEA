def append(username, password):
    import string
    import random
    from hashlib import sha256
    salt = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))
    hash_password = sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    
    user_db = open("users/users.txt", "a")
    user_db.write(username + "," + hash_password + "," + salt + ",\n")
    user_db.close()
    return 0

def verify(username):
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()
    for user_record in db:
        if user_record.split(",")[0] == username:
            return True
    return False
