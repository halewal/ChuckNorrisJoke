import requests 
from flask import Flask, render_template 
 
 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    fact = get_random_fact() 
    return render_template('index.html', fact=fact) 
 
def get_random_fact(): 
    url = 'https://api.chucknorris.io/jokes/random' 
    response = requests.get(url) 
    return response.json()['value'] 
 
@app.route('/fact/<category>') 
def fact_by_category(category): 
    url = f'https://api.chucknorris.io/jokes/random?category={category}' 
    response = requests.get(url) 
    if response.status_code == 200: 
        fact = response.json()['value'] 
    else: 
        fact = "NOTHING" 
    return render_template('fact.html', fact=fact, category=category) 
 
if __name__ == '__main__': 
    app.run(debug=True) 
