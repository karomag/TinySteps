# -*- coding: utf-8 -*-
import json

from data import goals, teachers


def main():
    """
    The Convertor data from .py to .json
    :return: .json files from python objects
    """
    with open('goals.json', "w", encoding='utf-8') as f:
        json.dump(goals, f, ensure_ascii=False, indent=2)
    with open('teachers.json', "w", encoding='utf-8') as f:
        json.dump(teachers, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
