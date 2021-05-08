#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:54:21 2021

@author: maherme
"""

import sys
import importer

module1 = importer.import_('module1', 'module1_source.py', '.')

print('sys says:', sys.modules.get('module1', 'module1 not found'))

import module2
module2.hello()