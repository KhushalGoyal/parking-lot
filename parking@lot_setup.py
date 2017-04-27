from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Parking@lot',
      version='0.1',
      description='Parking lost application',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='Parking lot',
      url="khushal.goyal16@gmail.com",
      author='khushalGoyal',
      author_email='khushal.goyal16@gmail.com',
      license='MIT',
      packages=['parkinglot'],
      install_requires=[
          'markdown','pandas'
      ],
      entry_points={
          'console_scripts': ['parking@lot=parkinglot.test2:main'],
      },
      include_package_data=True,
      zip_safe=False)