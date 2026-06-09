from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Python CI/CD Pipeline is working perfectly on my Mac!</h2>'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=3000)