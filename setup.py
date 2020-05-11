# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-09 14:13:10
@UpdateDate: 2020-05-09 14:13:53
@Description: 发布包的配置
'''

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name='AStar',
    version="0.0.1",
    author="lamborghini1993",
    author_email="1323242382@qq.com",
    description='A*搜索算法',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/lamborghini1993/mypypi/tree/master/AStar',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
