from flask import Flask, request, render_template

app = Flask(__name__)

# In-memory history storage
calculation_history = []

@app.route('/')
def index():
    return render_template('index.html', history=calculation_history)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get the form data
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform the calculation
        if operation == 'add':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operation_symbol = '*'
        elif operation == 'divide':
            if num2 == 0:
                result = "Error (Division by Zero)"
                operation_symbol = '/'
            else:
                result = num1 / num2
                operation_symbol = '/'
        else:
            result = "Invalid Operation"
            operation_symbol = '?'

        # Add the calculation to the history
        if isinstance(result, (int, float)):
            calculation_history.append(f"{num1} {operation_symbol} {num2} = {result}")

        # Pass the result and history back to the HTML page
        return render_template('index.html', result=result, history=calculation_history)
    except ValueError:
        return render_template('index.html', result="Invalid Input", history=calculation_history)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    # Clear the history
    calculation_history.clear()
    return render_template('index.html', history=calculation_history)

if __name__ == "__main__":
    app.run(debug=True)