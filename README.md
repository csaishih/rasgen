# RaS Generator
**RaS Generator** is a tool that generates class schedules for University of Toronto students. The goal is to provide a simpler solution to course planning.

## Current Version
**1.0.0 (Alpha)**

## Installation
Clone this repo
```bash
$ git clone https://github.com/g3aishih/rasgen.git
```
Make sure you have the following dependencies installed on your machine
* [python 2.x](https://www.python.org/download/releases/2.7/) (v2.7 recommended)
* cPickle: Should be included in python2.7
* [requests](http://docs.python-requests.org/en/latest/user/install/#distribute-pip)
```bash
$ pip install requests
```
* [lxml](http://lxml.de/installation.html)
```bash
$ pip install lxml
```
* [MongoClient](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)
```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```
To run MongoDB
```bash
$ sudo service mongod start
```
To stop MongoDB
```bash
$ sudo service mongod stop
```

## How to use the scraper
Go to the directory with `scraper.py` and run:
```bash
$ python scraper.py
```
If `courses.dat` does not exist in your working directory it will be created for you.
To update `courses.dat` with the most current data from [coursefinder.utoronto.ca](http://coursefinder.utoronto.ca) run
```bash
$ python scraper.py -u
```
