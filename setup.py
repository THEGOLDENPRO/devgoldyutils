from setuptools import setup, find_packages

classifiers = [
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9'
]

setup(
  name='devgoldyutils',
  version="2.0",
  description='My own utils libary I use throught all my python projects.', 
  url='https://github.com/THEGOLDENPRO/Dev-Goldy-Utils', 
  project_urls={"Bug Tracker": "https://github.com/THEGOLDENPRO/Dev-Goldy-Utils/issues"}, 
  author='Dev Goldy', 
  author_email='goldy@novauniverse.net', 
  license='MIT', 
  classifiers=classifiers, 
  keywords=["Goldy Utils", "Dev Goldy Utils", "devgoldyutils"], 
  packages=find_packages(), 
  include_package_data=True,
  install_requires=open('requirements.txt').read(),
  python_requires=">=3.8"
)