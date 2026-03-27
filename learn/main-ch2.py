from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# @app.route('/')
# def index():
#   return '<h1>Hello Flask!</h1>'

# @app.route('/')
# def index():
#   user_agent = request.headers.get('User-Agent')
#   return f'''
#   <h1>Hello Flask! Your UA is {user_agent}</h1>
#   ''', 400

@app.route('/')
def index():
  res = make_response('<h1>Hello Flask!</h1>')
  res.set_cookie('answer', '42')
  return res

@app.route('/baidu')
def baidu():
  return redirect('https://baidu.com')

# name默认是string
@app.route('/user/<name>')
def user(name):
  return f'<h1>Hello {name}!</h1>'


# 代替使用命令行启动服务器
if __name__ == '__main__':
  app.run(debug=True)