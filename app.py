from flask  import Flask,render_template,request

#creating object by using Flask class
app=Flask(__name__)

@app.route('/')
def home():
    #return render_template('index.html')
    #return render_template('grid.html')
    return render_template('registration.html')

@app.route('/regitration',methods=['POST','GET'])
def regitration():
    if request.method=='POST':
        name=request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        contact = request.form.get('contact')
        mail = request.form.get('email')

    return render_template('details.html',name=name,age=age,address=address,contact=contact,mail=mail)

app.run(debug=True)