users.txt stores all the users:
USERNAME, HASHED PASSWORD, ASSISTANT ID | THREAD1 | THREAD2 ...

user_verify.py checks user information given in /login

user_new.py adds user information to DB

append_thread.py adds openAI threads to DB array

pop_thread.py deletes particular thread from DB array

view_threads.py returns the array of threads
