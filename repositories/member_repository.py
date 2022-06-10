from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, premium, active) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    sql = "SELECT * FROM members"
    members = run_sql(sql)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id=%s"
    values = [id]
    member = run_sql(sql, values)[0]
    return member