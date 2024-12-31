from flask import Flask, render_template, request, jsonify
from utils.converter import convert_currecy
from utils.api import get_crypto_price

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/crypto_price', methods=['GET'])
def crypto_price():
    symbol = request.args.get('symbol', 'BTC')  # Valor padrão: BTC
    convert_to = request.args.get('convert_to', 'USDT')  # Valor padrão: USDT
    amount = float(request.args.get('amount', 1))  # Valor padrão: 1

    result = get_crypto_price(symbol, convert_to)
    
    if 'error' in result:
        return jsonify(result)
    
    price = result["price"]
    converted_amount = price * amount

    return jsonify({
        "symbol": symbol.upper(),
        "price": price,
        "converted_amount": converted_amount,
        "convert_to": convert_to.upper(),
        "amount": amount
    })


if __name__ == "__main__":
    app.run(debug=True)