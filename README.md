# Logthon

A simple logger for Python

## Getting Started

These instructions will install the logger to your machine.

### Prerequisites

* Python3
* PIP3

### Installation

```
pip3 install logthon
```

## Usage


### Import

#### Classic import

```
from logthon.logthon import Logthon as Logger

Logthon = Logger()
```

#### Save output on file

```
from logthon.logthon import Logthon as Logger

Logthon = Logger(save_log=True)
```

#### Save output on custom file

```
from logthon.logthon import Logthon as Logger

Logthon = Logger(save_log=True, filename='/path/to/file')
```

### Info level

```
Logthon.info('This is an info log')
```

### Warn level

```
Logthon.warn('This is a warn log')
```

### Error level

```
Logthon.error('This is an error log')
```

### Success level

```
Logthon.success('This is a success log')
```

### Critical level

```
Logthon.critical('This is a critical log')
```

### Debug level

```
Logthon.debug('This is a debug log')
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the GNU General Public License v3 (GPLv3), read [LICENSE](LICENSE) for details 

## Author

* **Giuseppe "mastrobirraio" Matranga** - *Initial work* - [Github](https://github.com/mastrobirraio)
