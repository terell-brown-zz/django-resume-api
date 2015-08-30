from .base import *

try:
 	from .new import *
 	live = False
 	print 'l_new'

except:
	live = True

if live:
	from .w import *
	#print 'production'

