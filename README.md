# Flask Blog

Flask 有 3 个主要依赖：路由、调试和 Web 服务器网关接口（WSGI，Web server gateway
interface）子系统由 Werkzeug 提供；模板系统由 Jinja2 提供；命令行集成由 Click 提供。

创建虚拟环境：

```bash
python -m venv .venv
```

激活：

```bash
source .venv/bin/activate
```

创建环境变量（如果Flask app的入口文件是app.py或wsgi.py时，可以不创建环境变量）

```bash
export FLASK_APP=main.py
```

开启调试模式：

```bash
export FLASK_DEBUG=1
```

启动本地服务器：

```bash
flask run
```