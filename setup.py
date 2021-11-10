from setuptools import setup

setup(name='fuserock',
      version='1.0',
      description='FUSion-Evaporation ReactiOn Calculator of Kinematics',
      url='',
      author='Jorge Romero',
      author_email='joromero@jyu.fi',
      license='GPL-3.0',
      packages=['fuserock'],
      install_requires=[
          'argparse',
      ],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'fuserock = fuserock:main'
        ]},
    )