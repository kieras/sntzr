# SNTZR

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

patterns:
  - 'data': 'xml'
    'field': 'MachineName'
    'pattern': 'gr://machine_name'
    'replace': 'machine_name'
  - 'data': 'xml'
    'field': 'IPAddress'
    'pattern': 'gr://ipv4'
    'replace': 'ipv4'
  - 'data': 'raw'
    'field': '-'
    'pattern': 'gr://ipv4'
    'replace': 'ipv4'
  - 'data': 'raw'
    'field': '-'
    'pattern': 'NCR'
    'replace': 'ALOHA'
```

Detailes info about each configuratio file field:

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
```

You should define 4 fields here.
  - data: It holds the type of data it is going to be looked for. The value might be: 'xml', 'kv', 'raw'.
  - field: It holds the name of the field. Ex: if the 'data': 'xml' the field might be 'Name' so we have the full representation for that: \<Name>value\</Name>
  - pattern: It holds the regex itself, a reference to a global_regex or a raw value.
  - replace: It holds the function name used to replace the pattern found or a raw value it will be replaced by

## Install from local directory

Clone the repo and execute the command:

```bash
pipx install -e --force .
```
