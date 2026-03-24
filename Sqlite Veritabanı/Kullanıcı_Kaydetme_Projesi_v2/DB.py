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

    def get_state(self, func):
        def wrapper(self,*args, **kwargs):

            self.cursor.execute("""
            SELECT state FROM users WHERE user_id = ? 
            """, (self.user_id,))

            state = self.cursor.fetchone()[0]

            if state == "NotLoggedIn":
                raise "NotLoggedInError"
            else:
                func(*args, **kwargs)

        return wrapper

    @get_state
    def __str__(self):
        return """
        KULLANICI BİLGİSİ:
        
        İsim: {}
        Yaş: {}
        E-mail: {}
        """.format(self.name,self.age,self.email)

    def make_connection(self):
        self.con = sqlite3.connect("Users.db")
        self.cursor = self.con.cursor()

    def cut_connection(self):
        self.con.close()

    def register_user(self):
        self.cursor.execute("""
        SELECT user_id FROM users WHERE email = ? 
        """,(self.email,))

        email = self.cursor.fetchone()[0]

        if self.email == email:
            raise "UsedEmailError"
        elif invalid_email(email):
            raise "InvalidEmailError"
        else:
            self.cursor.execute("""
            INSERT INTO users VALUES (?,?,?,?,?,?)
            """,(self.name,self.age,self.email,self.user_id,self.state,self.password))

    def login_user(self):
        self.cursor.execute("""
        SELECT user_id FROM users WHERE email = ? and password = ? 
        """,(self.email,self.password))

        user_id = self.cursor.fetchone()[0]

        if not user_id:
            raise "UnSuccessfulLoginError"
        else:
            self.cursor.execute("""
            UPDATE users SET state = "LoggedIn" WHERE user_id = ?"
            """,(self.user_id,))

    def logout_user(self):
        self.cursor.execute("""
        UPDATE users SET state = "NotLoggedIn" WHERE user_id = ?"
        """,(self.user_id,))

    @get_state
    def update_user(self,new_user_info: tuple):
        self.name = new_user_info[0]
        self.age = new_user_info[1]
        self.email = new_user_info[2]
        self.password = new_user_info[5]

        self.cursor.execute("""
        UPDATE users SET name = ? , age = ? , email = ? , password = ? WHERE user_id = ?
        """,(self.name,self.age,self.email,self.password,self.user_id))



def invalid_email(email: str):
    valid = {"@gmail.com","@hotmail.com"}

    indx = email.find("@")

    if email[indx:] in valid:
        return False
    else:
        return True









