from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required,  current_user
from .models import Clothes
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        shirt = request.form.get('shirt')
        new_shirt = Clothes(data=shirt, user_id=current_user.id)
        db.session.add(new_shirt)
        db.session.commit()
        flash('Shirt Added!', category='success')

    return render_template("home.html", user=current_user)

# @views.route('/delete-clothes', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     print(note)
#     noteId = note['noteID']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
#             flash('Note Deleted!', category='success')

#     return jsonify({})