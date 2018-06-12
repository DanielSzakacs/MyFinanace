import database_common


@database_common.connection_handler
def check_username(cursor, username):
    cursor.execute(""" SELECT username
                       FROM   users 
                       WHERE username = %(username)s; 
                       """, {'username': username})
    return cursor.fetchall()


@database_common.connection_handler
def save_username(cursor, username, password, time):
    cursor.execute(""" INSERT INTO users (username, password, registration_time)
                       VALUES ( %(username)s, %(password)s, %(registration_time)s) ;
                       """, {'username': username, 'password': password, 'registration_time': time})


@database_common.connection_handler
def get_password(cursor, username):
    cursor.execute("""SELECT password
                        FROM users 
                        WHERE username = %(username)s;
                        """, {'username': username})
    return cursor.fetchone()

@database_common.connection_handler
def account_get_registration_time(cursor, username):
    cursor.execute("""SELECT registration_time
                        FROM users
                        WHERE username = %(username)s;
                        """, {'username':username})
    return cursor.fetchone()