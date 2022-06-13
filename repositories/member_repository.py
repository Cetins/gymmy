from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, age, email, premium, active) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.email, member.premium, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    sql = "SELECT * FROM members ORDER BY name"
    members = run_sql(sql)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result["age"], result["email"], result["premium"], result["active"], result["id"])
    return member

def update(member):
    sql = "UPDATE members SET name=%s, age=%s, email=%s, premium=%s, active=%s WHERE id=%s"
    values = [member.name, member.age, member.email, member.premium, member.active, member.id]
    run_sql(sql, values)
    
def delete(id):
    sql = "DELETE FROM members WHERE id=%s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)