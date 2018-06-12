import database_common


@database_common.connection_handler
def check_username(cursor, username):
    cursor.execute(""" SELECT username
                       FROM   users 
                       WHERE username = %(username)s; 
                       """, {'username': username})
    return cursor.execute


@database_common.connection_handler
def save_username(cursor, username, password):
    cursor.execute(""" INSERT INTO users (username, password)
                       VALUES ( %(username)s, %(password)s ) ;
                       """, {'username': username, 'password': password})