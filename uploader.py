#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import helper
import commands
import hashlib
import time

class Uploader:

	__file = None

	project_path = ''
	github_username = ''
	github_repo = ''

	# default master branch
	__MARKDOWN_IMG_URL = '![{}](https://github.com/{}/{}/raw/master/{})';


	def __init__(self, file):
		self.__file = file
		self.project_path = os.environ.get('project_path')
		self.github_username = os.environ.get('github_username')
		self.github_repo = os.environ.get('github_repo')

		self.run()

	def run(self):

		helper.notify('Uploading','Please wait for a while')

		# Image suffix
		a,b,suffix = self.__file.filename.rpartition('.')


		# Get image
		filename = str(hashlib.md5(self.__file.filename).hexdigest())+str(int(time.time()))+'.'+suffix
		self.__file.save(self.project_path+'/'+filename)

		# Git
		cmd = '''
		cd {}
		git add .
		git commit -m 'clipboard'
		git push'''.format(self.project_path)

		a,b = commands.getstatusoutput(cmd)

		if a == 0:
			self.__write_to_doc(filename)
			helper.notify('Success','Upload success')
		else:
			# Alfred workflow debugger console
			sys.stderr.write(str(b))
			helper.notify('Error','Git error')

	def __write_to_doc(self, filename):
		remote_url = self.__MARKDOWN_IMG_URL.format(filename,self.github_username,self.github_repo,filename)
		os.system('echo "{}"|pbcopy'.format(remote_url))
		a,b = commands.getstatusoutput('pbpaste')
		self.print_pasteboard_content()

	# this func is forked from `kaito-kidd/markdown-image-alfred` thanks
	def print_pasteboard_content(self):
	    """从剪贴板打印出内容"""
	    write_command = (
	        'osascript -e \'tell application '
	        '"System Events" to keystroke "v" using command down\''
	    )
	    os.system(write_command)


