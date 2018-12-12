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
        'Programming Language :: Python :: 3.7',
        'Topic :: Command Line :: Application',
      ],
      keywords='Parking lot',
      url="https://gist.github.com/KhushalGoyal/66619cfe0df47ed3a76771fc50f6a752",
      author='khushalGoyal',
      author_email='khushal.goyal16@gmail.com',
      license='-',
      packages=['parkinglot'],
      install_requires=[
          'markdown','pandas'
      ],
      entry_points={
          'console_scripts': ['parking@lot=parkinglot.test2:main'],
      },
      include_package_data=True,
      zip_safe=False)
