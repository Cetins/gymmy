from db.run_sql import run_sql

from models.payment import Payment
from models.member import Member

def save(payment):
    sql = "INSERT INTO payments (amount, date, member_id,) VALUES (%s, %s, %s) RETURNING id"
    values = [payment.amount, payment.date, payment.member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    payment.id = id
    
def select_all():
    sql = "SELECT * FROM payments"
    payments = run_sql(sql)
    return payments

def select(id):
    sql = "SELECT * FROM payments WHERE id=%s"
    values = [id]
    payment = run_sql(sql, values)[0]
    return payment

def update(payment):
    sql = "UPDATE payments SET amount=%s, date=%s, member_id=%s WHERE id=%s"
    values = [payment.amount, payment.date, payment.member_id]
    run_sql(sql, values)
    
def delete(id):
    sql = "DELETE FROM payments WHERE id=%s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM payments"
    run_sql(sql)
    