from distutils.core import setup
import py2exe 
setup(windows=[{"script":"index.py"}],options={"py2exe":{"includes":["PyQt5.Qt","PyQt5.sip","PyQt5.QtWidgets","PyQt5.QtCore","PyQt5.QtGui"]}})