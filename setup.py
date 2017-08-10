from setuptools import setup


setup(name='lunchboy',
      version='0.1',
      description='Lunch without #lunch',
      url='http://github.com/lisunshiny/lunchboy',
      author='Liann Sun',
      author_email='liann@appboy.com',
      license='MIT',
      packages=['lunchboy'],
      install_requires=['Scrapy'],
      scripts=['bin/lunchboy']
      zip_safe=False)
