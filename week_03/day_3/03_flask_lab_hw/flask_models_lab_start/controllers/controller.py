from flask import render_template
from models.order_list import *

from app import app
# from models.something

@app.route('/')
def index():
    return render_template('index.html', orders = enumerate(order_list))

@app.route('/orders/<index>')
def get_order(index):
    return render_template('order.html', orders = order_list, number = int(index))