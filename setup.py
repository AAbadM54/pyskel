from setuptools import setup
import pyskel

setup(name='pyskel',
      version=pyskel.__version__,
      description='Create python project structure',
      author='Thiago Balbo',
      author_email='thiago.dbalbo@gmail.com',
      packages=['pyskel'],
      entry_points={
        'console_scripts': [
            'rpyskel = pyskel.__main__:main',
        ]}
      )
