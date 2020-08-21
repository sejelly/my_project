from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# 닉네임 받아오고 없으면 저장
@app.route('/api/go', methods=['POST'])
def go():
    nickname = request.form['nickname']

    name = {
        'nickname': nickname
    }

    name = db.names.find_one({'nickname':nickname})
    if(name == None)db.names.insert_one({'nickname':name})
    # return jsonify({'result': 'success'})
    return render_template('page1.html')


@app.route('/api/show', methods=['GET'])
def show():
    nickname = request.form['nickname']
    names = list(db.names.find({nickname},{'_id':0}))
    return jsonify({'result':'success', 'names': names})


if __name__ == '__main__':
    app.run('0.0.0.0', port=17000, debug=True)