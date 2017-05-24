from setuptools import setup, find_packages
import pyskel

setup(name='pyskel',
      author=pyskel.__author__,
      author_email=pyskel.__email__,
      version=pyskel.__version__,
      description='Create python project structure',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'rpyskel = pyskel.__main__:main',
        ]}
      )
