from .base import *

try:
 	from .local import *
 	live = False
 	print 'local'
except:
	live = True

if live:
	from .production import *
	print 'production'

print live
