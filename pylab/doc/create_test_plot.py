from openalea.core.alea import *
pm = PackageManager()
pm.init(verbose=False)
from pylab import *

tests = ['contour', 'cohere']

for test in tests:
    res = run_and_display(('openalea.pylab.test', test),{},pm=pm)
    #savefig('%.png', test)
    #close('all')
    import time

