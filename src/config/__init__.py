from flask import Flask 
from dotenv import dotenv_values
import os
from collections import namedtuple

class Env:

    def __init__(self):
        env_path = os.getcwd()
        self._config = {
            **dotenv_values(f'{env_path}/.env'),
            **os.environ,
        }

    @property
    def config(self):
        return self._config
    
    @config.setter
    def config(self, config):
        self._config = config
    
    def get_item(self, key: str, default = None):
        if key in self.config:
            return self.config[key]
        return None

environment = Env()


def init_app(app: Flask, runtime_config: dict = None):

    if runtime_config == None:
        runtime_config = {}

    env = {
        **environment.config,
        **runtime_config
    }

    environment.config = env

    app.config.from_object(config_to_object(env, app))


    
def config_to_object(config, app):

    keys = list(config.keys())
    for key in keys:    
        #Remove underscore keys (Flask rules)
        if key.startswith("_"):
            del config[key]
        else:
            #Remove empty values
            value = config[key]
            if not value:
                del config[key]

    return namedtuple("Config", config.keys())(*config.values())