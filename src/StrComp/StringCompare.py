from mod_python import psp

def index(req):
   compare(req)
   return
def compare(req, s1='', s2=''):
   req.content_type = "text/html"
   '''
   hamming = 0
   for i, c1 in enumerate(s1):
     hamming = hamming + abs(cmp(c1, s2[i]))
'''
   tmpl = psp.PSP(req, filename='StringCompare.psp')
   shortLen = max(len(s1), len(s2))
   tmpl.run(vars = { 'string1' : s1, 'string2' : s2, 'hamming' : -1, 'shortLen': shortLen })
   return