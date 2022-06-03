# WSCBS_Assignment4b_brane_getfeatures

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6612428.svg)](https://doi.org/10.5281/zenodo.6612428)

This implementation is the features engineering part of Titanic Project ([Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)).

## Usage
This is the **second** package in our pipeline of project([Assignment 4b](https://github.com/TISNN/WSCBS_Assignment4b)). It does data preprocessing and generates some new features combining the training and test set. Results will be saved to `./data`

Each package, as a part in the brane pipeline, can be run separately to produce the corresponding results (processed data, ML models, visualization)

## Requirements

- Complete installation of Brane ([manual1](https://wiki.enablingpersonalizedinterventions.nl/user-guide/software-engineers/installation.html), [manual2](https://wiki.enablingpersonalizedinterventions.nl/admins/installation/get-binaries.html))
- Brane Dependencies (also in [manual1](https://wiki.enablingpersonalizedinterventions.nl/user-guide/software-engineers/installation.html), [manual2](https://wiki.enablingpersonalizedinterventions.nl/admins/installation/get-binaries.html))

## Setup

### By source code (Git repository)

1. Download the source code by `git clone`
```shell
$ git clone https://github.com/TISNN/brane-getfeatures.git
$ cd brane-getfeature
```
2. Build brane package by .yml file
```shell
$ brane build container.yml
```
3. Check availablity
```shell
$ brane list
```

### By brane package method

1. import brane package
```shell
$ brane import TISNN/brane-getfeatures
```
2. Check availablity
```shell
$ brane list
```

If you see `getfeatures` package with version==8.0.0, it was successfully built.

## Run
```shell
$ brane --debug test --data ./data getfeatures
```
1. Choosing the *processing* function
2. Enter "**EDA**" as source string
3. It runs correctly with output "features was saved at /data"
4. The result will be save to `./data` folder in your local file system.

## Tests for package
### Automated builds and running (CI/CD)
This repository is equipped with a GitHub Action workflow. 

Every time we push the code to this repository, it will automatically run the tests using branescript. The build status of the project can be viewed on the [Actions](https://github.com/TISNN/brane-getfeatures/actions) page.

- The `brane` is the executable compiled binary file, used for automated testing.
- The `test.txt` is the branescript used for automated testing.

### Unit pytest
You can also test for a single function by python. 

Parameters can be changed in file: `pytest.py`
```shell
$ python pytest.py
```
