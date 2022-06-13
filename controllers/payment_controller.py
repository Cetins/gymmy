from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.member_repository as member_repository
import repositories.payment_repository as payment_repository

payments_blueprint = Blueprint("payments", __name__)

@payments_blueprint.route("/payments")
def payments():
    pass