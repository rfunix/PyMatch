# -*- coding: UTF-8 -*-


import optparse
import sys
import re
import pprint
from Engine.searchs import extractGroupsText

sys.path.insert(0, '..')

def groupMatchOut(**kwargs):
    #groupMatch = "(1)teste(2)"
    if kwargs["groupMatch"]:
        i=0
        listGroups = []
        #TESTANDO CONTADOR DE GRUPOS
        while(i <= 9):
            reg = re.compile(r"(?<=[^\\])\({0}\)".format(i)) #Verify groups
            if reg.search(kwargs["groupMatch"]):
                listGroups.append(i)
            i +=1
        print listGroups
      
    
def printHelpMessage():
    print """
Options:
  -h, --help                      show this help message and exit
  -p, --pattern     <pattern>     pattern to find
  -g, --groupmatch  <groupmatchs> combine text with groupmatchs
  --update                        upgrade to latest version
  
  Observation:    stdin works
              """

def basicInfo():
     print """
            pyout - auxiliary tool  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer) - @rfunix\n
              Usage: pyout.py  [-p/--pattern    <pattern>    ]
                               [-g/--groupmatch <groupmatchs>]
                               [--update   Update from github]
                               [Observation:    stdin works  ]
                               
      \n              Get basic options and Help, use: -h\--help
              """
    
def createOptions():
    kwargs = {}
    if not sys.stdin.isatty():
        kwargs["stdin"] = sys.stdin.readlines()
    else:
        kwargs["stdin"] = None
        
#    data = sys.stdin.readlines()
#    if data:
#        print data
        
    parser = optparse.OptionParser(add_help_option=False)
    
    parser.add_option("-p", "--pattern", dest="pattern", type="string",
                                        help="pattern to find",)
                                        
    parser.add_option("--update", dest="update", action="store_true", \
                                        help="update to latest version",)
    
    parser.add_option("-g", "--groupmatch", dest="groupMatch", type="string",
                                        help="combine group match with text",)

    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")
   
   
    options, args = parser.parse_args()
    
    kwargs["groupMatch"] = options.groupMatch
    kwargs["pattern"] = options.pattern
    
    if kwargs["stdin"] == None:
      print "Invalid value in stdin"
      return


    help = options.help
    
    if help:
       printHelpMessage()
       return
   
    # if (kwargs["groupMatch"] == None or
    #     kwargs["stdin"]  == None or
    #     kwargs["pattern"] == None):
    #         print basicInfo()
    #         return


    groups = extractGroupsText(**kwargs)
    
def main():
    createOptions()    


    
if __name__ == "__main__":
    main()