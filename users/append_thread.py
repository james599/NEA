def append(username, thread):
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    for line_index, user_record in enumerate(db):
        # If the username matches, replace the current line with the updated record
        if user_record.split(",")[0] == username:
            if "|" not in user_record:
                # If the user has no threads yet, add the thread to the record
                db[line_index] = user_record.replace("\n", "") + "|" + thread + "\n"
            else:
                # If the user already has threads, append the new thread to the existing list
                threads = user_record.split('|')[1].replace("\n", "")
                db[line_index] = user_record.split('|')[0] + "|" + str(threads) + "|" + thread + "\n"
           
    with open('users/users.txt', 'w') as user_db:
        user_db.writelines(db)

    return 0
