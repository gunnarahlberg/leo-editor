# -*- coding: utf-8 -*-
#@+leo-ver=5-thin
#@+node:ekr.20140526082700.18440: * @file leoRope.py
#@@first
#@+<< leoRope imports >>
#@+middle:ekr.20140526123310.17592: ** class RopeController
#@+node:ekr.20140525065558.15807: *3* << leoRope imports >>
import leo.core.leoGlobals as g
import glob
import imp
import rope
import time
imp.reload(rope)
#@-<< leoRope imports >>
#@+others
#@+node:ekr.20140526123310.17592: ** class RopeController
class RopeController:
    #@+others
    #@+node:ekr.20140525065558.15809: *3* ctor
    def __init__(self,c):
        self.c = c
        self.proj = rope.base.project.Project(g.app.loadDir)
    #@+node:ekr.20140525065558.15806: *3* modules
    def modules(self):
        '''Return full path names of all Leo modules.'''
        aList = glob.glob(g.os_path_join(g.app.loadDir,'*.py'))
        return sorted(aList)
    #@+node:ekr.20140525065558.15808: *3* path
    def path(self,fn):
        return g.os_path_join(g.app.loadDir,fn)
    #@+node:ekr.20140525065558.15805: *3* refactor
    def refactor(self):
        '''Perform refactorings.'''
        proj = self.proj
        m = proj.get_resource(self.path('leoAtFile.py'))
        s = m.read()
        # Important: get an offset in actual code.
        s = rope.base.simplify.real_code(s)
        tag1 = 'atFile'
        tag2 = self.pep8_class_name(tag1)
        offset = s.find(tag1)
        if offset > -1:
            changes = rope.refactor.rename.Rename(proj,m,offset).get_changes(tag2)
            g.trace(changes.get_description())
        else:
            g.trace('not found',tag)
        # prog.do(changes)
    #@+node:ekr.20140525065558.15812: *3* pep8_class_name
    def pep8_class_name(self,s):
        '''Return the proper class name for s.'''
        assert s
        if s[0].islower():
            s = s[0].upper()+s[1:]
        return s
    #@+node:ekr.20140525065558.15810: *3* run
    def run(self):
        '''run the refactorings.'''
        proj = self.proj
        proj.validate(proj.root)
        self.refactor()
        proj.close()
    #@-others
#@+node:ekr.20140526123310.17593: ** test
def test(c):
    t1 = time.clock()
    RopeController(c).run()
    print('done: %s sec.' % g.timeSince(t1))
#@-others

#@@language python
#@@tabwidth -4
#@@pagewidth 70
#@-leo