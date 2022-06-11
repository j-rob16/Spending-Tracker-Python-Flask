from db.run_sql import run_sql
from models.total import Total

def save(total):
    sql = "INSERT INTO totals(total_paid_to_merchant, user_id, merchant_id)"
    values = [total.total_paid_to_merchant, total.user.id, total.merchant.id]
    results = run_sql(sql, values)
    total.id = results[0]['id']
    return total