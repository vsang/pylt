#!/usr/bin/env python
#
#    Copyright (c) 2007-2009 Corey Goldberg (corey@goldb.org)
#    License: GNU GPLv3
#
#    This file is part of Pylot.
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.  See the GNU General Public License 
#    for more details.
#


#  All configuration options here are overridden if specified on the command line

AGENTS = 1
DURATION = 60  # secs
RAMPUP = 0  # secs
INTERVAL = 0  # millisecs
TC_XML_FILENAME = 'testcases.xml'
OUTPUT_DIR = None
TEST_NAME = None
LOG_MSGS = False
BLOCKING = False
GUI = False
COOKIES_ENABLED = True
HTTP_DEBUG = False  # really only useful if combined with blocking mode