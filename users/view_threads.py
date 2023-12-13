def view(username):
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    line = -1
    for user_record in db:
        line += 1
        if user_record.split(",")[0] == username:
            return user_record.replace("\n","").split('|')[1:][::-1]