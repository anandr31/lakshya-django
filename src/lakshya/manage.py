#!/usr/bin/env python
import os
import sys

DIRNAME = os.path.dirname(__file__)
_parent = lambda x: os.path.normpath(os.path.join(x, '..'))

EXT_APPS = os.path.join(DIRNAME, 'ext')
if not EXT_APPS in sys.path:
    sys.path.insert(0,EXT_APPS)

if DIRNAME in sys.path:
    sys.path.remove(DIRNAME)
    
sys.path.insert(0,DIRNAME)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lakshya.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
