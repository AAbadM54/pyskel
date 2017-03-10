[![Build Status](https://travis-ci.org/thibalbo/pyskel.svg?branch=master)](https://travis-ci.org/thibalbo/pyskel)
[![Coverage Status](https://coveralls.io/repos/github/thibalbo/pyskel/badge.svg)](https://coveralls.io/github/thibalbo/pyskel)

# Pyskel

A simple python project skeleton.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to setup your [Travis CI](https://travis-ci.org/) and [Coveralls](https://coveralls.io/) account.

### Installing

You just need to install the packages in `requirements.txt`:

```
virtualenv -p python3.5 venv
source venv/bin/activate
pip install -r requirements.txt
```

You run the project using the run.py file. You need to provide handler and environment to execute.

```
python run.py HANDLER ENV
python run.py --handler HANDLER --env ENV
```

Examples:

```
python run.py do_handle qa
python run.py --handler do_handle --env prod
```


## Running the tests

You run tests using the `nose2` package.

```
nose2 test -v
nose2 test -v --with-coverage
nose2 test -v --coverage pyskel --with-coverage
```

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](URL) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Thiago Balbo** - *Initial work* - [PurpleBooth](URL)

See also the list of [contributors](URL) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
