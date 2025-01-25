from setuptools import setup, find_packages

setup(
    name="Medical Chatbot",
    version="0.0.0",
    author="Aman Vishwakarma",
    author_email="rraman0923@gmail.com",
    packages=find_packages(), #this will try to find __init__.py file and whenever it will find it will consider that folder as local package
    install_requires=[]
)