#coding=utf-8
import sys
import webbrowser
args = sys.argv[1:]
args.reverse()
print ''.join(reversed(sys.argv[1:]))
webbrowser.open('http://www.python.org')