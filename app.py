from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.get('/')
def index():
  return render_template('index.html', title='Home')

@app.get('/about')
def about():
  return render_template('about.html', title='About',  location=request.args.get('location'))

@app.get('/hello')
def hello():
  return render_template('hello.html', name=request.args.get('name'), title='Hello')

#  eg http://localhost:8080/hello?name=Renee

@app.errorhandler(404)
def handle_404(e):
    return render_template('status_404.html', title="Page not found"), 404


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)