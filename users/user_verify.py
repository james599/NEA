from hashlib import sha256
def verify(username: str, expected_password: str) -> bool:
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()
    for user_record in db:
        expected_hash_password = sha256(expected_password.encode('utf-8') + user_record.split(",")[2].encode('utf-8')).hexdigest()
        if user_record.split(",")[0] == username and user_record.split(",")[1] == expected_hash_password:
            return True
    return False
