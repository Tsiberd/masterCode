from flask  import Flask, render_template , request



app = Flask(__name__,template_folder="Flask/template")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)

@app.route('/submit_v1', methods=['POST'])
def sumbit_v1():
    
        return render_template('sumbit_v1.py')

if __name__ == '__main__':
    app.run()
 
    
