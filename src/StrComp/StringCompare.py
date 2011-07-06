from mod_python import psp

def charset(string):
    d = {}
    for x in list(string):
        d[x] = 1
    chars = list(d.keys())
    chars.sort()
    return chars

'''
implementation from http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
'''
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s1:
        return len(s2)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):   
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

def hamming(s1, s2):
    if len(s2) > len(s1):
        return hamming(s2, s1)
    shortLen = len(s2)
    longLen = len(s1)
    ham = []
    for i in range(longLen):
        if i >= shortLen or s1[i] != s2[i]:
            ham.append(i)
    return ham

def index(req):
    req.content_type = "text/html"
    tmpl = psp.PSP(req, filename='Empty.psp')
    tmpl.run(vars = {'string1': 'Hallo Welt!', 'string2': 'Hello World!'})
    return
def compare(req, s1='', s2=''):
    req.content_type = "text/html"
    
    s1 = req.form.getfirst('s1', '')
    s2 = req.form.getfirst('s2', '')
    shortLen = min(len(s1), len(s2))
    longLen = max(len(s1), len(s2))
   
    tmpl = psp.PSP(req, filename='StringCompare.psp')
    tmpl.run(vars = { 'string1' : s1, 'string2' : s2, 'hamming' : hamming(s1, s2), 'levenshtein': levenshtein(s1, s2), 'longLen': longLen, 'shortLen': shortLen, 'charset1': charset(s1), 'charset2': charset(s2) })
    return