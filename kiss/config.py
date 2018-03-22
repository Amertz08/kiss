import os
import collections
import pprint

import yaml

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIR = 'templates'
BUILD_DIR = 'build'
DATA_DIR = 'data'


class Config(collections.MutableMapping):

    def __init__(self):
        self.store = {
            'IGNORE': [],
            'CONFIG_FILE': '',
            'TEMPLATE_DIR': TEMPLATE_DIR,
            'BUILD_DIR': BUILD_DIR,
            'DATA_DIR': DATA_DIR,
            'PROJECT_DIR': os.getcwd(),
            'ENV': None
        }

        conf_file = os.path.join(os.getcwd(), '.kiss.yml')
        if os.path.exists(conf_file):
            self.store['CONFIG_FILE'] = conf_file
            with open(self.store['CONFIG_FILE'], 'r') as conf:
                data = yaml.load(conf)
            if 'ignore' in data:
                if isinstance(data['ignore'], str):
                    self.store['IGNORE'] = [data['ignore']]
                else:
                    self.store['IGNORE'] = data['ignore']

        self.store['ENV'] = Environment(
            loader=FileSystemLoader(self.store['TEMPLATE_DIR']),
            autoescape=select_autoescape(['html'])
        )

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key

    def __repr__(self):
        return pprint.pformat(self.store, indent=4)

    def render(self, template_name, *args, **kwargs):
        template = self.store['ENV'].get_template(template_name)
        return template.render(*args, **kwargs)
