def view(username):
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    for user_record in db:
        if user_record.split(",")[0] == username:
            # Remove the newline character and return the user's thread id's, 
            # converted to a list, and reversed to show in chronological
            return user_record.replace("\n","").split('|')[1:][::-1]
