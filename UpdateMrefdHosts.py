#!/usr/bin/env python
__author__ = "Steve Miller KC1AWV"
__copyright__ = "Copyright 2023, KC1AWV"
__credits__ = ["Steve Miller"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Steve Miller KC1AWV"
__email__ = "vt81nuj0@4wrd.cc"
__status__ = "Production"

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter('ignore')

import os
import requests
import pandas as pd

# Parse command line options
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-u', '--url', default='https://reflectors.m17.link/ref-list/json', help="URL to lookup mrefd reflector JSON")
parser.add_argument('-p', '--path', default=os.getcwd(), help="Path to save the hosts file (Defaults to current working directory)")
parser.add_argument('-o', '--outfile', default="M17Hosts.txt", help="Output file name")
args = vars(parser.parse_args())

# Set up parameters
url = args['url']
path = args['path']
outfile = args['outfile']
fullpath = os.path.join(path, outfile)

headers = {
    'User-Agent': 'updateMrefdHosts/1.0 (Python)',
}
response = requests.request("GET", url, headers=headers).json()

data = pd.json_normalize(response, record_path=['items'])
df = data[['designator','ipv4','port']]
df = df.assign(designator = 'M17-' + df.designator)
df.to_csv(fullpath, sep=' ', index=False, header=False)
