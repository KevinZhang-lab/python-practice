from  flask import Flask
from vsearch import search4letters
app=Flask(__name__)
@app.route('/')
def hello()->str:
    return 'Hello world from Flask'

@app.route('/search4')
def do_search()->str:
    """return letters that existed in both letter and phrase"""
    return str(search4letters).intersection('life, the univeristy, and everything!','eiru,!')

app.run()

