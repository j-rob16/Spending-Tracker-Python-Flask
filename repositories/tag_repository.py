from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags(category) VALUES (%s)"
    values = [tag.category]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag