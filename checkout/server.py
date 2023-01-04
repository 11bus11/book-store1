#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
from flask import Flask, render_template, jsonify, request


# This is your test secret API key.
stripe.api_key = 'sk_test_51MMWIHKw2dgU31gmbmOT850THTjvEiZUgExqCGw4r9dysEfGh5auf9ZyZfiEy8CHhPs9CbPQ9SxCQNEoG877A0sm00Hy6e9Q2l'

app = Flask(__name__, static_folder='static',
            static_url_path='static/', template_folder='templates')


def calculate_order_amount(total):
    order_amount = total
    return order_amount


@app.route('/checkout', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['grand_total']),
            currency='sek',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run(port=8000)