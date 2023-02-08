from flask import Flask, request
app = Flask(__name__)

    
@app.route('/')
def hello():
    s1 = "<H1> 'Hello WOrld!' </H1>"
    return s1


@app.route('/add')
def add():
    a = 10
    b = 20
    s2 = "<H1>" +  str(a+b) + "</H1>"
    return s2


@app.route('/add_new')
def add_new():
    a1 = request.args.get("a")
    b1 = request.args.get("b")    
    s2 = "<H1>" +  str(int(a1) + int(b1) ) + "</H1>"
    return s2




if __name__=='__main__':
    app.run()