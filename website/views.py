from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Book
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        book = request.form.get('book')
        checked = request.form.get('isRead')

        if len(book) < 1:
            flash('Book title is too short', category='error')
        else:
            if checked:
                is_read = True
            else:
                is_read = False

            new_book = Book(name=book, read=is_read, user_id=current_user.id)
            db.session.add(new_book)
            db.session.commit()
            flash('Book added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-book', methods=['POST'])
def delete_book():
    data = json.loads(request.data)
    book_id = data['bookId']
    book = Book.query.get(book_id)
    if book:
        if book.user_id == current_user.id:
            db.session.delete(book)
            db.session.commit()
    return jsonify({})


@views.route('/update-read', methods=['POST'])
def update_read():
    data = json.loads(request.data)
    book_id = data['bookId']
    book = Book.query.get(book_id)

    if book.read:
        book.read = False
    else:
        book.read = True

    db.session.commit()
    return jsonify({})