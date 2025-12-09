#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items_page():
    items = ["Leonardo", "Raphael", "Donatello", "Michelangelo"]
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

