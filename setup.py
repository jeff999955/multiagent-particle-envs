import os

from setuptools import setup, find_packages

# Read requirements.txt
with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="multiagent",
    version="0.0.1",
    description="Multi-Agent Goal-Driven Communication Environment",
    url="https://github.com/openai/multiagent-public",
    author="Igor Mordatch",
    author_email="mordatch@openai.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)
