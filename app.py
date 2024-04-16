from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'Hello, World!'

@app.route('/products')
def Products():
    return "This is product's page"

if __name__ == "__main__":
    app.run(debug=True)

    # If you want to change the port you can run this command:
    '''
    app.run(debug=True,port=8000)
    '''
