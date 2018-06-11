try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='BatteryAlert',
      version='1.1.8',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      packages=['src', ],
      entry_points={
          'console_scripts': ['batteryalert=BatteryAlert:main'],
      },
      description="A speaking battery's charge level",
      long_description=open('README').read(),
      keywords=['reminder', 'battery',
                'notification', 'voice alert', 'python'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring'
      ],
      )
