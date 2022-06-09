from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members(name, premium, active) VALUES (%s, %s, %s) RETURNING *"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member
