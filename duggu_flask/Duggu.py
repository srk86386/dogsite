from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>')
def breed(name):
   #return f'Hello {nam}’
   return render_template('index.html', name = name)

if __name__ == '__main__':
   app.debug = True
   app.run()
   #app.run(debug = True)

