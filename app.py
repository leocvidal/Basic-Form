from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from forms import APIForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = APIForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        response = call_api(name, email)
        if response:
            flash('Form submitted successfully!', 'success')
            return redirect(url_for('result', result=response))
        else:
            flash('API call failed!', 'danger')
    return render_template('index.html', form=form)

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

def call_api(name, email):
    api_url = 'https://jsonplaceholder.typicode.com/posts'  # Replace with your API URL
    payload = {'name': name, 'email': email}
    try:
        #GET returns API response
        #response = requests.get(api_url, json=payload)
        #POST returns your payload
        response = requests.post(api_url, json=payload)

        response.raise_for_status()
        print (response.json())
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
