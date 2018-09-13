#!/usr/local/bin/python3.6
# coding = utf-8
from flask import Flask, render_template

app = Flask(__name__)


# 返回一个网页（模板）
# 给模板填充数据
@app.route('/')
def index():
    # 比如需要传入网址
    url_str = "www.mindai.com"
    # return 'yes?!'
    return render_template('index.html', url_str=url_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004, debug=True)
