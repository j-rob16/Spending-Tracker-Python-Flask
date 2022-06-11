from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users(first_name, last_name, age, wallet) RETURNING id"
    values = [user.first_name, user.last_name, user.age, user.wallet]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user