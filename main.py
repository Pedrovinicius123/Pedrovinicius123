from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
  return render_template('homepage.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)
