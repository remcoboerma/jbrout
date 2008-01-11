# -*- coding: UTF-8 -*-
##
##    Copyright (C) 2005 manatlan manatlan[at]gmail(dot)com
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation; version 2 only.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##


from __main__ import JPlugin

import datetime

def cd2d(f): #yyyymmddhhiiss -> datetime
   return datetime.datetime(int(f[:4]),int(f[4:6]), int(f[6:8]),int(f[8:10]),int(f[10:12]),int(f[12:14]))


class Plugin(JPlugin):
    """to change the datetime of a photo"""

    __author__ = "manatlan"
    __version__ = "1.1"


    def menuEntries(self,l):
        return [(2500,_("Change Datetime"),True,self.redate,None)]

    def redate(self,list):
        from redate import Winredate

        Winredate.defaultDate = cd2d(list[0].date)
        win = Winredate()

        ret=win.loop()[0]
        if ret:
            vw,vd,vh,vi,vs = ret
            try:
                for i in list:
                    self.showProgress( list.index(i), len(list) , _("Redating") )
                    i.redate(vw,vd,vh,vi,vs)
            finally:
                self.showProgress()

            return True
        else:
            return False