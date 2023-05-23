from setuptools import setup


setup(
    name='easytqdm',# 需要打包的名字,即本模块要发布的名字
    version='v1.5',#版本
    description='easytqdm', # 简要描述
    py_modules=['easytqdm'],   #  需要打包的模块
    author='LXD', # 作者名
    author_email='clearlyzero@stu.cqut.edu.cn',   # 作者邮件
    url='https://github.com/clearlyzerolxd/easytqdm', # 项目地址,一般是代码托管的网站
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)