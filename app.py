from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cart')
def manager():
    return render_template("cart.html")

@app.route('/shop')
def inventory():
    return render_template("shop.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
