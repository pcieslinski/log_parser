# log-parser

## Overview
Log-parser is a CLI tool used to calculate statistics based on 
logs from servers, e.g. Gunicorn. It was designed with a view
to making it easy to extend with further commands, formats 
and statistics.

## Quickstart
The package manager used in the project is [Pipenv](https://pipenv.kennethreitz.org/en/latest/).

The installation of the log-parser is very simple.. You should be 
in the root directory of the project and run the following command:

```bash
bash install.sh
```

Uninstalling is also easy.

```bash
pipenv uninstall log-parser
```

In the `data` directory in the project there is an example log 
file on which you can test the operation of the application.

## Usage
Log-parser has one subcommand implemented, which is called `stats`. 
It is used to calculate statistics based on logs from the server.

The statistics currently implemented and calculated by CLI are:
* number of all requests
* number of individual request statuses
* number of requests per second
* average response size for 2xx


#### **log-parser**
____________________

Getting help for the main command:
```bash
log-parser -h
```


#### **log-parser stats**
____________________

Get help for the stats command:
```bash
log-parser stats -h
```

#### **log-parser stats file**
____________________
Calculating statistics for the entire log file.
```bash
log-parser stats data/gunicorn.log2
```

#### **log-parser stats file --since**
____________________
The log file can also be filtered by date. The first way is 
the `--since` flag. 

An important issue is that the functionality 
is currently implemented in such a way that you must provide 
the full date in this format: `01/Dec/2019:05:07:05`

```bash
log-parser stats data/gunicorn.log2 --since=01/Dec/2019:05:07:05
```

#### **log-parser stats file --until**
____________________
Another option for filtering by date is the `--until` flag:
```bash
log-parser stats data/gunicorn.log2 --until=01/Dec/2019:05:07:05
```

#### **log-parser stats file --since --until**
____________________
Flags can appear together:
```bash
log-parser stats data/gunicorn.log2 --since=01/Dec/2019:05:07:05 --until=01/Dec/2019:10:00:00
```

## Project structure

### CLI
In `./cli` directory there is the main program skeleton and 
individual argument parsers. The addition of another subcommand
can be started by creating a separate argument parser and 
adding a new method to the `LogParser`.
 
### Commands
In `./commands` there is a logic of the `stats` command, as well 
as individual statistics that are calculated within it.

### Parser
Logic is implemented in this part of the project, which helps to
parse individual records from the log file. **Builder Pattern** has 
also been used here, which aims to enable the creation of new 
patterns for other types of logs.

### Renderers
In `./renderers` there are classes that are responsible for 
displaying the results of the application's operation directly 
in the console.


## TODO
1. Enable more user-friendly input of dates into the `--since` 
and `--until` filters.
2. Analyzing and refining the application in terms of algorithmics.
