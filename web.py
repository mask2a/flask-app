from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'UP LOAD THU LEN WEB/'
 
if __name__ == '__main__':
    app.run()
