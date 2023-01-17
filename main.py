from flask import Flask, render_template

app = Flask(__name__)

@app.route('\homepage')
def homepage():
  return render_template('homepage.html')


@app.route('\dev_log')
def dev_log():
  return render_template('devlog.html')

@app.route('\contatos')
def contatos():
  return render_template('contatos.html')

app.run(debugger=True)