from flask import Flask, render_template, request

app = Flask(__name__)

multiplication_factor = 1  # Default multiplication factor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    global multiplication_factor
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        multiplication_factor = int(request.form['multiplication_factor'])  # Update multiplication factor
        # Here you can handle the form data, e.g., send an email, store in a database, etc.
        return render_template('contact_success.html', name=name)
    return render_template('contact.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    # Placeholder logic for starting an attack (not implemented due to security concerns)
    global multiplication_factor
    return f"Attack started with multiplication factor {multiplication_factor}!"  # Just a placeholder

if __name__ == '__main__':
    app.run(debug=True)
