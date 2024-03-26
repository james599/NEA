def append(username, assistant):  
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()

    # Iterate through the lines in the db
    for line_index, user_record in enumerate(db):
        # If the username matches, replace the current line with the updated record
        if user_record.split(",")[0] == username:
            db[line_index] = user_record.replace("\n", "") + str(assistant) + "\n"
    
    with open('users/users.txt', 'w') as user_db:
        user_db.writelines(db)
    # Return confirmation 0 after updating the users.txt file
    return 0
