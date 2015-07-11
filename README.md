# RaS Generator
**RaS Generator** is a tool that generates class schedules for University of Toronto students. The goal is to provide a simpler solution to course planning.

## Current Version
1.0.0 (Alpha)

## Installation
Clone this repo
```bash
$ git clone https://github.com/g3aishih/rasgen.git
```
Make sure you have the following dependencies installed on your machine
* python 2.x
* requests
* lxml
* cPickle
* MongoClient

## How to use - Scraper
Go to the directory with `scraper.py` and run:
```bash
$ python scraper.py
```
If `courses.dat` does not exist in your working directory it will be created for you.
To update `courses.dat` with the most current data from [coursefinder.utoronto.ca](http://coursefinder.utoronto.ca) run
```bash
$ python scraper.py -u
```
