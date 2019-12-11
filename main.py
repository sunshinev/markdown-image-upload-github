#!/usr/bin/python
# -*- coding: UTF-8 -*-

import helper
from uploader import Uploader
from PIL import ImageGrab

def main():
	# Issue: if your screen is extend, please make sure the `Screen show profile` is LCD or normal RGB
	try:
		# Get latest file from os clipboard
		img = ImageGrab.grabclipboard()

	except BaseException as e:
		helper.notify('Error',str(e))
	else:
		if img is not None:
			# Move and upload
			Uploader(img)
		else:
			helper.notify('Empty','The clipboard is empty')



if __name__ == '__main__':
	main()