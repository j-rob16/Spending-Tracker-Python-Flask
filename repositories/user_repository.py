from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users( first_name, last_name, age, wallet ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [user.first_name, user.last_name, user.age, user.wallet]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['first_name'], row['last_name'], row['age'], row['wallet'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        user = User(result['first_name'], result['last_name'], result['age'], result['wallet'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)