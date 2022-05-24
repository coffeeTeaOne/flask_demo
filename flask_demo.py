from flask import Flask, request, render_template
import json

# 创建一个Flask实例
app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False


@app.route('/')
@app.route('/welcome')  # 路由系统生成视图对应url， 1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
    return 'Hello, world!，asdfasdf'


@app.route('/getInfo', methods=['GET', 'POST'])
def returnInfo():
    # python类型
    data = {'name': 'XiaoMing', 'age': '20', 'city': 'beijing'}
    # 编码为json类型
    json_data = json.dumps(data)

    status = request.args['status']

    # 获取客户端传过来的data参数值
    receive_data = request.args.get('data')
    print('data:', receive_data)
    if status == 'ok':  # 为ok时才返回给客户端data数据
        return json_data



if __name__ == '__main__':
        app.run(host='0.0.0.0',port=10102)
