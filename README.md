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
from logthon import Logthon as Logger

Logthon = Logger(save_log=True)
```

#### Save output on custom file

```
from logthon import Logthon as Logger

Logthon = Logger(save_log=True, filename='/path/to/file')
```

### Define module name on log format

```
from logthon import Logthon as Logger

Logthon = Logger(module_name=__name__)  # or Logger(module_name='my.module.path')

# Example
Logthon.info('This is an info log')
# [2012-01-14 00:00:00] my.module.path - INFO: This is an info log
```

### Info level

```
Logthon.info('This is an info log')
# [2012-01-14 00:00:00] INFO: This is an info log
```

### Warn level

```
Logthon.warn('This is a warn log')
# [2012-01-14 00:00:00] WARN: This is a warn log
```

### Error level

```
Logthon.error('This is an error log')
# [2012-01-14 00:00:00] ERROR: This is an error log
```

### Success level

```
Logthon.success('This is a success log')
# [2012-01-14 00:00:00] SUCCESS: This is a success log
```

### Critical level

```
Logthon.critical('This is a critical log')
# [2012-01-14 00:00:00] CRITICAL: This is a critical log
```

### Debug level

```
Logthon.debug('This is a debug log')
# [2012-01-14 00:00:00] DEBUG: This is a debug log
```

## Log and exit program with error code
You can log a message and exit the program defining optionally and error code.
```
# Default log level is CRITICAL
# Default error code is 1
Logthon.log_and_exit_with_code('This is a message')
```

If you want to define log level, you need to import level you want
```
from logthon.logthon import INFO_LEVEL
from logthon.logthon import WARN_LEVEL
from logthon.logthon import ERRO_LEVEL
from logthon.logthon import SUCC_LEVEL
from logthon.logthon import CRITICAL_LEVEL
from logthon.logthon import DEBUG_LEVEL

# e.g. we want to log with error level and exit
Logthon.log_and_exit_with_code('Log message', level=ERRO_LEVEL)

# e.g. we want to log with debug level and exit with code 5
Logthon.log_and_exit_with_code('Log message', level=DEBUG_LEVEL, error_code=5)
```

## Log a prettified dictionary 
You can log a message with a dictionary pretty printed
```
# Default log level is DEBUG 
Logthon.pretty_print('This is a message', {'key': 'word'})
```

If you want to define log level, you need to import level you want
```
from logthon.logthon import INFO_LEVEL
from logthon.logthon import WARN_LEVEL
from logthon.logthon import ERRO_LEVEL
from logthon.logthon import SUCC_LEVEL
from logthon.logthon import CRITICAL_LEVEL
from logthon.logthon import DEBUG_LEVEL

# e.g. we want to log with info level
Logthon.pretty_print('This is a message', {'key': 'word'}, level=INFO_LEVEL)
```
## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the GNU General Public License v3 (GPLv3), read [LICENSE](LICENSE) for details 

## Author

* **Giuseppe "mastrobirraio" Matranga** - *Initial work* - [Github](https://github.com/mastrobirraio)
