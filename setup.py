from setuptools import setup


setup(name='braise',
      version='0.3',
      description='Lunch without #lunch',
      url='http://github.com/lisunshiny/braise',
      author='Liann Sun',
      author_email='liann@braze.com',
      license='MIT',
      packages=['braise'],
      install_requires=['Scrapy'],
      scripts=['bin/lunch'],
      zip_safe=False)
