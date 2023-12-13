import requests
from flask import Flask,request,render_template
import SECRETS
import webbrowser
# webbrowser.open('http://127.0.0.1:5000')


app =Flask(__name__)
@app.route('/',methods=["POST","GET"])
def test():
    if request.method == "POST":
        code = request.form.get("code")
        key= SECRETS.x
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={code}&appid={key}&units=metric")
        
        class vars:
            s = r.json()['main']
            d=r.json()['weather'][0]
            temp = s['temp']
            min = s['temp_min']
            max = s['temp_max']
            hum = s['humidity']
            m = d['main'].upper()
            des= d['description'].upper() 
            icon = d['icon']
        print(r.json())
        # return r.json()#,str(temp)
        return render_template('weatherapp2.html',vars=vars)#temp=temp,min=min,max=max,hum=hum)
    
    return render_template('weatherapp1.html')


if __name__ == '__main__':
       

       app.run(debug='true')

       
