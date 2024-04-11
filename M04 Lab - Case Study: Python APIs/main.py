from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    publisher = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User {self.bookname} - {self.author} - {self.publisher}"

@app.route('/home/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/books/get', methods=['GET'])
def get_books():
    books = Books.query.all()
    output = []
    for book in books:
        book_data = {'bookname': book.bookname, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return jsonify({'books': output})

@app.route('/books/get/<id>', methods=['GET'])
def get_book(id):
    book = Books.query.get_or_404(id)
    return jsonify({'bookname': book.bookname, 'author': book.author, 'publisher': book.publisher})

@app.route('/books/post', methods=['POST'])
def add_book():
    bookname = request.json['bookname']
    author = request.json['author']
    publisher = request.json['publisher']
    new_book = Books(bookname=bookname, author=author, publisher=publisher)
    db.session.add(new_book)
    db.session.commit()
    return 'Book is added'

@app.route('/books/delete/<id>', methods=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return 'Book is deleted'

if __name__ == '__main__':
    app.run(debug=True)
