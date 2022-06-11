from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags( category ) VALUES ( %s ) RETURNING id"
    values = [tag.category]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)