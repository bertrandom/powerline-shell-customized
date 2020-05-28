# -*- coding: utf-8 -*-

from powerline_shell.utils import BasicSegment
import os

class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline

        hamburger = u"🍔 "
        powerline.append(hamburger, powerline.theme.REPO_CLEAN_FG, powerline.theme.REPO_CLEAN_FG)

