def append(username, thread):
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    line = -1
    for user_record in db:
        line += 1
        if user_record.split(",")[0] == username:
            if "|" not in user_record:
                db[line] = user_record.replace("\n","") + "|" + thread + "\n"
            else:
                threads = user_record.split('|')[1].replace("\n","")
                db[line] = user_record.split('|')[0] + "|" + str(threads) + "|" + thread + "\n"
           
    with open('users/users.txt', 'w') as user_db:
        user_db.writelines(db)
    return 0
