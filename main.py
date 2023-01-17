from flask import Flask, render_template

app = Flask(__name__)

try:
  @app.route('/')
  def homepage():
    return render_template('homepage.html')
    
except Exception as err_0:
  print(f'{err_0}')

try:  
  @app.route('/dev_log')
  def dev_log():
    return render_template('devlog.html')

except Exception as err_1:
  print(f'{err_1}')
  
try:
  @app.route('/contatos')
  def contatos():
    return render_template('contatos.html')

except Exception as err_2:
  print(f'{err_2}')

app.run(debug=True, host='0.0.0.0', port=8080)
