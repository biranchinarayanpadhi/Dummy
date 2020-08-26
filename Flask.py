from flask import Flask,request,make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/city',methods=['GET','POST'])
def getItem():
    if request.method == "POST":
        user=request.get("user")
        print(user)
    return make_response(request.method,200)


if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True) 
    
    

    