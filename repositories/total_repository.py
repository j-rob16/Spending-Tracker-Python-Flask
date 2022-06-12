from db.run_sql import run_sql
from models.total import Total

def save(total):
    sql = "INSERT INTO totals( total_paid_to_merchant, user_id, merchant_id ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [total.total_paid_to_merchant, total.user.id, total.merchant.id]
    results = run_sql(sql, values)
    total.id = results[0]['id']
    return total

def select_all():
    totals = []
    sql = "SELECT * FROM totals"
    results = run_sql(sql)
    for row in results:
        total = Total(row['total_paid_to_merchant'], row['user_id'], row['merchant_id'])
        totals.append(total)
    return totals

def select(id):
    total = None
    sql = "SELECT * FROM totals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None: 
        total = Total(result['total_paid_to_merchant'], result['user_id'], result['merchant_id'])
    return total

def update(total):
    sql = "UPDATE totals SET ( total_paid_to_merchant, user_id, merchant_id ) VALUES ( %s, %s, %s )WHERE id = %s"
    values = [total.total_paid_to_merchant, total.user_id, total.merchant_id, total.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM totals"
    run_sql(sql)