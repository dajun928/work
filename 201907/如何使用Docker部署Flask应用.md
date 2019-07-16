

#  使用Docker部署Flask项目

 Theodore Si      14 July 2019

## 新建一个Flask项目

目录结构

```
$ tree .
.
├── gunicorn.conf.py
├── my_flask_demo
│   └── __init__.py
└── setup.py
```

`__init__.py`就是我们的app了，其内容如下：

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I am running in docker!'

if __name__ == '__main__':
    app.run(debug=True)
```

也许你好奇为什么我们把程序放在了`__init__.py`里，这是因为对于一个大型项目，官方建议将其变为一个package，详细内容可以[看这里](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/#larger-applications)。好吧，我承认我们的项目怎么说也不算大型…Anyway…

`setup.py`是用来协助`Distutils`对程序打包的。有了它，我们就可以通过`pip`来安装我们的app了。其实这里`setup.py`也不是必须的啦，因为我们会把项目整个COPY过去。

```
from distutils.core import setup

setup(name='my_flask_demo',
      version='1.0',
      description='This is a demo to show how to run a flask app in docker',
      author='Theo Si',
      author_email='theosi@outlook.com',
      url='https://www.theodoresi.top',
      packages=['my_flask_demo']
      )
```

而`gunicorn.conf.py`是`gunicorn`的配置文件，它描述了我们的程序应该被怎样运行。

```
$ cat gunicorn.conf.py 
workers = 10
worker_class = "gevent"
bind = "0.0.0.0:8888"
```

显然，我们的程序可以被任意网络访问，并且运行在8888端口上。

## 在本地部署运行

创建一个新的venv并且安装依赖包： 最好加入`-i`参数指定Base URL of Python Package Index，不然速度可能让你怀疑人生。

```
# 我已经在home目录中建立了venv，如果你没有，可以使用 $python3 -m venv ~/venv创建
$ . ~/venv/bin/activate 
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent gunicorn flask wheel
```

尝试运行一下：

```
$ export FLASK_APP=my_flask_demo
$ flask run
```

如果一切正常，你应该看到你的app已经在`5000`端口运行了。

然后我们用`pip`将我们的app安装到刚刚创建的venv中：

```
$ pip install .
```

使用`gunicorn`运行：

```
gunicorn my_flask_demo:app -c ./gunicorn.conf.py
```

现在我们就可以通过`http://127.0.0.1:8888`成功访问了！

## 使用docker部署运行

### 生成Dockerfile

首先，我们来生成`requirements.txt`，它描述了我们的python程序需要哪些依赖包。有了它，我们就可以无差异地克隆我们的运行环境。

```
$ pip freeze > requirements.txt

# 只要有这三行就够了
$ cat requirements.txt
Flask==1.1.1
gevent==1.4.0
gunicorn==19.9.0
```

接着我们创建一个Dockerfile，文件的内容很简单，歌词大意就是以`python:3`这个镜像为基础，设置好working directory，但后把`requirements.txt`复制过去，用pip重建我们的依赖环境，然后复制我们下源代码，最后启动程序。

```
$ cat Dockerfile 
FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
RUN pip install .

CMD ["gunicorn", "my_flask_demo:app", "-c", "./gunicorn.conf.py"]
```

我们这里为了简单，就不再搭配Nginx什么的了。

### build & run

我们最终的目录结构如下：

```
$ tree .
.
├── Dockerfile
├── gunicorn.conf.py
├── my_flask_demo
│   └── __init__.py
├── requirements.txt
└── setup.py
```

现在我们就可以开始创建我们的image了

```
$ sudo docker build -t "my_flask_demo" .
$ sudo docker image ls
```

我们应该可以看到新的image已经生成好了。那就让我们来运行一下吧！

```
# interactively
$ sudo docker run -it --rm -p 8888:8888 my_flask_demo
# 或者run in background
$ sudo docker run -d -p 8888:8888 --name my_flask_demo my_flask_demo
```

这个时候你就可以通过`http://localhost:8888`访问你的app了。当你想关闭应用的时候，如果是通过`-it`运行的，只要`Ctrl-C`即可，如果是通过`-d`，只要运行以下命令就可以了。

```
$ sudo docker stop my_flask_demo
```

- ©Theo's blog. All rights reserved.