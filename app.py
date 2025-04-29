from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            price_per_kg = float(request.form['price_per_kg'])
            weight = float(request.form['weight'])
            unit = request.form['unit']

            # Convert gram to kg if needed
            if unit == 'Gram (g)':
                weight = weight / 1000

            total_price = weight * price_per_kg
            result = f"Total Price: ₹{total_price:.2f}"

        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('index.html', result=result)