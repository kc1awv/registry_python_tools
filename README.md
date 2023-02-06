# registry_python_tools
Python scripts for mrefd reflector registry

## UpdateMrefdHosts.py

Creates a hostfile that can be used with [M17Gateway](https://github.com/g4klx/M17Gateway)

Requires `requests` and `pandas`

`pip install requests pandas`

```
usage: UpdateMrefdHosts.py [-h] [-u URL] [-p PATH] [-o OUTFILE]

options:
  -h, --help
        show this help message and exit
  -u URL, --url URL     
        URL to lookup mrefd reflector JSON (default: https://reflectors.m17.link/ref-list/json)
  -p PATH, --path PATH
        Path to save the hosts file (Defaults to current working directory)
  -o OUTFILE, --outfile OUTFILE
        Output file name (default: M17Hosts.txt)
```
