#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys
def firstProg(text):
  text1 = "Hello " + text
  return text1

def main():
  fields = {
  "yourName": {"required": True, "type": "str"}
  }
  module = AnsibleModule(argument_spec=fields)
  yourName = os.path.expanduser(module.params['yourName'])
  print(yourName)
  newName = firstProg(yourName)
  module.exit_json(msg=newName)

if __name__ == '__main__':
  main()
