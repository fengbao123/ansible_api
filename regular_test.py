import re

a = r'abc?'

b = 'abcccc'


if re.match(a,b):
    print 'match'
else:
    print 'not match'

