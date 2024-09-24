from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method=='POST'):
        operation=request.form['operation']  #from form class we are pulling information
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if(operation=='addition'):
            r=num1+num2
            result =  f"The sum of num1 and num2 is {r} "

        if(operation=='subtraction'):
            r=num1-num2
            result =  f"The subtraction of num1 and num2 is {r} "

        if(operation=='multiplication'):
            r=num1*num2
            result =  f"The multiplication of num1 and num2 is {r} "

        if(operation=='divide'):
            r=num1/num2
            result =  f"The division of num1 and num2 is {r} "
        

        return render_template("results.html",result=result)


@app.route('/postman_request',methods=['POST'])
def postman_math_ops():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])

        if(operation=='addition'):
            r=num1+num2
            result =" The sum of num1 and num2 is " +  str(r)

        if(operation=='subtraction'):
            r=num1-num2
            result =  " The subtraction of num1 and num2 is " + str(r) 

        if(operation=='multiplication'):
            r=num1*num2
            result =  "The multiplication of num1 and num2 is " + str(r) 

        if(operation=='divide'):
            r=num1/num2
            result = "The division of num1 and num2 is" + str(r) 
        

        return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)