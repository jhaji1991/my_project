import re
import configparser
import os

def load_regex(config_path):
    if not os.path.isfile(config_path):
        raise FileNotFoundError("Configuration file not found.")
    
    config = configparser.ConfigParser()
    config.read(config_path)

    if "settings" not in config or "regex" not in config["settings"]:
        raise KeyError("Regex not found in configuration file.")
    
    return config["settings"]["regex"]

def extract_questions(text, regex_pattern):
    matches = re.findall(regex_pattern, text, re.MULTILINE)
    return matches