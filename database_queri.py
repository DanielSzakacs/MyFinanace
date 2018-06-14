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
                        """, {'username': username})
    return cursor.fetchone()


@database_common.connection_handler
def save_finance_data(cursor, user_id, house, food, cloth, everything_else, saving_month):
    cursor.execute(""" INSERT INTO  financedata  (user_id, house, food, cloth, everything_else, income)
                       VALUES (%(user_id)s, %(house)s, %(food)s, %(cloth)s, %(everything_else)s, %(income)s);
                       """, {'user_id': user_id, 'house': house, 'food': food, 'cloth': cloth, 'everything_else': everything_else, 'income': saving_month })


@database_common.connection_handler
def get_user_id(cursor, username):
    cursor.execute("""SELECT id
                    FROM users  
                    WHERE username = %(username)s;
                    """, {'username': username})
    return cursor.fetchone()


@database_common.connection_handler
def delete_finance_row(cursor, id):
    cursor.execute("""DELETE 
                      FROM financedata
                      WHERE user_id = %(id)s; 
                      """,{'id': id})

@database_common.connection_handler
def graph_data(cursor, id):
    cursor.execute("""SELECT house, food, cloth, everything_else, income 
                      FROM financedata 
                      WHERE user_id = %(id)s; 
                      """, {'id': id})
    return cursor.fetchall()
