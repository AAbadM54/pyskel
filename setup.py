from distutils.core import setup

setup(name='pyskel',
      version='1.0.0',
      description='Create python project structure',
      author='Thiago Balbo',
      author_email='thiago.dbalbo@gmail.com',
      packages=[
        'pyskel',
        'pyskel.service',
        'pyskel.domain',
        'pyskel.model',
        'test',
        'test.service',
        'test.domain',
        'test.model',
        'log',
        'deploy'],
     )
