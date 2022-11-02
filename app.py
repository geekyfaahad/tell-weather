from flask import Flask,render_template,request,redirect,url_for
import requests,json

app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/output', methods=['POST','GET'])
def view():
    try:
        if request.method=='POST':
            city=str(request.form['city'])
            base_url='https://api.openweathermap.org/data/2.5/weather?q='
            city=city
            api=open('F9Y%$6n5').read()
            url=(f'{base_url}{city}&appid={api}')
            response=json.loads(requests.request("GET", url).text)
            temp=(response['main']['temp'])
            c=int(temp-273.15)
            print(url)
            return render_template("output.html",result=c,city=city) 
        elif request.method=='GET':
            return "sorry we don't accept get requests"
    except:
        return redirect(url_for('index'))
app.run(debug=True)
