from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.payment import Payment
import repositories.member_repository as member_repository
import repositories.payment_repository as payment_repository

payments_blueprint = Blueprint("payments", __name__)

@payments_blueprint.route("/payments")
def payments():
    results = payment_repository.select_all()
    payments = []
    
    for result in results:
        member = member_repository.select(result['member_id'])
        payment = Payment(result["amount"], result["date"], member, result["id"])
        payments.append(payment)
    return render_template("/payments/index.html", payments=payments)