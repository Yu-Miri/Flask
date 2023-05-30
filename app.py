from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/main") #바인딩
def index():
    temp = request.args.get("uid")
    temp1 = request.args.get("cid")
    print(temp, temp1)
    return render_template("index.html")

@app.route("/test") #화면으로 가기 위한 함수, 창 띄워주는 것, 반응할 함수 선언
def testget():
    return render_template('posttest.html')

#post를 받는 함수
@app.route('/test',methods=['POST'])
def testpost():
    value = request.form['input'] #posttest.html에서 form 안에 있는 input tag를 불러와서 value 변수에 저장

    print(value)
    return render_template('posttest.html')

if __name__ =="__main__":
    app.run(debug=True)
    #host 등을 직접 지정하고 싶다면
    #app.run(host="127.0.0.1", port="5000", debug=True)