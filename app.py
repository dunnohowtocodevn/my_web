from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="post">
        <input type="number" name="a" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="b" required>
        <input type="submit" value="Calculate">
    </form>
    {% if result %}
        <p>Result: {{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b if b != 0 else 'Error: Division by zero'
    
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)