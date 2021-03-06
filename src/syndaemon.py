#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
__author__='atareao'
__date__ ='$01/09/2013'
#
# Configure the Touchpad
#
# Copyright (C) 2013 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
import shlex
import os.path
import subprocess

def run(comando):
	print(comando)
	args = shlex.split(comando)
	p = subprocess.Popen(args, bufsize=10000, stdout=subprocess.PIPE)
	answer = p.communicate()[0].decode('utf-8')
	return answer

def run2(comando):
	print(comando)
	args = shlex.split(comando)
	p = subprocess.Popen(args, bufsize=10000, stdout=subprocess.PIPE)

class Syndaemon(object):

	def __init__(self,waiting_time=2):		
		self.waiting_time = waiting_time
	
	def start(self):
		if self.is_running():
			if os.path.exists('/tmp/touchpad-indicator-syndaemon.pid'):
				return True
			else:
				self.stop()
		run2('syndaemon -i %0.1f -d -p /tmp/touchpad-indicator-syndaemon.pid  &'%(self.waiting_time))
		return self.is_running()
		
	def stop(self):
		if self.is_running():
			return run('killall syndaemon')
		True
		
	def is_running(self):
		return run('pidof syndaemon')!=''

	#def __del__(self):
	#	run('killall syndaemon')

if __name__ == '__main__':
	import time	
	syndaemon = Syndaemon(0.5)
	syndaemon.stop()
	print(syndaemon.start())
	'''synclient.stop()'''
	time.sleep(5)
	syndaemon.stop()
	print(syndaemon.is_running())
	'''
	print(synclient)
	print(synclient.set('TouchpadOff','1'))
	time.sleep(3)
	print(synclient.set('TouchpadOff','0'))
	print(synclient)
	'''
	exit(0)
