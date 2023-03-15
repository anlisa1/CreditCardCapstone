# These routes are an example of how to use data, forms and routes to create
# a forum where a blogs and comments on those blogs can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import User
from app.classes.forms import MarkasCompleteForm
from flask_login import login_required
import datetime as dt

global index;

@app.route("/module<int:id>")
def module(id):
  index = id
  return render_template(f"./modules/module{id}.html")

@login_required
def markComplete():
    form = MarkasCompleteForm

    if form.validate_on_submit():
        # if the form was valid then this gets an object that represents the currUser's data
        currUser = User.objects.get(id=current_user.id)
        # This updates the data on the user record that was collected from the form
        courses_completion[index] = True
        currUser.update(
            courses_completion = form.courses_completion.data,
        )
