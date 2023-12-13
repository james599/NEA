def append(username, assistant):  
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    line = -1
    for user_record in db:
        line += 1
        if user_record.split(",")[0] == username:
            db[line] = user_record.replace("\n","") + str(assistant) + "\n"
    
    with open('users/users.txt', 'w') as user_db:
        user_db.writelines(db)
    return 0