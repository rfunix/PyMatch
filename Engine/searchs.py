#-*- coding: UTF-8 -*-
import re

def extractGroupsText(**kwargs):
    if  kwargs["stdin"]:
        text = "".join(kwargs["stdin"])  # join text stdin
    else:
        _file = open(kwargs["file"], "r")
        text = "".join(_file.readlines())

    # compile pattern
    regex = re.compile("(?m)(?s){0}".format(kwargs["pattern"]))
    for match in regex.finditer(text):  # for each match in text
        outText = kwargs["groupMatch"]  # text output equal --groupMatch
        groups = []
        if match:
            for group in match.groups():
                groups.append(group)
            for key, group in enumerate(groups):
                regex = re.compile(r"(?<!\\)\({0}\)".format(key+1))
                match = regex.search(str(kwargs["groupMatch"]))
                if match:
                    outText = regex.sub(str(group), outText)
            print outText
