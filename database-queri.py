import database_common


@database_common.connection_handler
def get_new_user_name(cursor, username):
    cursor.execute(""" SELECT username
                       FROM   users 
                       WHERE username = %(username)s; 
                       """, {'username': username})
    return cursor.execute