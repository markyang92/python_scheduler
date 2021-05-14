#!/usr/bin/python3

import src.parser



if __name__ == "__main__":
    scenario1 = src.parser.parsing()
    if src.parser.debug:
        print(scenario1.schedule)
        print(scenario1.log)
