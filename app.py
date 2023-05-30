# backend 부분에 해당하는 script
# 작성중인 script는 인터프리터로 결정 -> 변경해주기
# zsh -> bash로 변경
# python app.py 실행 시 가상환경이 잘 들어가져 있는지 확인해야 함

from flask import Flask, render_template
from flask import request #get post 하려면 필수
import pymysql

app = Flask(__name__)

#앱을 실행시키기 위해 작성
@app.route("/")
def signup(): # 창을 띄워주는 함수
    return render_template("signup.html")

@app.route("/signup", methods=["POST"]) # '/' 필수, 'methods' 주의
def signupPost(): # 함수 명은 다르게 해야한다, 제출 버튼을 누르면 실행되는 함수
    uid = request.form['user_id'] # front에서 가져올 때 signup.html의 name 기준으로 불러와야 한다
    # name이 user_id인 form을 가져와라
    upwd = request.form['user_pwd']
    uemail = request.form['user_email']
    uphone = request.form['user_phone']

    print(uid, upwd, uemail, uphone)
    
    # return render_template

# 연결 시키기
# host랑 port 중요, mysql의 root랑 비밀번호, db 이름, charset은 한글 깨짐 방지
# DB 연동
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'dlsvlslxm1!',
    db = 'test',
    charset = 'utf8'
)

print(db_conn) # 웹과 db를 연결시키려면 db_conn 형식으로 connection 한다
# mysql이 켜져 있어야 함

# 커서 객체 생성
cursor = db_conn.cursor()

query = "select * from player"

cursor.execute(query)

for i in cursor:
    print(i)

@app.route('/sqltest')
def sqltest():
    # 커서 객체 생성
    cursor = db_conn.cursor()

    query = "select * from player"

    cursor.execute(query)

    result = []
    for i in cursor: # i = ('2012136', '오비나', ....) 튜플 형태로 받는다
        temp = {'player_id':i[0],'player_name':i[1]}
        result.append(temp)
    
    return render_template('sqltest.html', result_table = result)

@app.route('/detail')
def detailtest():
    temp = request.args.get('id')
    temp1 = request.args.get('name')

    cursor = db_conn.cursor()

    query = "select * from player where player_id = {} and player_name like '{}'".format(temp, temp1)
                                                #sql 쿼리에서 작은 따옴표 쿼리문에 넣으니까 넣어줘야 함
    cursor.execute(query)

    result = []
    for i in cursor:
        temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2], 'weight':i[-1]}
        result.append(temp)
        
    return render_template('detail.html', result_table = result)

# flask 웹 서버를 실행시키기 위해서는 필수 작성
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="127.0.0.1", port="7000") # url을 바꾸는 방식