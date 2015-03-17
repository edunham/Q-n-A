#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/poll/")

from hello import app as application
application.secret_key = 'TODO FIXME PUT A SECRET KEY HERE'
