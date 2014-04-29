# -*- coding: UTF-8 -*-

import optparse
import sys
import re
import pprint
from Engine.searchs import extractGroupsText


def basicInfo():
    print """
            pyout - Text Output Tool  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer) - @rfunix\n
              Usage: pyout.py
                           [-p/--pattern    <pattern>    ]
                           [-g/--groupmatch <groupmatchs>]
                           [-f/--file <file>]
                           [--update   Update from github]
                           [Observation:    stdin works  ]

      \n              Get basic options and Help, use: -h\--help
              """
              
def main():
    kwargs = {}
    if not sys.stdin.isatty():
        kwargs["stdin"] = sys.stdin.readlines()
    else:
        kwargs["stdin"] = None

    parser = optparse.OptionParser()

    parser.add_option("-p", "--pattern", dest="pattern", type="string",
                      help="pattern to find",)

    parser.add_option("-f", "--file", dest="file", type="string",
                      help="search GroupMatches in File",)

    parser.add_option("--update", dest="update", action="store_true",
                      help="update to latest version",)

    parser.add_option("-g", "--groupmatch", dest="groupMatch", type="string",
                      help="combine group match with text",)

    options, args = parser.parse_args()

    try:
        kwargs["groupMatch"] = options.groupMatch
        kwargs["pattern"] = options.pattern
        kwargs["file"] = options.file

        if (kwargs["groupMatch"] == None or
                kwargs["pattern"] == None or
                (kwargs["file"]) == None and
                kwargs["stdin"] == None):
            basicInfo()
            return

        groups = extractGroupsText(**kwargs)
    except Exception, e:
        parser.error("Please select an option or use --help for help")
        return


if __name__ == "__main__":
    main()
