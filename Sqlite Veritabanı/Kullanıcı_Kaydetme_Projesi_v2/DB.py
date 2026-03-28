import sqlite3

class User:
    def __init__(self,
        name: str = None,
        age: int = None,
        email: str = None,
        user_id: str = None,
        state="NotLoggedIn",
        password: str = None):

        self.name = name
        self.age = age
        self.email = email
        self.user_id = user_id
        self.state = state
        self.password = password

    def __str__(self):
        return "user_id:{}\nemail:{}\npassword:{}".format(self.user_id,self.email,self.password)

    def show_user_info(self):
        self.cursor.execute("""
        SELECT * FROM users WHERE user_id = ?
        """,(self.user_id,))

        user_info = self.cursor.fetchall()

        name = user_info[0][0]
        age = user_info[0][1]
        email = user_info[0][2]

        return """
USER INFORMATION:
        
Name: {}
Age: {}
E-mail: {}
        """.format(name,age,email)

    def make_connection(self):
        self.con = sqlite3.connect("Users.db")
        self.cursor = self.con.cursor()

    def cut_connection(self):
        self.con.close()

    def register_user(self):
        self.cursor.execute("""
        SELECT email FROM users WHERE email = ? 
        """,(self.email,))

        email = self.cursor.fetchall()

        if email:
            return "UsedEmailError"
        elif not invalid_email(self.email):
            return "InvalidEmailError"
        else:
            self.cursor.execute("""
            INSERT INTO users VALUES (?,?,?,?,?,?,datetime('now','localtime'))
            """,(self.name,self.age,self.email,self.user_id,self.state,self.password))
            self.con.commit()
            return True

    def login_user(self):
        self.cursor.execute("""
        SELECT * FROM users WHERE email = ? and password = ? 
        """,(self.email,self.password))

        user_info = self.cursor.fetchall()

        if not user_info:
            return "UnSuccessfulLoginError"
        else:
            self.cursor.execute("""
            UPDATE users SET state = "LoggedIn" WHERE user_id = ?
            """,(user_info[0][3],))
            self.con.commit()
        return user_info


    def logout_user(self):
        self.cursor.execute("""
        UPDATE users SET state = "NotLoggedIn" WHERE user_id = ?
        """,(self.user_id,))
        self.con.commit()


    def update_user(self,new_user_info: tuple):
        self.name = new_user_info[0]
        self.age = new_user_info[1]
        self.email = new_user_info[2]
        self.password = new_user_info[3]

        self.cursor.execute("""
        UPDATE users SET name = ? , age = ? , email = ? , password = ? WHERE user_id = ?
        """,(self.name,self.age,self.email,self.password,self.user_id))
        self.con.commit()

    def pull_user_info(self,user_id):
        self.cursor.execute("""
        SELECT * FROM users WHERE user_id = ?
        """,(user_id,))

        user_info = self.cursor.fetchall()
        return user_info

    def is_log_id_unique(self,log_id):
        self.cursor.execute("""
        SELECT log_id FROM logs WHERE log_id = ?
        """,(log_id,))

        log_unique_id = self.cursor.fetchall()

        if not log_unique_id:
            return True
        else:
            return False

    def is_user_id_unique(self,user_id):
        self.cursor.execute("""
        SELECT user_id FROM users WHERE user_id = ?
        """,(user_id,))

        user_unique_id = self.cursor.fetchall()

        if not user_unique_id:
            return True
        else:
            return False

    def get_state(self):
        self.cursor.execute("""
        SELECT state FROM users WHERE user_id = ?
        """,(self.user_id,))

        state = self.cursor.fetchall()

        if state and state[0][0] == "NotLoggedIn":
            return False
        else:
            return True

    def insert_log(self,log_info: tuple):
        log_id = log_info[0]
        user_id = log_info[1]
        action = log_info[2]

        self.cursor.execute("""
        INSERT INTO logs VALUES (?,?,?,datetime('now','localtime'))
        """,(log_id,user_id,action))
        self.con.commit()

    def delete_user(self):
        self.cursor.execute("""
        DELETE FROM users WHERE user_id = ?
        """,(self.user_id,))

        self.con.commit()

def invalid_email(email: str):
    valid = {"gmail.com","hotmail.com"}

    parts = email.split("@")

    if len(parts) != 2:
        return False
    elif parts[1] not in valid:
        return False
    else:
        return True









