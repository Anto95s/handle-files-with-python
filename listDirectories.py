#!/usr/bin/python

import os

dirs = os.walk("../")

for i in dirs:
	print(i)