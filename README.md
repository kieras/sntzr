# SNTZR

A small tool to help clean up log files.

## Installation

Run:

```bash
pipx install git+https://github.com/kieras/sntzr.git
```

## Usage

Run:

```bash
sntzr --help
```

Sample configuration file:

```yaml
---
global_regex:
  'gr://machine_name': '[A-Z0-9-]+'
  'gr://ipv4': '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
  'gr://host': '(?:[0-9A-Za-z][0-9A-Za-z-]{0,62})(?:\.(?:[0-9A-Za-z][0-9A-Za-z-]{0,62}))*'

patterns:
  - 'data': 'xml'
    'field': 'MachineName'
    'pattern': 'gr://machine_name'
    'replace': 'machine_name'
    'activated': true
  - 'data': 'xml'
    'field': 'IPAddress'
    'pattern': 'gr://ipv4'
    'replace': 'ipv4'
    'activated': true
  - 'data': 'raw'
    'field': '-'
    'pattern': 'gr://ipv4'
    'replace': 'ipv4'
    'activated': true
  - 'data': 'raw'
    'field': '-'
    'pattern': 'NCR'
    'replace': 'ALOHA'
    'activated': false
  - 'pattern': 'gr://host'
    'replace': 'www.acme.com'
```

Detailed info about each configuratio file field:

global_regex:

You should define the regex and choose a proper name so that it can be reused by patterns. The sytax is:

```
  'gr://<name_of_pattern>': '<regex>'
```

patterns:

```
  - 'data': 'xml'
    'field': 'Name'
    'pattern': 'gr://<pattern_reference>'
    'replace': '<replacer_function_name>'
    'activated': true
```

You should define 5 fields here.
  - data: It holds the type of data it is going to be looked for. The value might be: 'xml', 'kv', 'raw'.
  - field: It holds the name of the field. Ex: if the 'data': 'xml' the field might be 'Name' so we have the full representation for that: \<Name>value\</Name>
  - pattern: It holds the regex itself, a reference to a global_regex or a raw value.
  - replace: It holds the function name used to replace the pattern found or this raw value will be used instead.
  - activated: If you want to use this pattern, set to true, false otherwise.

* obs: You may ommit the data, field and activated fields which are not mandatory. In this case, default values will be used: 'raw', '-', 'true' respectively.


## Install from local directory

Clone the repo and execute the command:

```bash
pipx install -e --force .
```
