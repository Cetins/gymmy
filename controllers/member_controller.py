from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)

@members_blueprint.route("/members/new")
def new():
    return render_template("members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def add_member():
    name = request.form['member_name']
    premium = request.form['premium']
    active = request.form['active']
    new_member = Member(name, premium, active)
    member_repository.save(new_member)
    
    return redirect("/members")

@members_blueprint.route("/members/edit/<id>")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form['member_name']
    premium = request.form['premium']
    active = request.form['active']
    updated_member = Member(name, premium, active, id)
    member_repository.update(updated_member)
    return redirect("/members")

@members_blueprint.route("/members/delete/<id>")
def delete(id):
    member_repository.delete(id)
    return redirect("/members")