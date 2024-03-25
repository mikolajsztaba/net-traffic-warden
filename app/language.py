"""
TBD
"""
import yaml


def read_prompts_from_yaml(file_path):
    """
    TBD
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data
