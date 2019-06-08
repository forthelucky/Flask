from flask import Flask
from flask import render_template, request, jsonify
import re

from calculator.controller import CalculatorController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # templates 폴더가 디폴트라 파일명망 쓰면 된다.


@app.route("/move/<path>")
def move(path):
    return render_template('{}.html'.format(path))

@app.route("/titanic", methods=["POST"])
def titanic():
    f1 = request.form['train']
    f2 = request.form['train']


@app.route("/ai_calc", methods=["POST"])  #python은 methods를 생략하면 디폴트값인 GET, html의 form테그보고 하는 것
def ai_calc():
    num1 = request.form['num1'] #form테그에 값이 여러개인데, 그 중 이름이 num1인 것
    num2 = request.form['num2']
    opcode = request.form['opcode']

    c = CalculatorController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = int(result)

    return render_template('ai_calc.html', **render_params)

@app.route("/ui_calc")
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('There is no value')
    else:
        print('formular : {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        #정규표현식에 익숙해지라고 한다..
        #patt = 에서 숫자에 대해 정의하고, sub에서는 stmt 스트링에서 patt 을 ''으로 변경하라고 하는 의미
        print('operator : {}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])

        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '/':
            result = n1 / n2
        elif op == '*':
            result = n1 * n2

    return jsonify(result = result)
    #flask는 값을 렌더링하기 위해서는 json으로 넘겨야한다.


if __name__ == '__main__' :
    app.run()

